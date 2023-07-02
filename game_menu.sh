#!/bin/bash
# TODO: update function: remove thumbdirs and download again 
export DISPLAY=:0

# Install emulators
# flatpak install mgba
# flatpak install citra


root_dir=$(dirname "$(realpath "$0")")

# import variables: games_dir
source "$root_dir/game_menu.conf"
console_dir=( $(ls -1 "$games_dir") )


# fatal() {
#   echo "FATAL ERROR: $@"
#   exit 1
# }
# trap 'sudo -k' EXIT

# zenity --password | sudo -Sv || fatal "Unable to sudo"


# TODO: pyqt5
function check_requirements {
    progs="wget flatpak setsid xdotool python3"
    for p in $progs; do 
        if ! which $p &>/dev/null; then 
            echo "Program not installed: $p"
            exit 1
        fi
    done


}


function find_thumbnails {
    echo "hei"
}

function download_thumbnails { 

    if [ ! -d "$root_dir/thumbnails" ]; then
        mkdir "$root_dir/thumbnails"
    fi


    for d in "${console_dir[@]}"; do 

        for f in "$games_dir""$d"/*; do 

            file_name="${f##*/}"

            if [ ! -d "$root_dir/thumbnails/$d" ]; then
                mkdir "$root_dir/thumbnails/$d"
            fi

            if [ $d = "gamecube" ]; then

                game_name=$(echo "$file_name" | sed -e 's/\.iso//' -e 's/\.nkit//')
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_GameCube/master/Named_Boxarts/"

            elif [ $d = 'play_station_2' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.iso//')
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Sony_-_PlayStation_2/733507283dd0f52e3b8a47fe0a139be13f82903a/Named_Boxarts/"

            elif [ $d = 'nintendo_64' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.z64//')
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Nintendo_64/c9278f93bfbcb41e4e728b952b25e6cc2ab6830f/Named_Boxarts/"

            elif [ $d = 'nintendo_3ds' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.3ds//')
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Nintendo_3DS/15dcea5c55f3ce0bd25a951616a7990a66e25f2d/Named_Boxarts/"

            elif [ $d = 'game_boy_advance' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.gba//' -e 's/\s*\# GBA\.GBA//')
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Game_Boy_Advance/e0200a10a81e74a565f335b5ef3d9cb7e8e89672/Named_Boxarts/"

            else
                break 
            fi

            search_game=$(echo "$game_name" | sed -e 's/&/_/' -e 's/(U)//')
            data_file="$root_dir/data/$d/Named_Boxarts.txt" # File with *.png names

            match=$(grep -e "$search_game" "$data_file") 
            if [ -n "$match" ]; then 

                # Get line with min char
                img_url=$(echo "$match" | awk '
                length==len {line=line ORS $0}
                NR==1 || length<len {len=length; line=$0}
                END {print line}')

                img_url=$(echo "$img_url" | sed 's/.*->\s*//')
                url="$base_url$img_url"

            else
                echo "Can't find: $game_name"
                continue 
            fi

            # if fail download url; try download url2
            img_url2=$(echo "$img_url" | sed -e 's/(.*)//g')
            img_url2=$(echo "$img_url2" | sed -e 's/\.png/(USA)\.png/')
            url2="$base_url$img_url2"

            if [ ! -f "$root_dir/thumbnails/$d/$file_name.png" ]; then 

                # Save filename corresponding to rom name. 
                # download 1. attempt
                wget -q -O "$root_dir/thumbnails/$d/$file_name.png" "$url" && continue

                # download 2. attempt
                wget -q -O "$root_dir/thumbnails/$d/$file_name.png" "$url2" || echo "download failed: $img_url2. No more retries"
            fi


        done


    done

}



function game_picker {

    # run with sxiv 
    # choice=$(sxiv -t -z 150 -of $root_dir/thumbnails/**/*)
    # choice=$(echo "$choice" | head -n 1) # full path to .png

    # run python gui
    choice=$(python3 "$root_dir/src/main.py")
    choice=$(echo "$choice" | grep -e "choice:" | sed -e 's/\choice://')



    [[ -z "$choice" ]] && exit 0

    file_search=$(echo "$choice" | sed -e 's/\.png//')
    file_search=$(basename "$file_search")
    console_dir=$(basename "$(dirname "$choice")")

    result=$(find "$games_dir$console_dir" -name "*$file_search*")

    [[ -z "$result" ]] && notify-send "Can't find file: $file_search" && exit 1

    if echo "$choice" | grep -q "gamecube"; then
        emulator='org.DolphinEmu.dolphin-emu'

        if ! which "$emulator"; then 
            flatpak install --noninteractive "org.DolphinEmu.dolphin-emu" || (notify-send "Could not install: $emulator" && exit 1)
        fi

        setsid -f flatpak run "$emulator" -e "$result" &
        sleep 2 
        id=$(xdotool search --name "dolphin-emu" | head -n 1)
        xdotool key --window $id "$fullscreen_key"

    elif echo "$choice" | grep -q "play_station_2"; then
        emulator='net.pcsx2.PCSX2'

        if ! which "$emulator"; then 
            flatpak install --noninteractive "$emulator" || (notify-send "Could not install: $emulator" && exit 1)
        fi 

        setsid -f flatpak run "$emulator" -fullscreen "$result" & 

    elif echo "$choice" | grep -q "nintendo_64"; then 

        which m64py > /dev/null || bash "$root_dir/installer/install_m64py.sh install"

        if which m64py; then 
            setsid -f m64py "$result" & 
        else
            notify-send "Not installed: m64py"
        fi

    elif echo "$choice" | grep -q "nintendo_3ds"; then 

        emulator='org.citra_emu.citra'

        if ! which "$emulator"; then 
            flatpak install --noninteractive "$emulator" || (notify-send "Could not install: $emulator" && exit 1)
        fi

        setsid -f flatpak run "$emulator" "$result" & 

    elif echo "$choice" | grep -q "game_boy_advance"; then

        emulator='io.mgba.mGBA'

        if ! which "$emulator"; then 
            flatpak install --noninteractive "$emulator" || (notify-send "Could not install: $emulator" && exit 1)
        fi

        setsid -f flatpak run io.mgba.mGBA -f "$result" &

    elif echo "$choice" | grep -q "nintendo_switch"; then

        emulator='org.yuzu_emu.yuzu'

        if ! which "$emulator"; then 
            flatpak install --noninteractive "$emulator" || (notify-send "Could not install: $emulator" && exit 1)
        fi

        setsid -f flatpak run "$emulator" "$result" &


    fi

}


function main {
    bash "$root_dir/installer/install.sh"
    check_requirements
    download_thumbnails
    game_picker
}

main




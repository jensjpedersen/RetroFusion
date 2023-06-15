#!/bin/bash
# TODO: remove thumbnails for deleted games
export DISPLAY=:0

# Install emulators
#
#
# flatpak install mgba
# flatpak install citra

# hwmodel=$(hostnamectl | awk -F ": " '/Hardware Model:/ {print $2}')
# if [[ $hwmodel == "ThinkCentre M900" ]]; then
#     games_dir="/mnt/hdd/ManjaroSSD/Games/"
# elif [[ $hwmodel == "ThinkPad W530" ]]; then
#     games_dir="/mnt/ssd/Games/"
# fi

root_dir=$(dirname $(realpath $0))

# source conf: games_dir
source "$root_dir/game_menu.conf"
console_dir=( $(ls $games_dir) )


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

            if [ ! -d "thumbnails/$d" ]; then
                mkdir "thumbnails/$d"
            fi

            if [ $d = "gamecube" ]; then

                game_name=$(echo "$file_name" | sed -e 's/\.iso//' -e 's/\.nkit//')
                # img_url="$game_name"".png"
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_GameCube/master/Named_Boxarts/"

            elif [ $d = 'play_station_2' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.iso//')
                # img_url="$game_name"".png"
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Sony_-_PlayStation_2/733507283dd0f52e3b8a47fe0a139be13f82903a/Named_Boxarts/"

            elif [ $d = 'nintendo_64' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.z64//')
                # img_url="$game_name"".png"
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Nintendo_64/c9278f93bfbcb41e4e728b952b25e6cc2ab6830f/Named_Boxarts/"

            elif [ $d = 'nintendo_3ds' ]; then 

                game_name=$(echo "$file_name" | sed -e 's/\.3ds//')
                # img_url="$game_name"".png"
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Nintendo_3DS/15dcea5c55f3ce0bd25a951616a7990a66e25f2d/Named_Boxarts/"

            elif [ $d = 'game_boy_advance' ]; then 
                game_name=$(echo "$file_name" | sed -e 's/\.gba//' -e 's/\s*\# GBA\.GBA//')
                # img_url="$game_name"".png"
                base_url="https://raw.githubusercontent.com/libretro-thumbnails/Nintendo_-_Game_Boy_Advance/e0200a10a81e74a565f335b5ef3d9cb7e8e89672/Named_Boxarts/"

            else
                break 
            fi

            search_game=$(echo "$game_name" | sed -e 's/&/_/' -e 's/(U)//')
            data_file="$root_dir/data/$d/Named_Boxarts.txt" # File with *.png names

            # get line with min char
            match=$(grep -e "$search_game" "$data_file") 
            if [ -n "$match" ]; then 

                # Get line with min char
                img_url=$(echo "$match" | awk '
                length==len {line=line ORS $0}
                NR==1 || length<len {len=length; line=$0}
                END {print line}')

                img_url=$(echo "$img_url" | sed 's/.*->\s*//')


                url="$base_url$img_url"

                # echo "$img_url"


                # TODO:
                # 1. remove "->.*"
                # 2. Find line with min char
                # 3. Check if line has -> 
                # 4. use exp on right side of ->
            else
                echo "Can't find $game_name"
                continue 
            fi

            # if fail download url; try download url2
            img_url2=$(echo "$img_url" | sed -e 's/(.*)//g')
            img_url2=$(echo "$img_url2" | sed -e 's/\.png/(USA)\.png/')
            url2="$base_url$img_url2"

            if [ ! -f "thumbnails/$d/$img_url" ] && [ ! -f "thumbnails/$d/$img_url2" ] ; then 
                # download 1. attempt
                wget -q --directory-prefix "thumbnails/$d" "$url" && continue
                echo "Download failed: $img_url"

                # done 2. attempt
                wget -q --directory-prefix "thumbnails/$d" "$url2" || echo "download failed: $img_url2. No more retries"
            fi


        done


    done

}



function game_picker {

    choice=$(sxiv -t -z 150 -of $root_dir/thumbnails/**/*)
    choice=$(echo "$choice" | head -n 1) 

    [[ -z "$choice" ]] && exit 0


    file_search=$(echo "$choice" | sed -e 's/\.png//')
    file_search=$(basename "$file_search")


    if echo $choice | grep -q "gamecube"; then

        result=$(find "$games_dir/gamecube" -name "*$file_search*")

        if which dolphin-emu; then 
            setsid -f dolphin-emu -e "$result" &
            sleep 2 
            id=$(xdotool search --name "dolphin-emu" | head -n 1)
            xdotool key --window $id 'super+f'
        else 
            notify-send "Not installed: dolphin-emu"
        fi



    elif echo $choice | grep -q "play_station_2"; then
        # Playstation 2
        result=$(find "$games_dir/play_station_2" -name "*$file_search*")
        if which pcsx2-qt; then 
            setsid -f pcsx2-qt -fullscreen "$result" & 
        else
            notify-send "Not installed: pcsx2-qt"
        fi

    elif echo $choice | grep -q "nintendo_64"; then 
        result=$(find "$games_dir/nintendo_64" -name "*$file_search*")

        if which m64py; then 
            setsid -f m64py "$result" & 
        else
            notify-send "Not installed: m64py"
        fi

    elif echo $choice | grep -q "nintendo_3ds"; then 
        result=$(find "$games_dir/nintendo_3ds" -name "*$file_search*")
        if flatpak list | grep -q org.citra_emu.citra; then 
            setsid -f flatpak run org.citra_emu.citra "$result" & 
        else 
            notify-send "Not installed: org.citra_emu.citra_emu"
        fi

    elif echo $choice | grep -q "game_boy_advance"; then
        result=$(find "$games_dir/game_boy_advance" -name "*$file_search*")

        if flatpak list | grep -q io.mgba.mGBA; then 
            setsid -f flatpak run io.mgba.mGBA "$result" &
        else
            notify-send "Not installed: io.mgba.mGBA"
        fi


    fi


}



function main {
    download_thumbnails
    game_picker


}


main




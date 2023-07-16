#!/bin/bash

root_dir=$(dirname "$(realpath "$0")")
install_path="$root_dir/../emulators"
installed_pkg_list="$root_dir/../data/installed_packages.txt"


function fatal {
    echo "FATAL ERROR: $@"
    exit 1
}


function install_font {
    fc-list | grep -q "clacon2.ttf" && return 0
    # which fc-cache || (echo "fc-cache not found, please install it" && return 1)
    wget "http://webdraft.hu/fonts/classic-console/fonts/clacon2.ttf"
    mkdir -p "${HOME}/.local/share/fonts"
    mv clacon2.ttf "${HOME}/.local/share/fonts/"
    fc-cache -f 
}


function check_pkg_manager {
    # Exit program if no supported package manager is found
    supported="dnf apt pacman" # Supported package managers
    for i in $supported; do
        if which $i &>/dev/null ; then
            package_manager=$i
            break
        fi
    done


    if [ -z "$package_manager" ]; then
        echo "No supported package manager found"
        exit 1
    fi
}


function prompt_for_sudo {
    which zenity &>/dev/null || (echo "zenity not found, please install it" && exit 1)

    trap 'sudo -k' EXIT

    zenity --password | sudo -Sv || fatal "Unable to sudo"

}


# Handle general dependencies

function __pacman_base_installer {
    prog_list=("wget" "git" "flatpak" "python" "pip" "xdotool")
    pkg_list=("wget" "git" "flatpak" "python" "python-pip" "xdotool")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo pacman -S --noconfirm $pkg && echo $pkg >> $installed_pkg_list

    done


}

function __dnf_base_installer {
    prog_list=("wget" "git" "flatpak" "python3" "pip" "xdotool")
    pkg_list=("wget" "git" "flatpak" "python3" "python3-pip" "xdotool")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo dnf install -y $pkg && echo $pkg >> $installed_pkg_list

    done
}

function __apt_base_installer {
    pkg_list=("wget" "git" "flatpak" "python3" "python3-pip" "xdotool" "python3-pyqt5")
    prog_list=("wget" "git" "flatpak" "python3" "pip" "xdotool" "null")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo apt install -y $pkg && echo $pkg >> $installed_pkg_list

    done



}

function pip_installer {
    cd "$root_dir/.." || return 1

    [ -f $root_dir/../venv/bin/activate ] || python3 -m venv venv
    source venv/bin/activate

    pip3 list | grep 'PyQt5\s' &>/dev/null || pip3 install --no-input PyQt5

    cd "$root_dir" || return 1
}

function base_installer {
    if which pacman &>/dev/null; then
        __pacman_base_installer
    elif which dnf &>/dev/null; then
        __dnf_base_installer
    elif
        which apt &>/dev/null; then
        __apt_base_installer
    else
        fatal "No supported package manager found"
    fi

    # pip list | grep -q 'PyQt5\s' || pip install --no-input PyQt5

}



function main {
    check_pkg_manager # Check for supported package manager
    prompt_for_sudo # Prompt for sudo password
    base_installer # Install base dependencies
    pip_installer # Install python base dependencies
    install_font 
    flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

}


# main
__pip_installer


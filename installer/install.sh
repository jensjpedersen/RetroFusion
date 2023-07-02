#!/bin/bash

root_dir=$(dirname "$(realpath "$0")")
install_path="$root_dir/../emulators"
installed_pkg_list="$root_dir/../data/installed_packages.txt"


function fatal {
    echo "FATAL ERROR: $@"
    exit 1
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
    prog_list=("wget" "git" "flatpak" "python" "pip" "xdotool")
    pkg_list=("wget" "git" "flatpak" "python3" "python3-pip" "xdotool")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo dnf install -y $pkg && echo $pkg >> $installed_pkg_list

    done
}

function __apt_base_installer {
    prog_list=("wget" "git" "flatpak" "python" "pip" "xdotool")
    pkg_list=("wget" "git" "flatpak" "python3" "python3-pip" "xdotool")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo pacman -S --noconfirm $pkg && echo $pkg >> $installed_pkg_list

    done



}

function base_installer {
    if which pacman &>/dev/null; then
        __pacman_base_installer
    elif which dnf &>/dev/null; then
        __dnf_base_installer
    else
        fatal "No supported package manager found"
    fi

    pip list | grep -q 'PyQt5\s' || pip install --no-input PyQt5

}


function check_if_installed {
    [ -f "$installed_pkg_list" ] && exit 0 || touch $installed_pkg_list
}

function main {
    check_if_installed
    check_pkg_manager # Check for supported package manager
    prompt_for_sudo # Prompt for sudo password
    base_installer # Install base dependencies
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

}


main

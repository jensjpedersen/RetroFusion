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
#
#


function dnf_base_installer() {
    pkg_list=" wget git flatpak python3 python3-pip"

    for i in $pkg_list; do
        which $i &>/dev/null && continue
    done

    echo "Installing wget, git ..."

    # TODO: 
    # * loop pgk_list if not installed -> install and add to pkg_list

}


if which dnf &>/dev/null; then
    dnf_base_installer

    # Add flatpak repo
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

fi
# Create a string variable with spaces over multiple lines




function main {
    check_pkg_manager
    # prompt_for_sudo

}


main

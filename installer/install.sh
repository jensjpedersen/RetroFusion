#!/bin/bash

root_dir=$(dirname "$(realpath "$0")")
install_path="$root_dir/../emulators"



supported="dnf apt pacman" # Supported package managers


# Exit program if no supported package manager is found
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








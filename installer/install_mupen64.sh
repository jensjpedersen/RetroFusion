#!/bin/bash

current_dir=$(dirname "$(realpath "$0")")
install_path="$current_dir/../emulators/mupen64plus-ui-python"
installed_pkg_list="$current_dir/../data/installed_packages.txt"

# * sudo snap 
#
# if which apt-get > /dev/null; then
#     sudo apt-get install -y mupen64plus
# elif which dnf > /dev/null; then
#     sudo dnf install -y mupen64plus # OK 
#     # Install gui
# elif which pacman > /dev/null; then
#     sudo pacman -S --noconfirm mupen64plus
# else
#     echo "Could not find package manager"
#     exit 1
# fi
#
#
#

# function install_m64py {
#     which pip3 > /dev/null || echo "pip3 not found"
# }

# Apt
# sudo apt install libsdl2-dev qttools5-dev-tools pyqt5-dev-tools python3-pyqt5 python3-pyqt5.qtopengl
#
#
#


# Pacman 
#
# Think this is ok. 
#
#
#
#
#

function prompt_for_sudo {
    which zenity &>/dev/null || (echo "zenity not found, please install it" && exit 1)

    trap 'sudo -k' EXIT

    zenity --password | sudo -Sv || (echo "Unable to sudo" && exit 1)

}

function __pacman_install {
    # m64py requirements
    pkg_list=("mupen64plus" "sdl2" "qt5-tools" "python-pyqt5")
    prog_list=("mupen64plus" "sdl2-config" "qt5-tools" "pyuic5")


    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo pacman -S --noconfirm $pkg && echo $pkg >> $installed_pkg_list

    done


    git clone "https://github.com/mupen64plus/mupen64plus-ui-python.git" "$install_path"


    if cd $install_path; then
        # pip3 install -r requirements.txt 
        pip3 install pyqt5 pysdl2
        python setup.py build
        python setup.py install --user
    else
        echo "Could not find mupen64plus-ui-python"
        exit 1
    fi
}


function __dnf_install {
    pkg_list=("SDL2-devel" "qt5-qttools-devel" "PyQt5")
    prog_list=("sdl2-config" "qtplugininfo-qt5" "pyuic5")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo pacman -S --noconfirm $pkg && echo $pkg >> $installed_pkg_list

    done

    git clone "https://github.com/mupen64plus/mupen64plus-ui-python.git" "$install_path"


    if cd $install_path; then
        # pip3 install -r requirements.txt 
        pip3 install pyqt5 pysdl2
        python setup.py build
        python setup.py install --user
    else
        echo "Could not find mupen64plus-ui-python"
        exit 1
    fi



}


function __pacman_uninstall {
    sudo pacman -Rsu --noconfirm mupen64plus

    rm -rf $(which m64py)

    if cd "$install_path"; then
        # pip3 uninstall -r requirements.txt

        pip3 uninstall pyqt5 pysdl2
        cd ..
        rm -rf mupen64plus-ui-python

    else
        echo "Could not find mupen64plus-ui-python"
        exit 1
    fi

    # sudo pacman -R sdl2 qt5-tools python-pyqt5
    # sudo pacman -R mupen64plus-ui-python

}
# Dnf
#
#
# pacman_uninstall


function install {
    which m64py &>/dev/null && exit 0
    prompt_for_sudo
    # __pacman_install
}



function uninstall {
    prompt_for_sudo
    __pacman_uninstall
}



# install

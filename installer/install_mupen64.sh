#!/bin/bash

current_dir=$(dirname "$(realpath "$0")")
install_path="$current_dir/../emulators/mupen64plus-ui-python"
install_core_path="$current_dir/../emulators/mupen64plus-core"
installed_pkg_list="$current_dir/../data/installed_packages.txt"


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


}


function __dnf_install {
    pkg_list=("mupen64plus" "SDL2-devel" "qt5-qttools-devel" "PyQt5")
    prog_list=("mupen64plus" "sdl2-config" "qtplugininfo-qt5" "pyuic5")

    for ((i=0; i<${#prog_list[@]}; i++)); do
        prog=${prog_list[$i]}
        pkg=${pkg_list[$i]}
        which $prog &>/dev/null && continue

        sudo dnf install -y $pkg && echo $pkg >> $installed_pkg_list

    done

}

function __ubuntu_build_core {

    # TODO: fix only check if core is installed. 
    # if [ -d "$install_core_path" ]; then
    #     echo "mupen64plus-core already installed"
    #     return 0
    # fi

    git clone "https://github.com/mupen64plus/mupen64plus-core.git" "$install_core_path"

    if cd "$install_core_path/projects/unix"; then
        make all 
    fi 

}

function __apt_core_install {
    pkg_list=("mupen64plus-audio-all" "mupen64plus-input-all" "mupen64plus-rsp-all" "mupen64plus-video-all")
    for ((i=0; i<${#pkg_list[@]}; i++)); do
        pkg=${pkg_list[$i]}
        dpkg -s "$pkg" &>/dev/null && continue
        sudo apt install -y $pkg && echo $pkg >> $installed_pkg_list
    done



}


function __apt_install {
    # TODO: add build requirements
    # Install mupen64plus core dependencies
    # XXX: removed - use apt install instead
    # pkg_list=("libpng-dev" "libfreetype-dev" "zlib1g" "build-essential" "nasm")     # sdl2-dev
    # prog_list=("libpng-config" "null" "null" "gcc" "nasm")

    # for ((i=0; i<${#prog_list[@]}; i++)); do
    #     prog=${prog_list[$i]}
    #     pkg=${pkg_list[$i]}
    #     which $prog &>/dev/null && continue

    #     sudo apt install -y $pkg && echo $pkg >> $installed_pkg_list

    # done

    # Install m64py dependencies
    pkg_list=("libsdl2-dev" "qttools5-dev-tools" "pyqt5-dev-tools" "python3-pyqt5.qtopengl") # installed in base: "python3-pyqt5" 

    for ((i=0; i<${#pkg_list[@]}; i++)); do
        pkg=${pkg_list[$i]}
        dpkg -s "$pkg" &>/dev/null && continue

        sudo apt install -y $pkg && echo $pkg >> $installed_pkg_list

    done

    # Build mupen64plus-core
    # __ubuntu_build_core || (echo "Unable to build mupen64plus-core" && exit 1)
    __apt_core_install
}




function __python_setup {

    # which m64py &>/dev/null && return 0
    [ -f "${HOME}/.local/bin/m64py" ] && return 0

    git clone "https://github.com/mupen64plus/mupen64plus-ui-python.git" "$install_path"

    if cd $install_path; then
        # pip3 install -r requirements.txt 

        source "${current_dir}/../venv/bin/activate"

        pip3 list | grep 'PySDL2\s' &>/dev/null || pip3 install --no-input PySDL2
        python3 setup.py build
        python3 setup.py install --user

        deactivate

        # Create shortcut 
        # if ! which m64py &>/dev/null; then
        #     # "${HOME}/.local/bin/m64py"
        #     touch "$install_path/m64py"
        #     echo '#!/bin/bash' > "$install_path/m64py"
        #     echo "python3 $install_path/bin/m64py" >> "$install_path/m64py"
        #     ln -s "$install_path/m64py" "${HOME}/.local/bin/m64py"
        # fi 

    else
        echo "Could not find mupen64plus-ui-python"
        exit 1
    fi



}

# TODO: need pyqt5 in base install

function __pacman_uninstall {
    sudo pacman -Rsu --noconfirm mupen64plus

    # rm -rf $(which m64py)
    rm -rf "${HOME}/.local/bin/m64py"

    if cd "$install_path"; then
        # pip3 uninstall -r requirements.txt

        pip3 uninstall --yes pysdl2
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
#

function install_m64py {

    # which m64py &>/dev/null && exit 0
    [ -f "${HOME}/.local/bin/m64py" ] && return 0

    prompt_for_sudo

    if which pacman > /dev/null; then
        __pacman_install
    elif which dnf > /dev/null; then
        __dnf_install
    elif which apt > /dev/null; then
        __apt_install
    else
        echo "Could not find package manager"
        exit 1
    fi

    __python_setup



}

function uninstall_m64py {
    prompt_for_sudo
    __pacman_uninstall
}


# if [ "$1" == "install" ]; then
#     install_m64py
# elif [ "$1" == "uninstall" ]; then
#     uninstall_m64py
# fi
#
#
install_m64py


#!/usr/bin

current_dir=$(dirname "$(realpath "$0")")
tool_path="$current_dir/../tools"

if [ ! -d "$tool_path" ]; then
    mkdir -p "$tool_path"
fi


# Rqeuirements: cmake, make, gcc

if [ ! -f "$tool_path/extract-xiso/build/extract-xiso" ]; then
    echo "Installing: extract-xiso"
    git clone https://github.com/XboxDev/extract-xiso.git "$tool_path/extract-xiso"
    cd "$tool_path/extract-xiso"
    mkdir build
    cd build || (echo "Failed to cd to build" && exit 1)

    [ ! -f "$current_dir/../venv/bin/activate" ] && (echo "No virtualenv found" && return 1)
    source "$current_dir/../venv/bin/activate"
    pip list | grep 'cmake\s' &>/dev/null || pip install --no-input cmake
    cmake ..
    make
    deactivate
fi


# Create xbox cd-rom
# TODO: 
# * stricter check 
# * correct break? 
if ! file "$1" | grep -q "CD-ROM filesystem data"; then
    echo "Extracting: $1"
    "$tool_path/extract-xiso/build/extract-xiso" -x "$1" -d "${1%.iso}" || (echo "Failed to extract iso" && break)
    "$tool_path/extract-xiso/build/extract-xiso" -c "${1%.iso}" "$1" && rm -rf "${1%.iso}"
fi










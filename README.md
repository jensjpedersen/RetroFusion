# Retro Fusion - Game Launcher for Retro Console Games
Retro Fusion is a user-friendly application designed to bring together all your
favorite retro console games in one convenient launcher. It offers easy setup
and installation, making it a breeze to organize and play your beloved classic
games.



## Inspiration Retro Fusion draws its inspiration from RetroArch, a well-known
multi-platform emulator frontend. While building upon this foundation, I
discovered that native emulators provided a superior gaming experience compared
to RetroArch. Native emulators offered smoother gameplay, reduced lag, and an
overall more enjoyable gaming experience.

## Features
* Auto-installation of required dependencies and consoles.
* Display of game thumbnails for a visually appealing interface.
* Intuitive game launcher for easy navigation and launching of games.
* Simple setup and installation process for hassle-free use.

## Requirements Retro Fusion is currently supported on Linux systems such as
Fedora, Ubuntu, Debian, Manjaro, and Arch, which use apt, dnf, or pacman as the
package manager. To use Retro Fusion, ensure that `zenity` is installed on your
machine. If not already installed, you can do on debian systems with the following command:
`sudo apt install zenity` 


## Installation
To install Retro Fusion, clone this repository using the following command:
`git clone "https://github.com/jensjpedersen/RetroFusion.git"` 


## Usage
1. Add your ROM files to the respective directories within the 'roms' directory.
   - Supported consoles include:
     * Game Boy Advance
     * GameCube
     * Nintendo 3DS
     * Nintendo 64
     * PlayStation 2
     * Xbox

   For example, place a Game Boy Advance ROM file in the 'roms/gameboyadvance' directory.

2. Compressed files are automatically decompressed for convenience.

3. Start the application with the following command:
`bash game_menu.sh` 


## Navigation
Navigate through the user interface with the arrow keys or vi keys. Press enter
to launch the selected game.

## Contributing
Contributions to Retro Fusion are welcome! If you find any issues or have
suggestions for improvements, feel free to open an issue or submit a pull
request.

## License
This project is licensed under the MIT License.




# LNK File Editor

LNK File Editor is a simple graphical user interface (GUI) application for editing Windows shortcut (.lnk) files on Linux systems. The application allows you to load a .lnk file, view and modify its target path and command-line arguments, and save the changes.

## Features

- Load .lnk files using a file dialog or by entering the file path manually.
- View and edit the target path of the .lnk file.
- View and edit the command-line arguments of the .lnk file.
- Save the modified .lnk file.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- `pylnk3` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/lnk-file-editor.git
   cd lnk-file-editor
   ```

2. Create a virtual environment and activate it:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the required libraries:
   ```sh
   pip install pylnk3
   ```

## Usage

1. Run the application:
   ```sh
   python gui_ink_editor.py
   ```

2. Use the GUI to load a .lnk file, edit the target path and arguments, and save the changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
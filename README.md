# pgn_splittr

This script splits a large PGN (Portable Game Notation) file into smaller files, each containing a specified number of games. It’s ideal for breaking down large chess databases into manageable chunks for analysis or study.

## Features

- Processes a large PGN file and splits it into multiple smaller PGN files.
- Allows customization of the output folder name and the number of games per file.
- Automatically creates the output directory if it doesn't already exist.
- Handles non-UTF-8 characters in the original PGN file to avoid encoding issues.

## Requirements

- Python 3.x

## Setup

1. Clone or download this repository to your local machine.
2. Place the PGN file you want to split in the `pgn_splitter` directory.

## Usage

1. **Run the script:**

    ```bash
    python pgn_splitter.py
    ```

2. **Provide the following inputs** when prompted:
   - PGN file name (e.g., `Laszlo Polgar Chess 5334 Problems Combinations and Games.pgn`)
   - Output directory name (e.g., `output`)
   - Number of games per file (e.g., `100`)

3. The script will generate multiple PGN files in the specified output directory, each containing the chosen number of games.

## Example Output

After running the script, you’ll find files named `Polgar_5334_Games_Part_1.pgn`, `Polgar_5334_Games_Part_2.pgn`, etc., in the output directory you specified.

## Troubleshooting

- **FileNotFoundError**: Ensure the PGN file path entered is correct and that the file is in the same directory as the script.
- **Encoding Issues**: The script replaces non-UTF-8 characters to avoid errors.

## License

This project is open-source and available for personal and educational use.

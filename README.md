PGN Splitter
This script splits a large PGN (Portable Game Notation) file into smaller files, each containing a specified number of games. It’s ideal for breaking down large chess databases into manageable chunks for analysis or study.

Features
Processes a large PGN file and splits it into multiple smaller PGN files.
Each output file contains a set number of games, configurable within the script.
Handles non-UTF-8 characters in the original PGN file to avoid encoding issues.
Requirements
Python 3.x
Setup
Clone or download this repository to your local machine.

Place the PGN file you want to split in the pgn_splitter directory.

Ensure the output directory exists by running:

bash
Copy code
mkdir output
Usage
Edit the script: Update the file_path variable in pgn_splitter.py to match the name of your PGN file. By default, it expects a file named Laszlo Polgar Chess 5334 Problems Combinations and Games.pgn.

Specify the number of games per file: Modify the games_per_file variable in the script to set how many games each output file should contain. For example:

python
Copy code
games_per_file = 100
Run the script:

bash
Copy code
python pgn_splitter.py
The script will generate multiple PGN files in the output directory, each containing the specified number of games.

Example Output
After running the script, you’ll find files named Polgar_5334_Games_Part_1.pgn, Polgar_5334_Games_Part_2.pgn, etc., in the output directory.

Troubleshooting
FileNotFoundError: Make sure the PGN file path in the script is correct and that the output directory exists.
Encoding Issues: The script replaces non-UTF-8 characters to avoid errors.
License
This project is open-source and available for personal and educational use.

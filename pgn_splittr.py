# Import necessary libraries for file handling and re-encoding
import re

# File path for the original PGN file
file_path = 'Laszlo Polgar Chess 5334 Problems Combinations and Games.pgn'

# Load and read the PGN file, handling non-UTF-8 characters
with open(file_path, 'rb') as file:
    raw_content = file.read()

# Decode the content, replacing non-UTF-8 characters
decoded_content = raw_content.decode("utf-8", errors="replace")

# Split into separate games based on the PGN "[Event " tag
games = decoded_content.split("\n\n[Event ")
games[0] = "[Event " + games[0] if not games[0].startswith("[Event") else games[0]

# Update the number of games per file as requested
games_per_file = 100
output_files = []

# Clean up any non-UTF-8 characters (replacing common encoding errors) and prepare game chunks
cleaned_games = [re.sub("�", "", game) for game in games]

# Process in chunks of 100 games and save each chunk to a new file
for i in range(0, len(cleaned_games), games_per_file):
    chunk = cleaned_games[i:i + games_per_file]
    chunk_text = "\n\n".join(chunk)
    # Define a relative path to output the files in the "output" folder within pgn_splitter
    output_file_path = f"./output/Polgar_5334_Games_Part_{i // games_per_file + 1}.pgn"
    output_files.append(output_file_path)

    # Write the chunk to a new PGN file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(chunk_text)

output_files  # List of generated output files

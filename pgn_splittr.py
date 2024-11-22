import os
import re

# Input: PGN file name, output folder, and games per file.
file_path = input("Enter the PGN file name (e.g., 'your_file.pgn'): ")
output_dir = input("Enter the output directory name (e.g., 'output'): ")
games_per_file = int(input("Enter the number of games per file (e.g., '100'): "))

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created output directory: {output_dir}")
else:
    print(f"Output directory '{output_dir}' already exists. Files will be saved there.")

# Load and read the PGN file, handling non-UTF-8 characters
with open(file_path, 'rb') as file:
    raw_content = file.read()

# Decode the content, replacing non-UTF-8 characters
decoded_content = raw_content.decode("utf-8", errors="replace")

# Split into separate games based on the PGN "[Event " tag
games = decoded_content.split("\n\n[Event ")
games[0] = "[Event " + games[0].lstrip("\"")  # Ensure no leading quote for the first game

# Clean up any non-UTF-8 characters and prepare game chunks
cleaned_games = [re.sub("�", "", game) for game in games]

# Process in chunks and save each chunk to a new file
output_files = []
for i in range(0, len(cleaned_games), games_per_file):
    chunk = cleaned_games[i:i + games_per_file]
    chunk_text = "\n\n".join(chunk)
    output_file_path = os.path.join(output_dir, f"Polgar_5334_Games_Part_{i // games_per_file + 1}.pgn")
    output_files.append(output_file_path)
    
    # Write the chunk to a new PGN file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(chunk_text)

print("Files successfully created:", output_files)

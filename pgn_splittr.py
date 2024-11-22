import os
import re
import unicodedata

# Function to clean non-UTF-8 characters
def clean_text(text):
    # Normalize the text to NFKD form (compatibility decomposition)
    text = unicodedata.normalize('NFKD', text)
    # Replace specific problematic characters
    text = text.replace("�", "")  # Remove any lingering replacement characters
    # Polgar mates specific example
    text = text.replace("L�szl�", "László")  # Correct example replacement
    text = text.replace("K�nemann", "Könemann")  # Correct example replacement
    text = text.replace("Polg�r", "Polgár")  # Correct example replacement
    return text

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
decoded_content = clean_text(decoded_content)  # Apply cleaning

# Split into separate games based on the PGN "[Event " tag
games = decoded_content.split("\n\n[Event ")
games[0] = games[0].strip()  # Strip leading/trailing whitespace

# Fix each game's `[Event` tag
fixed_games = []
for i, game in enumerate(games):
    # Ensure each game starts with a proper `[Event` tag
    if not game.startswith("[Event"):
        game = "[Event " + game.lstrip("#").strip()

    # Remove any redundant `[Event` prefix if present
    game = re.sub(r"^\[Event\s+\[Event\s+", "[Event ", game)

    # Clean the text of each game
    game = clean_text(game)
    fixed_games.append(game)

# Process in chunks and save each chunk to a new file
output_files = []
for i in range(0, len(fixed_games), games_per_file):
    chunk = fixed_games[i:i + games_per_file]
    chunk_text = "\n\n".join(chunk)
    output_file_path = os.path.join(output_dir, f"Polgar_5334_Games_Part_{i // games_per_file + 1}.pgn")
    output_files.append(output_file_path)
    
    # Write the chunk to a new PGN file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(chunk_text)

print("Files successfully created:", output_files)

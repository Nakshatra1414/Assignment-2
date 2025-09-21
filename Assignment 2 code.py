# Program to calculate average BPM from Spotify 2023 dataset
# This version correctly handles commas inside quotes (e.g. "Latto, Jung Kook")
# and ignores unrealistic BPM values.

# Path to your dataset (update if needed)
file_path = "/Users/khush/Downloads/spotify-2023.csv"

def simple_csv_split(line):
    """
    This function splits a line of CSV data into columns
    while respecting quotes ("..."). 
    Example:
    "Song Name","Latto, Jung Kook",125 -> ["Song Name", "Latto, Jung Kook", "125"]
    """
    fields = []           # List to store each column value
    field = ""            # Temporary string to build each field
    inside_quotes = False # Track whether we are inside quotes

    for char in line:
        if char == '"':
            # Flip the flag when we see a quote
            inside_quotes = not inside_quotes
        elif char == "," and not inside_quotes:
            # Comma ends a field only if we are not inside quotes
            fields.append(field)
            field = ""
        else:
            # Add character to current field
            field += char

    # Add the last field at the end of the line
    fields.append(field)
    return fields

total_bpm = 0   # To store the sum of BPM values
count = 0       # To count how many valid BPM values we find

# Open and read all lines from the file
with open(file_path, "r", encoding="latin-1") as file:
    lines = file.readlines()

# Skip the first line (header) and process each song
for line in lines[1:]:
    line = line.strip()  # Remove spaces/newlines
    if line == "":
        continue         # Skip empty lines

    # Use our custom function to split the line
    columns = simple_csv_split(line)

    # Check that we have enough columns before accessing BPM column
    if len(columns) > 14:
        bpm = columns[14].strip()  # BPM is in column 15 (index 14)

        # Check if BPM is a number (integer or decimal)
        if bpm.replace(".", "").isdigit():
            bpm_value = float(bpm)

            # Count only realistic BPM values (e.g. 40 to 250)
            if 40 <= bpm_value <= 250:
                total_bpm += bpm_value
                count += 1

# Calculate average BPM if we found valid rows
if count > 0:
    average_bpm = total_bpm / count
    print("Average BPM of Spotify Songs 2023:", round(average_bpm, 2))
else:
    print("No valid BPM data found.")
# Program to calculate average BPM from Spotify 2023 dataset
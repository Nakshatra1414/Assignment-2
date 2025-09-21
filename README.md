1. What is the purpose of this program(s)?
   The purpose of this program is to calculate the average BPM (Beats Per Minute) of songs from the Most Streamed Spotify Songs 2023 dataset.It helps analyze the overall tempo trend of the most popular songs from that year.

2. What does the program do, include what it takes for input, and what it gives as output?
   Input:
   The program takes a CSV file (dataset) as input.
   The file contains song information such as track name, artist name, release date, playlists, streams, and BPM.

Process:

Reads the file line by line.

Splits each line into separate columns (taking care of commas inside quotes).

Finds the BPM column and extracts the BPM values.

Checks if each BPM is a valid number and within a realistic range (40–250 BPM).

Adds all valid BPM values together and counts them.

Calculates the average BPM by dividing the total by the number of valid songs.

Output:
It prints the average BPM of all valid songs in the dataset, rounded to two decimal places.

3. How do you use the program?
   Make sure you have the dataset file saved on your computer.

Update the file_path in the program so it points to the location of the dataset on your system.

file_path = "/Users/yourname/Downloads/spotify-2023.csv"

Save the program as a .py file (e.g., average_bpm.py).

Open a terminal or VS Code and run:

python average_bpm.py

The program will read the dataset and print the average BPM on the screen.

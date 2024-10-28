import re
import csv

# Open the extracted text file from the PDF
with open("extracted_text.txt", "r") as file:
    text = file.read()

# Regex pattern to match coordinates in the format (latitude, longitude)
pattern = r'\((\-?\d+\.\d+),\s*(\-?\d+\.\d+)\)'

# Find all matches in the text
matches = re.findall(pattern, text)

# Open a CSV file to write the coordinates and timestamps
with open("coordinates.csv", "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Writing header
    csvwriter.writerow(["Timestamp", "Latitude", "Longitude", "Info"])

    # Loop through matches to extract coordinates
    for match in matches:
        latitude, longitude = match
        # Find the timestamp and additional info around each coordinate (optional)
        # Modify this part if you need specific data extracted from each entry
        timestamp_match = re.search(r'Time:\s([\d/]+ [\d:]+)', text)
        info_match = re.search(r'Name:\s([^\n]+)', text)
        
        timestamp = timestamp_match.group(1) if timestamp_match else "N/A"
        info = info_match.group(1) if info_match else "N/A"
        
        # Write each coordinate and additional data to the CSV
        csvwriter.writerow([timestamp, latitude, longitude, info])

print("Extraction complete. Coordinates saved in 'coordinates.csv'.")

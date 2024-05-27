import os
import subprocess
import json
import csv 
dir_path = os.path.dirname(os.path.realpath(__file__))
def get_mp4_files_in_folder():
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # List all files in the current directory
    all_files = os.listdir(current_directory)

    # Filter only the MP4 files
    mp4_files = [file for file in all_files if file.lower().endswith(".mp4")]

    return mp4_files


def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", os.path.join(dir_path,filename)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)
if __name__ == "__main__":
    mp4_files = get_mp4_files_in_folder()  # Replace with your file names
    file = open("videodata.csv","w", newline="")
    file = csv.writer(file)
    file.writerow(["File Name", "Duration"])
    for mp4 in mp4_files:
      duration = round( get_length(mp4)/60)
      file.writerow([mp4,duration])  
    

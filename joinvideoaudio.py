import subprocess
import os

file_names = []

for (path, dir, files) in os.walk('.'):
  for file in files:
    if file.endswith(".mp4"):
      file_names.append(file[:-4])

for file in file_names:
  # for each file we have vid and audio
  vid = file+".mp4"
  aud = file+".m4a"
  subprocess.run(["ffmpeg", "-i", vid, "-i", aud, "-acodec", "copy","-vcodec","copy", "D:/Videos/Appscript 1080 Joined/"+vid])
  print("Done : ",vid)

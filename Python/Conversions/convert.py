#!/usr/bin/env python3
#
# LICENSE : MIT
#
#Copyright © 2023 Dale Weber <dalew@hybotics.io>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the “Software”), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions
# of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# Convert selected audio files to WAV format
#
# Author  : Dale Weber <dalew@hybotics.dev>
# Date    : 26-Aug-2023
# Version : 1.0.0
# Purpose : Convert audio files with selected extensions to WAV format
#
import os
import subprocess

# Initialize
#
# Put the extensions of the files you want to convert here
#
file_extensions = [ "M4A", "MP3" ]
convert_to = "wav"
top_dir = os.getcwd()

check_dirs = os.listdir(".")
dir_list = []
fcount = 0

# Announce
print()
print("Audio file conversions - convert audio files to WAV format")
print()

# Filter out all regular filenames
for d in check_dirs:
  got_dir = os.path.isdir(d)

  if got_dir:
    dir_list.append(d)

#
# Start processing directories
#
for directory in dir_list:
  # Change to the new directory
  current_dir = top_dir + "/" + directory
  print(f"Current directory is {current_dir}")
  os.chdir(current_dir)

  # Get the list of files in this directory
  file_list = os.listdir(".")

  #
  # Main processing loop for each directory
  #
  for fname in file_list:
    # Split the filename into name and extension
    fn, ext = fname.split(".")
    ext = ext.upper()
  
    # Convert a file
    if ext in file_extensions:
      fcount += 1
      print(f"Processing file {fname}")
      command = "ffmpeg -v 0 -i " + fname + " " + fn + "." + convert_to
      print(f"Command = '{command}'")
      subprocess.run(command, shell=True)
      print()

print(f"Finished processing {fcount} files!")

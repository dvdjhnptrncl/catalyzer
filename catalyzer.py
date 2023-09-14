import subprocess
import sys

import re
modes ={}
with open("hash_mode_list.txt", "r") as file:
    for line in file:
        line.replace(" ","")
        mo=line.split("|")[0]
        wo=line.split("|")[1]
        modes[wo]=int(mo)
candidates = []

err=""
for mode in modes.values():
    command = "hashcat -m "+ str(mode) +" -a 0 "+sys.argv[1]+ " oneword.txt";
    try:
        output = subprocess.check_output(command, shell = True,stderr = subprocess.STDOUT, universal_newlines= True)
        print("Command output:")
        print(output)
    except subprocess.CalledProcessError as e:
        err=e

    substring = "255"
    if substring in str(err):
        continue

    else:
        candidates.append(mode)
        search_string= str(mode) +"|" 
        print(search_string)
        with open("hash_mode_list.txt", "r") as file:
    # Iterate through each line in the file
            for line in file:
            # Check if the line starts with the search string
                if line.replace(" ","").startswith(search_string):
                # If it does, print the line
                    print(line)
            


for c in candidates:
    search_string =str(c)+"|"
  



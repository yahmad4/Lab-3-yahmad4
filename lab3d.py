#!/usr/bin/env python3
'''Lab 3 Inv 4 function free_space '''
# Author ID: yahmad4

import subprocess

def free_space():
    # Launch the command and get the output
    command = "df -h | grep '/$' | awk '{print $4}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # Return the output as utf-8 string, stripping any newline characters
    return result.stdout.strip()

if __name__ == '__main__':
    print(free_space())

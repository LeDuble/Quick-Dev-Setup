# Quick-Dev-Setup

Using Python to quickly setup programs, tools, bash files, etc quickly in to a new work environment.

# File handling

The filehandler will iterate through each line of the text file (user desired programs, listed) 
and check whether the program specified on that line is already installed on the system.
If the program is installed, the filehandler will move to the next line in the text file. If not, it will check the program against a curated list of programs (secure measure) and then download it according to the instructions provided. Once the filehandler has reached the end of the text file, the program will stop.

# Bash files (bashaliases, bashrc, etc)

The purpose of this step is to check whether a file, such as "bash_aliases", exists in the system. If the file does exist, then the filehandler will check that it is the correct version.
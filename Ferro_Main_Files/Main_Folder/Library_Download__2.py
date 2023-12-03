#Librarys {Self}

from Other.Code import Vari_And_Func as Var
from Style import Animations

#Librarys {Public}

import subprocess , os , time , pyautogui , sys 

def Close_Program():
    pyautogui.FAILSAFE = False
    screen_width, screen_height = pyautogui.size()
    target_x = screen_width
    target_y = 0
    pyautogui.moveTo(target_x, target_y, duration=0.35)
    time.sleep(0.4)
    pyautogui.click()
    target_x = -500
    target_y = 500
    pyautogui.move(target_x,target_y,duration=0.35)
    time.sleep(0.1)

def play_mp3(file_path):
    subprocess.Popen(['start', '', file_path], shell=True, startupinfo=subprocess.STARTUPINFO(), creationflags=subprocess.CREATE_NO_WINDOW)
def install_or_update_libraries():
    libraries = ["playsound","pyttsx3","pydub","pyaudio"]
    for library in libraries:
        print(f"{Var.Space_Big}{Var.System_Message}Installing or updating {library}...{Var.Space_Big}")
        subprocess.run(f"pip install --upgrade {library}", shell=True)
    print(f"{Var.Space_Big}{Var.System_Message}Installation/update complete.{Var.Space_Big}")
def System_Sound():
    script_path = os.path.abspath(__file__)
    mp3_path = os.path.join(os.path.dirname(script_path),"Other", "Sounds", "System.mp3")
    play_mp3(mp3_path)
    time.sleep(2.5)
    Close_Program()

install_or_update_libraries()
System_Sound()

print(Var.Line_Break)
print("Adjusting")
print(Var.Line_Break)
Animations.loading_animation(total_time=3 , width=100)
print(Var.Line_Break)

Next_File_2 = 'Main_BOT.py'
subprocess.run(['python', Next_File_2])
sys.exit()
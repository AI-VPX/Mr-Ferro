from Style import Banner , Animations
from Other.Code import Vari_And_Func as Var
import time
import subprocess
import sys

Banner.Ferro_Banner()
print("_______ Bye There , Ferro Is Where? ________\n")
print(Var.Line_Break)

def BOT_EXIT_Review():
    EXP = input("""This Bot is Made By Vikrant Pathania, a School Student of 16 years.
He made this using 100% Python, random, and webbrowser libraries.
Please share your experience, and your You can give review\'s screenshort at 
our website or instagram which you can find in my website Thank You.
___________________________________________________________________________________
How Was Your Experience? => """)
    print("\n")
    advice = input("""If there is any mistake in the bot or any advice you want to give,
please let us know.
Your feedback is valuable to us.
___________________________________________________________________________________
Is there any Mistake in Bot or any advice you want to give => """)
    print("\n")
BOT_EXIT_Review()

print(Var.Space_Big*3)

Delete_Librarys = input("Did You Want to Delete All the Librarys Of Python (Y/N) ======>")
print(Var.Space_Big)
if Delete_Librarys == 'Y':
    Animations.loading_animation(total_time=5 , width=100)
    subprocess.run(['python', "Delete_All_Lib.py"])
    sys.exit()
elif Delete_Librarys == 'N':
    print("Closing Bot....")
    print(Var.Space_Big)
    Animations.loading_animation(total_time=3 , width=100)
    print("Exited....")
else:
    time.sleep(0.75)
    print("Closing Bot.... {Due to Wrong Input}")
    print(Var.Space_Big)
    Animations.loading_animation(total_time=3 , width=100)
    print("Exited...")
#Librarys {Self}

from In_And_Out.Input import Text_In 
from Style import Animations
from In_And_Out.Output import Text_Out 
from Links import Website_Links
from Style import Banner 
from Other.Code import Vari_And_Func as Var_Fun
from System import Text_To_Speech 
import Check_Speaker
from In_And_Out.Input import Quary_Text_input
from Links import Quary_Links

#Librarys {Public}

import random 
import subprocess 
import sys
import webbrowser

#Main Variables (+) Ferro Entry

Banner.Ferro_Banner()
print("_______ Hi There , Ferro Here ________\n")

#Main Code {Looping}

while True:

#Input and then set All Text Data In Small Case

    user_input = input(Var_Fun.YOU)
    user_input = user_input.lower().strip()
    user_input = Var_Fun.Remove_Char_Not_Req(user_input)

#Main Text Foam Reply To Text

    if user_input in  Text_In.Hi_Message:
        response = random.choice(Text_Out.Hi_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
    elif user_input in  Text_In.Fine_Message:
        response = random.choice(Text_Out.Fine_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
    elif user_input in  Text_In.Bye_Message:
        response = random.choice(Text_Out.Bye_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
        break
    elif user_input in  Text_In.Thanks_Message:
        response = random.choice(Text_Out.Thanks_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
    elif user_input in  Text_In.Blank_Message:
        response = random.choice(Text_Out.Blank_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
    elif user_input in  Text_In.Owner_Details:
        response = random.choice(Text_Out.Owner_Response)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()

#Links Open

    elif user_input in  Text_In.Open_YT:
        response = "Opening YouTube wait..."
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
        Website_Links.Youtube_Link()
    elif user_input in  Text_In.Chat_Gpt_Link:
        response = "Opening ChatGPT wait..."
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
        Website_Links.Chat_Gpt_Link()
    elif user_input in  Text_In.Open_My_url:
        response = "Opening My Website please wait..."
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
        Website_Links.Owner_Website()
    elif user_input in  Text_In.Open_Source_Code_Link:
        response = "Opening Please Wait..."
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()
        Website_Links.Source_Code_Link()

#Search Links 

    elif user_input in Quary_Text_input.query_YT:
        YT_Search = str(input("Search On Youtube ==> "))
        YT_Search_Go = f"{Quary_Links.yt}{YT_Search}"
        Animations.Animation_Of_UnderScore()
        webbrowser.open(YT_Search_Go)
    elif user_input in Quary_Text_input.query_web:
        Web_Search = str(input("Search On Your Google ==> "))
        Web_Search_Go = f"{Quary_Links.google}{Web_Search}"
        Animations.Animation_Of_UnderScore()
        webbrowser.open(Web_Search_Go)

#Error Message if No Data Found

    else:
        print(Var_Fun.Line_Break)
        print(Var_Fun.System_Message , f"You Typed \"{user_input}\" . Can You Please Check Is There Is Spalling Mistake If No Then Ferro Don\'t Accept This Command Yet If You Want that ferro Accept this Command Then Ask To Developer By Going to WebSite ==>  \"https://shrinkme.info/1roi7zl\" Or You Can tell About This Problem To Developer By Telling On Social Links Like Insta , FB , Discord , Etc all links are ==> \"Comming Soon Prefer To Go to https://shrinkme.info/1roi7zl Until Social Links Dont Come\" . Thank You")
        print(Var_Fun.Line_Break)
        response = random.choice( Text_In.No_Answer_Found)
        print(Var_Fun.BOT , response)
        if Check_Speaker.Speakers_Connected == True:
            Text_To_Speech.speak(response)
        Animations.Animation_Of_UnderScore()

#Exit The Bot

subprocess.run(['python', "Exit.py"])
sys.exit()
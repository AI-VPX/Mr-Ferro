from Style import Banner , Animations
from Other.Code import Vari_And_Func as Var

from pydub import AudioSegment
from pydub.playback import play

print(Var.Line_Break*2)
Banner.Ferro_Sound_Banner()
print(Var.Line_Break*2)

try:
    silent_segment = AudioSegment.silent(duration=100)
    play(silent_segment)
    Speakers_Connected = True
    print(Var.Line_Break)
    print("Checking Speaker ...")
    print(Var.Line_Break)
    Animations.loading_animation(total_time=2 , width=100)
    print(Var.Line_Break)
    print("Speaks are Connected. So There Will be some Sound, If Speakes Are not Connected Then Also its Show Error then Tell This to Head Of Project By going to \"https://shrinkme.info/1roi7zl\"")
    print(Var.Line_Break)
except Exception as e:
    Speakers_Connected = False
    print(Var.Line_Break)
    print("Checking Speaker ...")
    print(Var.Line_Break)
    Animations.loading_animation(total_time=2 , width=100)
    print(Var.Line_Break)
    print("No Speaks Connected. So No Sound, If Speakes Are Connected Then Also its Show Error then Tell This to Head Of Project By going to \"https://shrinkme.info/1roi7zl\"")
    print(Var.Line_Break)
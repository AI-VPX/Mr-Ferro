import sys 
import time

def Animation_Of_Tilt():
    for _ in range(139):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Tilt_Slow():
    for _ in range(139):
        sys.stdout.write("~")
        sys.stdout.flush()
        time.sleep(0.007)
def Animation_Of_UnderScore():
    for _ in range(139):
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_UnderScore_Slow():
    for _ in range(139):
        sys.stdout.write("_")
        sys.stdout.flush()
        time.sleep(0.007)
def Animation_Of_Straight_Line():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Straight_Line_Slow():
    for _ in range(139):
        sys.stdout.write("|")
        sys.stdout.flush()
        time.sleep(0.007)
def Animation_Of_Slash():
    for _ in range(139):
        sys.stdout.write("/")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_Slash_Slow():
    for _ in range(139):
        sys.stdout.write("/")
        sys.stdout.flush()
        time.sleep(0.007)
def Animation_Of_BackSlash():
    for _ in range(139):
        sys.stdout.write("\\")
        sys.stdout.flush()
        time.sleep(0.001)
def Animation_Of_BackSlash_Slow():
    for _ in range(139):
        sys.stdout.write("\\")
        sys.stdout.flush()
        time.sleep(0.007)
def Animation_Ferro_Banner():
    Animation_Of_Straight_Line()
    Animation_Of_Straight_Line()
def Animation_Ferro_Sound_Banner():
    Animation_Of_Straight_Line()
    Animation_Of_BackSlash()
    Animation_Of_Slash()
    Animation_Of_Straight_Line()
def loading_animation(total_time=5, width=50):
    start_time = time.time()
    while time.time() - start_time < total_time:
        elapsed_time = time.time() - start_time
        progress = min(100, int((elapsed_time / total_time) * 100))
        num_equals = int((progress / 100) * width)
        loading_bar = f"|{'=' * num_equals}{' ' * (width - num_equals)}| {progress}%"
        print(loading_bar, end='\r')
        time.sleep(0.1)
    loading_bar = f"|{'~' * width}| 100%"
    print(loading_bar)
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print()
    time.sleep(0.1)
    print("complete!")
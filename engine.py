import glob
import random
import time

from Soundstage import Soundstage
from Speakers import BasicSpeaker, AmbisonicSpeakers, HRTFSpeaker, Track
import numpy as np

sounds = glob.glob("sounds/*.wav")
size = np.array([1000, 1000])
myStage = Soundstage(size)



#h1 = HRTFSpeaker(np.array([-300, 300]), bark)
#h2 = HRTFSpeaker(np.array([300, 300]), metal)
#h3 = HRTFSpeaker(np.array([300, -300]), roar)
#h4 = HRTFSpeaker(np.array([-300, -300]), geese)


for x in range(5):
    size = np.array([1000, 1000])
    sound = random.choice(sounds)
    print("Playing sound", sound)
    s = Track(sound)
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    print(f"locations {x}, {y}")
    myStage = Soundstage(size)
    myStage.set_only([HRTFSpeaker(np.array([x, y]), s)])
    myStage.play(save_name="full_demo.wav")
    time.sleep(4)

#myStage.plot()

myStage.play(save_name="full_demo.wav")

from rotatescreen import *
import time
sc=get_primary_display()
for i in range(21):
    time.sleep(1)
    sc.rotate_to(i*90%360)


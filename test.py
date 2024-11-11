import time
from nava import play, stop
sound_id = play("alarm.wav", async_mode=True)
time.sleep(4)
stop(sound_id)
import wave
from datetime import datetime

import numpy as np
import sounddevice as sd

frames = []
stream = None
is_recording = False

def callback(in_data, frame_count, time_info, status):
    if status:
        print("Status:",status)
    global is_recording, frames
    frames.append(in_data.copy())


#definition

freq = 44100
channels = 1
dtype = "int16"


def record_audio():
    global is_recording, frames, stream
    frames = []
    is_recording = True
    print("Recording started.")
    stream = sd.InputStream(
        samplerate=freq,
        channels=channels,
        dtype=dtype,
        callback=callback,
    )
    stream.start()
    print("Recording... Press Enter to stop.")

def stop_recording():
    global is_recording, frames, stream
    is_recording = False
    stream.stop()
    print("Recording stopped.")
    stream.close()
    print("Recording closed.")
    frames = np.concatenate(frames, axis=0)

    if len(frames) == 0:
        print("No audio data to save.")
        return

    filename = datetime.now().strftime("recording_%Y%m%d_%H%M%S.wav")
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(2)
    wf.setframerate(freq)
    wf.writeframes(frames.tobytes())
    wf.close()
    print(f"Recording saved successfully as {filename}")


record_audio()
input()  # Enter’a basınca kaydı durdurur
stop_recording(),











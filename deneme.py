import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import numpy as np
import threading
# Sampling frequency
freq = 44100

# Initialize recording variables
recording = []
is_recording = False
stop_recording = False

def record_audio():
   global recording, is_recording, stop_recording
   is_recording = True
   while is_recording and not stop_recording:
      recording_segment = sd.rec(int(freq), samplerate=freq, channels=2)
      sd.wait()
      recording.append(recording_segment)

def handle_input():
   global is_recording, stop_recording
   while True:
      user_input = input("r to START , p to PAUSE and s to STOP the recording, please choice accordingly \n Enter command: ").lower()
      if user_input == 'p':
         if is_recording:
            print("Recording Paused, (you can again start the recording using 's') ")
            is_recording = False
         else:
            print("Recording is not working activly.")
      elif user_input == 'r':
         if not is_recording:
            print("Recording Resumed (type 'p' to pause or 's' to stop)")
            threading.Thread(target=record_audio).start()
         else:
            print("Already recording.")
      elif user_input == 's':
         if is_recording:
            print("Stopping recording. Thank you for recording :) ")
            is_recording = False
            stop_recording = True
            break
         else:
            print(" Nothing to stop.")

# Start the input handler in a separate thread
input_thread = threading.Thread(target=handle_input)
input_thread.start()

# Wait for the input thread to complete
input_thread.join()

# Combine all the recorded segments
if recording:
   final_recording = np.concatenate(recording, axis=0)
   write("recording0.wav", freq, final_recording)
   wv.write("recording1.wav", final_recording, freq, sampwidth=2)
   print("Recording saved as 'recording0.wav' and 'recording1.wav'.")
else:
   print("No recording was made.")
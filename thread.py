import pyaudio
import wave
import os
import threading
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5


class MyProcess(threading.Thread):

	def __init__(self, fileNumber):
		threading.Thread.__init__(self)
		self.fileNumber = fileNumber

	def run(self):
		WAVE_OUTPUT_FILENAME = "recording_"
		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
					channels=CHANNELS,
	                rate=RATE,
	                input=True,
	                frames_per_buffer=CHUNK)

		#print(threading.current_thread())
		print("* recording "+str(self.fileNumber))

		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		    data = stream.read(CHUNK)
		    frames.append(data)

		print("* done recording "+str(self.fileNumber))

		stream.stop_stream()
		stream.close()
		p.terminate()
		WAVE_OUTPUT_FILENAME += str(self.fileNumber)+".wav"
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()

		os.system('python3 SpeechRecognitionAudio.py recording_'+str(self.fileNumber)+'.wav')

#th1 = MyProcess(1)
#th2 = MyProcess(2)
#th3 = MyProcess(3)

#th1.start()
#time.sleep(RECORD_SECONDS-1.5)
#th2.start()
#time.sleep(RECORD_SECONDS-1.5)
#th3.start()

#th1.join()
#th2.join()
#th3.join()

NumberOfRecordings = 3
tab = []

for i in range (1, NumberOfRecordings+1):
	tab.append(MyProcess(i))
	tab[i-1].start()
	time.sleep(RECORD_SECONDS-1.5)

for i in range (1, NumberOfRecordings+1):
	tab[i-1].join()
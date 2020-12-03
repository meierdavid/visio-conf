import pyaudio
import wave
import os

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
fileNumber = 1

while fileNumber < 4:
	WAVE_OUTPUT_FILENAME = "recording_"
	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

	print("* recording "+str(fileNumber))

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
	    data = stream.read(CHUNK)
	    frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()
	WAVE_OUTPUT_FILENAME += str(fileNumber)+".wav"
	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()
	fileNumber = fileNumber + 1

commande = 'python3 SpeechRecognitionAudio.py '
for i in range (1, fileNumber):
	commande = commande +'recording_'+str(i)+'.wav '
os.system(commande)
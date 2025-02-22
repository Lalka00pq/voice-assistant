import pyaudio
import wave
import sys


def main():
    py = pyaudio.PyAudio()
    stream = py.open(format=pyaudio.paInt16, channels=1,
                     rate=16000, input=True, frames_per_buffer=8000)
    data = stream.read(num_frames=8000, exception_on_overflow=False)
    return data


if __name__ == "__main__":
    print(main())

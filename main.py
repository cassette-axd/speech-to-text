import speech_recognition
import pyttsx3

# create a recognizer object to understand what is said in mic
recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            # recognize when we start and stop talking
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            # extract text from audio
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue

import json
import speech_recognition
import pyttsx3
import googletrans
from googletrans import Translator

def main():

    # read from or create a json file that contains all possible languages to utilize
    try:
        with open("languages.json", "r") as data_file:
            # read old data
            data = json.load(data_file)
    # create a new json data file if it doesn't currently exist
    except FileNotFoundError:
        with open("languages.json", "w") as data_file:
            json.dump(googletrans.LANGUAGES, data_file, indent=4)

    run = True
    # print(list(data))

    while run:
        desired_language = input("Enter a language to translate to or type 'exit' to quit:\n").lower()
        if desired_language == 'exit':
            run = False
            break
        language_key = ""
        # print(list(data.keys())[list(data.values()).index(desired_language)])
        try:
            # try to get the language key of the desired language (value)
            language_key = list(data.keys())[list(data.values()).index(desired_language)]
            translate_by_voice(language_key, data)
        except Exception:
            print("Invalid language entered")

def translate_by_voice(language_key, data):
    translator = Translator()
    # create a recognizer object to understand what is said in mic
    recognizer = speech_recognition.Recognizer()
    run = True

    while run:
        try:
            with speech_recognition.Microphone() as mic:
                print("Listening")
                # recognize when we start and stop talking
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
 
                # extract text from audio
                text = recognizer.recognize_google(audio)
                text = text.lower()
                if text == 'exit translator' or translator.translate(text, dest=language_key).text == 'exit translator':
                    run = False

                # language_key = translator.detect(text).lang
                print(f"Recognized language: {data[translator.detect(text).lang]}")
                print(f"Recognized text: {text}")
                print(f"Translated text: {translator.translate(text, dest=language_key).text}")

        except speech_recognition.UnknownValueError:
            print("Unreccognized audio received")
            recognizer = speech_recognition.Recognizer()
            translator = Translator()
            continue



# This will be true when were run this file directly only
if __name__ == "__main__":
    main()

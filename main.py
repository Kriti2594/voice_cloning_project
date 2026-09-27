import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Speech settings
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)

    # Generate speech
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    text = input("Enter the text you want to convert into speech: ")

    if text.strip():
        text_to_speech(text)
        print("Speech generated successfully.")
    else:
        print("Please enter some text.")

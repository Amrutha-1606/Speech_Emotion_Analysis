import speech_recognition as sr

# Create recognizer
recognizer = sr.Recognizer()

# Emotion keywords
emotions = {
    "Happy": [
        "happy",
        "excited",
        "great",
        "wonderful",
        "love"
    ],

    "Sad": [
        "sad",
        "unhappy",
        "lonely",
        "cry",
        "upset"
    ],

    "Angry": [
        "angry",
        "furious",
        "hate",
        "mad",
        "annoyed"
    ],

    "Fear": [
        "afraid",
        "scared",
        "worried",
        "fear",
        "nervous"
    ]
}

print("Speech Emotion Analysis")
print("-----------------------")

try:

    # Open audio file
    with sr.AudioFile("speech.wav") as source:

        print("Reading audio file...")

        audio = recognizer.record(source)

    # Convert speech to text
    print("Converting speech to text...")

    text = recognizer.recognize_google(audio)

    print("\nRecognized Speech:")
    print(text)

    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    for symbol in ".,!?;:":
        text = text.replace(symbol, "")

    # Split into words
    words = text.split()

    # Store emotion scores
    scores = {}

    for emotion, keywords in emotions.items():

        score = 0

        for word in words:

            if word in keywords:
                score += 1

        scores[emotion] = score

    # Detect emotion
    if max(scores.values()) == 0:

        detected_emotion = "Unknown"

    else:

        detected_emotion = max(
            scores,
            key=scores.get
        )

    print("\nDetected Emotion:")
    print(detected_emotion)

except FileNotFoundError:

    print("\nError: speech.wav file was not found.")

except sr.UnknownValueError:

    print("\nSorry, the speech could not be understood.")

except sr.RequestError:

    print("\nSpeech recognition service is unavailable.")

except ValueError:

    print("\nPlease use a valid WAV audio file.")
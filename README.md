# Speech Emotion Analysis

## Description

Speech Emotion Analysis is a simple speech processing application that converts recorded speech into text and identifies a basic emotion from the spoken words.

## Emotions Detected

- Happy
- Sad
- Angry
- Fear
- Unknown

## Technology Used

- Python
- SpeechRecognition
- Natural Language Processing
- Speech Processing

## Requirements

- Python 3.x
- WAV audio file
- Internet connection

## Installation

Install SpeechRecognition:

pip install SpeechRecognition

## Project Structure

Speech_Emotion_Analysis/
│
├── app.py
├── speech.wav
└── README.md

## How to Run

1. Open the project folder in VS Code.
2. Add a WAV audio file.
3. Rename the audio file to:

speech.wav

4. Open the VS Code terminal.
5. Install SpeechRecognition:

pip install SpeechRecognition

6. Run:

python app.py

7. The application converts the speech into text.
8. The application displays the detected emotion.

## Example

### Speech

I am very happy and excited today.

### Output

Recognized Speech:
I am very happy and excited today

Detected Emotion:
Happy

## Conclusion

This project demonstrates the basic concepts of speech recognition and emotion analysis using Python.

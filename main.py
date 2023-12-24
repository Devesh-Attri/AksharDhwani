from gtts import gTTS
from pydub import AudioSegment
from googletrans import Translator
import os

def text_to_speech(text, language='en', slow=False):
    tts = gTTS(text=text, lang=language, slow=slow)
    return tts

def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translation = translator.translate(text, src=source_lang, dest=target_lang)
    return translation.text

def generate_audio_from_file(input_file, source_lang='en', target_lang='en', slow=False):
    with open(input_file, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Translate the text if source_lang is different from target_lang
    if source_lang != target_lang:
        text_content = translate_text(text_content, source_lang, target_lang)

    tts = text_to_speech(text_content, target_lang, slow)
    return tts

def play_audio(tts):
    tts.save('temp_audio.mp3')
    os.system('start temp_audio.mp3')

def save_audio(tts, output_file='output.mp3'):
    tts.save(output_file)

def combine_audio_files(audio_files, output_file='output_combined.mp3'):
    combined = AudioSegment.silent(duration=0)
    for file in audio_files:
        audio = AudioSegment.from_mp3(file)
        combined += audio

    combined.export(output_file, format="mp3")

if __name__ == "__main__":
    print()
    print("***---------------------------------------------***")
    print("***---  Welcome to the Audiobook Generator!  ---***")
    print("***---------------------------------------------***")
    print()
    while True:
        # Get input file path from the user
        input_file = input("Enter the path of the .txt file (type 'exit' to quit): ")

        if input_file.lower() == 'exit':
            print("Exiting the Audiobook Generator. Thank you!")
            break

        if not input_file.endswith('.txt'):
            print("Invalid file format. Please provide a .txt file.")
        else:
            # Get input and output languages from the user
            source_lang = input("Enter the language of the input file (e.g., en for English): ")
            target_lang = input("Enter the desired language for the output file (e.g., es for Spanish): ")

            # Generate audio from the input file
            tts = generate_audio_from_file(input_file, source_lang, target_lang)

            # Ask the user if they want to listen to the audio now
            listen_now = input("Do you want to listen to the audio now? (yes/no): ").lower()

            if listen_now == 'yes':
                # Play the audio for the user
                play_audio(tts)

            # Ask the user if they want to save the audio
            save_option = input("Do you want to save the audio? (yes/no): ").lower()

            if save_option == 'yes':
                # Get the desired output file name
                output_file = input("Enter the desired output file name (e.g., output.mp3): ")

                # Save the audio to the specified file
                save_audio(tts, output_file)
                print(f"Audio saved to {output_file}")

            else:
                print("Audio not saved.")
            print()  # Add a new line for better readability in the console

    print("***------------------------------------------------------***")
    print("***---  Thank you for using the Audiobook Generator!  ---***")
    print("***------------------------------------------------------***")
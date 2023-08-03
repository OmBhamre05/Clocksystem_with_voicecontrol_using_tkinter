import time
import tkinter as tk
import speech_recognition as sr
import pyttsx3

root = tk.Tk()
root.title("Voice Controlled Timer")
root.geometry("600x600")
root.configure(bg="white")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen_to_voice_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command + "\n")

    except sr.UnknownValueError:
        print("Your last command couldn't be heard")
        command = listen_to_voice_command()

    return command

def set_timer(duration):
    speak("Timer has been set for " + str(duration) + " seconds")
    time.sleep(duration)
    speak("Time is up")

def set_countdown(duration):
    for i in range(duration, 0, -1):
        speak(str(i) + " seconds remaining")
        time.sleep(1)
    speak("Countdown completed")

def set_sleep_cycle(duration):
    for i in range(duration):
        speak("You have " + str(duration - i) + " cycles left")
        set_timer(60)
    speak("Sleep cycle completed")

def listen_to_voice_command_btn():
    command = listen_to_voice_command()

    if "timer" in command:
        try:
            timer_duration = int(command.split("for")[1])
            set_timer(timer_duration)
        except:
            speak("Invalid input, please try again")

    elif "countdown" in command:
        try:
            countdown_duration = int(command.split("for")[1])
            set_countdown(countdown_duration)
        except:
            speak("Invalid input, please try again")

    elif "sleep cycle" in command:
        try:
            sleep_cycle_duration = int(command.split("for")[1])
            set_sleep_cycle(sleep_cycle_duration)
        except:
            speak("Invalid input, please try again")

listen_btn = tk.Button(root, text="Listen to Voice Command", font="Helvetica 20 bold",command=listen_to_voice_command_btn).pack(pady=270)
 
#listen_btn.pack()

root.mainloop()

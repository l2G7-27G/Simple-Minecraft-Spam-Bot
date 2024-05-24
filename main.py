# Import all necessary modules
import pygame
import time
from datetime import datetime
from rich import print
import json5 as json
import threading
import random
import os
# Yes, it’s not very optimized, but it works :)
import keyboard
from pynput.keyboard import Controller
import pyautogui

# Constants
PROGRAM_VERSION: str = "v1.0.0-release"

# Main variables
settings: dict = {} 
bot_is_toggle: bool = False

messages_history: list = []

keyboard_controller = Controller()

# I'm too lazy to write further comments

def log(text="", level=0, type=0):
    if level <= settings["loggingLevel"]:
        types = {
            0:"[DEBUG] ",
            1:"[yellow][WARNING][/yellow] ",
            2:"[red][ERROR][/red] "
        }
        if settings["showTimeWhenLogging"]:
            print(f"[{datetime.now().strftime("%H:%M:%S")}] " + str(types[type]) + text)
        else:
            print(str(types[type]) + text)

def on_key_press():
    global bot_is_toggle
    pygame.mixer.init()
    bot_is_toggle = not bot_is_toggle
    if bot_is_toggle:
        log(f"[green]Bot is enabled.[/green]", 1)
        pygame.mixer.music.load("./resources/sounds/bot_on.ogg")
    else:
        log(f"[red]Bot is disabled.[/red]", 1)
        pygame.mixer.music.load("./resources/sounds/bot_off.ogg")
    pygame.mixer.music.play()
    
def generate_message():
    message = settings["spamMessageSettings"]["spamMessagePrefix"] + random.choice(settings["spamMessageSettings"]["spamMessages"]) + settings["spamMessageSettings"]["spamMessageSuffix"]
    return message
    
def spam():
    global bot_is_toggle
    while True:
        if bot_is_toggle:
            log(f"messages_history: {messages_history}", 3)
            
            message = generate_message()
            while message in messages_history:
                message = generate_message()
                
            if len(messages_history) >= settings["spamMessageSettings"]["spamMessagesHistorySize"]:
                messages_history.pop(0)
                
            messages_history.append(message)
            
            log(f"Sending \"{message}\" to chat...", 1)
            if settings["spamMessageSettings"]["enableSpamMessageSound"]:
                pygame.mixer.init()
                pygame.mixer.music.load("./resources/sounds/spam_message.ogg")
                pygame.mixer.music.play()
            pyautogui.press(settings["minecraftClientSettings"]["openChatKey"])
            keyboard_controller.type(message)
            pyautogui.press("enter")
            time.sleep(random.uniform(float(settings["botSettings"]["minSpamMessageDelay"]), float(settings["botSettings"]["maxSpamMessageDelay"])))
            log(f"messages_history: {messages_history}", 3)

def main():
    global settings
    
    with open('./settings.json', 'r', encoding='utf-8') as file:
        settings = json.load(file)
    if settings["spamMessageSettings"]["spamMessagesHistorySize"] == "auto":
        settings["spamMessageSettings"]["spamMessagesHistorySize"] = round((len(settings["spamMessageSettings"]["spamMessages"])/100)*80)
    
    print(f"Simple Minecraft Spam Bot\nVersion: {PROGRAM_VERSION}, Author: l2G7\nGitHub: [link https://github.com/l2G7-27G/Simple-Minecraft-Spam-Bot]https://github.com/l2G7-27G/Simple-Minecraft-Spam-Bot[/link https://github.com/l2G7-27G/Simple-Minecraft-Spam-Bot]")

    keyboard.add_hotkey(settings["botSettings"]["botToggleKey"], on_key_press)

    spam()
    #thread = threading.Thread(target=spam)
    #thread.start()
    #thread.join()
    
if __name__ == '__main__':
    main()
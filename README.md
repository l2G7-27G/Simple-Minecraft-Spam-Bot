# Simple Minecraft Spam Bot

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

> [!IMPORTANT]
> <b>I beg you not to use this program for malicious purposes</b>. It was <ins>created to have a laugh</ins> at the expense of foolish spammers on Minecraft’s donation servers, who, upon being added to your Discord friends list, start sending links to Discord servers that actually pay these spammers.<br>This program is designed for spamming in the style of: <i>“Femboy desires passionate love —> _[Spammer’s Nickname]_”</i>
## Futures
- [ ] Graphical interface
- [ ] GUI overlay
- [ ] Using the Minecraft API instead of just pasting text into the chat.
- [ ] Make an icon
> While nothing from this list has been done yet, I will definitely improve and make progress.

## How to use
To use this bot, you first need to launch it. Let me explain how to do it! Okay, I'm just kidding. When you press a button <i>(by default, it's the `=` key)</i> to toggle the bot, the bot turns on/off and a note block sound is emitted depending on whether it has been turned on or off. You can also enable a setting so that a note block sound is played when a message is sent. This is enabled by default and can be turned off in the settings. The delay before the next message is randomly within a certain range, which can be adjusted in the settings.
> [!WARNING]
> I want to warn you in advance: if the program locks up <i>(and I’m not making any promises)</i>, and you can’t turn off the bot, remember that `Ctrl+C` probably won’t work. Before launching the program, you should make sure that you can turn it off in case of a bug, because I want to remind you again that I’m not making any promises.

![damit](https://github.com/l2G7-27G/Simple-Minecraft-Spam-Bot/assets/159056065/42b91b35-703d-4e2f-ad26-2ae48d5f8bfe)

## Settings
Just go to `settings.json` and read the C-like comments there <i>(fortunately, `json5` supports them)</i>. And actually, it’s already late and I want to go to bed as soon as possible.

## How it works
This program works very simply, let me explain. There is a `while True` loop that constantly checks if the user has turned on the bot and if they have, it selects a random message from the list of all messages. If it is not in the message history, it sends it by simply pressing `t` to open the chat and entering the text with a subsequent press of `Enter`.

Also, check out this masterpiece of optimization:
```python
1.  # Import all necessary modules
2.  import pygame
3.  import time
4.  from datetime import datetime
5.  from rich import print
6.  import json5 as json
7.  import threading
8.  import random
9.  import os
10. # Yes, it’s not very optimized, but it works :)
11. import keyboard
12. from pynput.keyboard import Controller
13. import pyautogui
```
I personally don't see any problems with optimization)

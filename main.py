import pygame
import requests
from io import BytesIO
import tkinter as tk
import pyperclip

pygame.init()
pygame.mixer.init()

def play_sound():
    global sound
    url = url_entry.get()
    response = requests.get(url)
    sound = pygame.mixer.Sound(BytesIO(response.content))
    sound.play()

def stop_sound():
    pygame.mixer.stop()

def paste_url():
    url_entry.insert(0, pyperclip.paste())

def clear_url():
    url_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Проигрыватель звука")

url_frame = tk.Frame(root)
url_frame.pack()

url_label = tk.Label(url_frame, text="URL звука:")
url_label.pack(side=tk.LEFT)

url_entry = tk.Entry(url_frame, width=40)
url_entry.pack(side=tk.LEFT)

paste_button = tk.Button(url_frame, text="Вставить", command=paste_url)
paste_button.pack(side=tk.LEFT)

clear_button = tk.Button(url_frame, text="Очистить", command=clear_url)
clear_button.pack(side=tk.LEFT)

control_frame = tk.Frame(root)
control_frame.pack()

play_button = tk.Button(control_frame, text="Play", command=play_sound)
play_button.pack(side=tk.LEFT)

stop_button = tk.Button(control_frame, text="Stop", command=stop_sound)
stop_button.pack(side=tk.LEFT)

root.mainloop()
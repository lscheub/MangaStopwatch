import time
from datetime import datetime
import keyboard
import os
import tkinter as tk
from tkinter import ttk
import json
scriptPath = os.path.dirname(__file__)

#Folders containing reading Mats
folders = [os.path.join(scriptPath, "ExampleFolder"),
           os.path.join(scriptPath, "ExampleFolder2")]

#Folders/Files inside the reading Mats folders that should not appear in the dropdown menu
ignoreFolders = ["ignore",
                 "ExampleFile 2"]

#Keybinds for Pausing, Continuing and Ending the stopwatch
continueKeybind = "ctrl+shift+p"
pauseKeybind = "ctrl+shift+r"
exitKeybind = "ctrl+shift+x"


timeDataPath = os.path.join(scriptPath, "Stopwatch.json")  #Time tracking json file
mostRecentPath = os.path.join(scriptPath, "lastRead.txt")  #File containing the default selected reading material

def pause_stopwatch():
    text_widget.insert(tk.END, "Pause detected!\n")
    root.iconbitmap(os.path.join(scriptPath, "pause.ico"))
    global paused, tmpStopTime
    if(not paused):
        tmpStopTime = time.time()
    paused = True

def continue_stopwatch():
    text_widget.insert(tk.END, "Continue detected!\n")
    root.iconbitmap(os.path.join(scriptPath, "play.ico"))
    global paused, tmpStopTime, stoppedTime
    if(paused):
        tmpStopTime = time.time() - tmpStopTime
        stoppedTime += tmpStopTime
        paused = False

def stop_stopwatch():
    text_widget.insert(tk.END, "Stop detected!\n")
    global start_time, stoppedTime, mostRecentPath, timeData, lastRead, paused, tmpStopTime
    if(paused):
        tmpStopTime = time.time() - tmpStopTime
        stoppedTime += tmpStopTime
    end_time = time.time()
    elapsed_time = (end_time - start_time) - stoppedTime
    now = datetime.now().strftime("%Y-%m-%d")
    if (lastRead in timeData):
        if(now in timeData[lastRead]):
            timeData[lastRead][now] += elapsed_time
        else:
            timeData[lastRead][now] = elapsed_time
        totalTime = 0
        for day in timeData[lastRead]:
            print(f"{day}\n")
            if(day != "total"):
                totalTime += timeData[lastRead][day]
        timeData[lastRead]["total"] = totalTime
    else:
        timeData[lastRead] = {}
        timeData[lastRead][now] = elapsed_time
        timeData[lastRead]["total"] = elapsed_time
    with open(timeDataPath, 'w', encoding='utf-8') as json_file:
        json.dump(timeData, json_file, ensure_ascii=False, indent=4)
    with open(mostRecentPath, "w", encoding='utf-8') as f:
        f.write(lastRead)
    os._exit(0)

#What happens when the dropdown menu is used
def handle_selection(event):
    global combo, lastRead, result_label
    selected_value = combo.get()
    text_widget.insert(tk.END, f"You selected: {selected_value}\n")
    lastRead = selected_value
    result_label.config(text=f"Selected: {selected_value}")

#Read the default selected manga
with open(mostRecentPath, "r", encoding='utf-8') as f:
    lastRead = f.read().strip()

#Read Reading Material names from Folders
options = []
for folder in folders:
    options += os.listdir(folder)

print(folders)
#Ignore some folders
for folder in ignoreFolders:
    print(folder)
    print(folder in folders)
    if folder in options: options.remove(folder)

#Tkinter GUI for selection of what reading material the stopwatch should be for
root = tk.Tk()
root.title("Stopwatch")
root.iconbitmap(os.path.join(scriptPath, "play.ico"))
label = tk.Label(root, text="Choose the item you want to track the time for:")
label.pack(pady=10)
combo = ttk.Combobox(root, values=options, width=50)
combo.pack(pady=10)
if (lastRead != ""):
    combo.set(lastRead)
combo.bind("<<ComboboxSelected>>", handle_selection)
result_label = tk.Label(root, text=f"Selected: {lastRead}")
result_label.pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack(pady=20)
button1 = tk.Button(button_frame, text="Continue", command=continue_stopwatch)
button2 = tk.Button(button_frame, text="Pause", command=pause_stopwatch)
button3 = tk.Button(button_frame, text="Exit", command=stop_stopwatch)
button1.pack(side=tk.LEFT, padx=5)
button2.pack(side=tk.LEFT, padx=10)
button3.pack(side=tk.LEFT, padx=15)
text_widget = tk.Text(root, height=15, width=50)
text_widget.pack(pady=40)

#Reading the time file
with open(timeDataPath, 'r', encoding='utf-8') as json_file:
    timeData = json.load(json_file)

#Misc variables
paused = False
tmpStopTime = 0
stoppedTime = 0
start_time = time.time()

#Keyboard shortcuts
keyboard.add_hotkey(continueKeybind, pause_stopwatch)
keyboard.add_hotkey(pauseKeybind, continue_stopwatch)
keyboard.add_hotkey(exitKeybind, stop_stopwatch)
text_widget.insert(tk.END, f"Press {continueKeybind} to resume\n")
text_widget.insert(tk.END, f"Press {pauseKeybind} to pause\n")
text_widget.insert(tk.END, f"Press {exitKeybind} to exit\n")
text_widget.insert(tk.END, f"Currently Selected: {lastRead}\n")
pause_stopwatch()
root.mainloop()

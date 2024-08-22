# ReadingStopwatch
A time tracker for tracking time you spend immersing in whatever

When editing the Stopwatch.py file, you can edit the folders and ignoreFolders variables to point to the folder(s) where you store your epubs or folders containing jpegs with your manga or whatever. Just create a File named after whatever you want to track at the location where you set the folders variable. You can also have multiple folders. The ignore folders should point to some items (or leave it empty) that are in the "folders" that you want to ignore / dont want to have to see in the dropdown menu everytime.

Assuming an example foder with the following files:

![ExampleFolder](https://github.com/user-attachments/assets/5d20c0d9-2515-422f-b96e-42b264ccecc8)

When running the scipt you will have a gui with a dropdown menu looking like this (this is with the dropdown menu open):

![Example](https://github.com/user-attachments/assets/7c5924d2-1d40-4bad-ba04-37ac00859f4c)

The icon in the top left indicates that the time is running. You can change and use the keybinds defined in the script to start, pause or end the stopwatch or you can use the buttons. The keybinds also work when the stopwatch is not in focus. The Textbox at the bottom serves as a log. You dont have to immeadiately choos the item you want to track the time for, you only have to choose one before ending the stopwatch (always use the end keybind or the end button, do not just close it). After ending the stopwatch for the first time, it will save the selected item to track and automatically select it on the next startup. The tracked times can be found in the Stopwatch.json.

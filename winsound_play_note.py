import msvcrt
import time
import winsound

notes = {'a': 440, 's': 935, 'd': 1039}

while True:
    key = msvcrt.getch()
    key = key.decode('utf-8')
    print(key)
    if key == 'q': break
    note = notes.get(key, 300)
    winsound.Beep(note, 100)
    time.sleep(0.01)
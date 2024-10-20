from sys import stdout as out
from time import sleep
from itertools import cycle

# def cycle(iterable):
#     saved = []
#     for element in iterable:
#         yield element
#         saved.append(element)
#     while 1:
#         for element in saved: yield element
     
out.write("\033[?25l\033[0;36m")
out.write("\u25AC"*52)
out.write("\033[52D\033[8B" + '\u25AC'*52 + "\033[52D\033[7A")

# Comment out sleep function for full speed animation
for progress in cycle(list(range(0,51)) + list(range(50, -1, -1))):
    out.write('\u258C' + "\u2588"*progress + " "*(50-progress) + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*(50-progress) + " "*progress + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*progress + " "*(50-progress) + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*(50-progress) + " "*progress + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*progress + " "*(50-progress) + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*(50-progress) + " "*progress + '\u2590\033[1B\033[102D')
    # sleep(0.005)
    out.write('\u258C' + "\u2588"*progress + " "*(50-progress) + '\u2590\033[6A\033[102D')
    # sleep(0.005)
out.write("\033[7B")
out.write('\033[102C\033[?25h\033[0;0m')

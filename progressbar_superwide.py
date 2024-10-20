from itertools import cycle
from time import sleep
from sys import stdout as out

total_width = 50
bgcolor = 36
progress = list(range(total_width + 1)) + list(range(total_width-1,0,-1))
out.write(f"\033[?25l\033[0;{bgcolor}m" + "\u25AC"*(total_width + 2) + f"\033[6B\033[{total_width + 2}D" + "\u25AC"*(total_width + 2) +f"\033[5A\033[{total_width + 2}D")
# print("\u2580 \u2581 \u2582 \u2583 \u2584 \u2585 \u2586 \u2587 \u2588 \u2589 \u258A \u258B \u258C \u258D \u258E \u258F \u2590 \u2591 \u2592 \u2593 \u2594 \u2595 \u2596 \u2597 \u2598 \u2599 \u259A \u259B \u259C \u259D \u259E \u259F")
for i in cycle(progress):
    out.write(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B")
    out.write(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B")
    out.write(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B")
    out.write(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B")
    out.write(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[4A")
    sleep(0.2)
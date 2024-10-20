from itertools import cycle
from time import sleep

total_width = 50
bgcolor = 36
progress = list(range(total_width + 1)) + list(range(total_width-1,0,-1))
colors = cycle([31,32,33,34,35,36,37])

print(f"\033[?25l" + "\u25AC"*(total_width + 2) + f"\033[6B\033[{total_width + 2}D" + "\u25AC"*(total_width + 2) +f"\033[5A\033[{total_width + 2}D",end="")
# print("\u2580 \u2581 \u2582 \u2583 \u2584 \u2585 \u2586 \u2587 \u2588 \u2589 \u258A \u258B \u258C \u258D \u258E \u258F \u2590 \u2591 \u2592 \u2593 \u2594 \u2595 \u2596 \u2597 \u2598 \u2599 \u259A \u259B \u259C \u259D \u259E \u259F")
for i in cycle(progress):
    print(f"\033[0;{next(colors)}m", end="")
    print(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B", end="")
    print(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B", end="")
    print(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B", end="")
    print(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[1B", end="")
    print(f"\033[{total_width + 2}D\u258C" + i*"\u2588" + (total_width-i)*" " + "\u2590\033[4A", end="")
    sleep(0.2)
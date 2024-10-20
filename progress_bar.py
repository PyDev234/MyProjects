# Program to Make a custom Progress Bar using unicode code points
from time import sleep as time_freeze

"""
block: str = "\u2588"
left_bar: str = "\u258C"
right_bar: str = "\u2590"
"""

def show_progress(start: int = 0, end: int = 100, size: int = 100, delay = 0.1) -> int:
    # Initial Variables and setting of terminal
    block: str = "\u2588"                                               # unicode character for block char
    print(end="\x1b[?25l")                                              # making cursor invisible
    progress_bar: format = "\u258C{0}{1}\u2590 {2:<.1f}%  \r"           # a template progress bar
    size: int = [size, 128][size>128]                                   # setting size if too big to display for pretty printing
    ratio: int = size/(end-start)                                       # Ratio to calculate no. of blocks on each iteration

    for progress in range(start, end+1):
        n_blocks: int = round((progress-start)*ratio)
        cur_progress: str = progress_bar.format(block*n_blocks, " "*(size-n_blocks), ((progress-start)*100)/(end - start), progress)
        print(end=cur_progress)
        time_freeze(delay)

    print(end="\x1b[?25h\n")                                            # making cursor visible again
    return progress==end                                                # return True if successfully executed else False

def main() -> None:
    show_progress(start = 0, end = 100, size = 100, delay = 0.1)

if __name__ == '__main__':
    main()
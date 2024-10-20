# Program to Implement a custom colored progress bar.

# full_block_char = "\u2588"
# left_half_block = "\u258C"
# right_half_block = "\u2590"
# Escape character = '\033' or '\x1b' or '\e' or decimal(27)

def cycle(it = []):
    i: list = []
    for item in it:
        i.append(item)
        yield item
    while True:
        for item in i:
            yield item

def show_progress(start = 0, end = 100, length = 100, n = 4, delay = 0.1) -> bool:
    # creating delay using time.sleep()
    from time import sleep as time_freeze
    from sys import stdout as out

    # Unicode points used 
    full_block_char: str = "\u2588"
    left_half_block: str = "\u258C"
    right_half_block: str = "\u2590"
    bold_minus: str = "\u25AC"
    reset_colors: str = "\033[0m"
    make_cursor_invisible: str = "\033[?25l"
    make_cursor_visible: str = "\033[?25h"
    fg_color = "\033[34m"

    # make cursor invisible
    out.write("\033[?25l")

    # initial settings
    out.write(fg_color)
    progress_to_blocks_ratio: float = length/(end-start)
    progress_bar_template: str = left_half_block + "{m_blocks}{m_spaces}" + right_half_block + " {percent:4.2f}%  \r"
    
    out.write("\u25AC"*(length+2) + "\n")
    out.write(f"{'\n'*n}{'\u25AC'*(length+2)}\033[{n}A\r")
    try:
        for progress in range(start, end+1):
            n_blocks: int = int((progress-start)*progress_to_blocks_ratio)
            progress_bar: str = progress_bar_template.format(m_blocks=n_blocks*full_block_char, m_spaces=(length-n_blocks)*" ", percent=((progress-start)*100)/(end-start))
            progress_bar = "\n".join([progress_bar for i in range(n)])
            out.write(progress_bar + f"\033[{n-1}A")
            out.flush()
            time_freeze(delay)
    except KeyboardInterrupt: pass

    # make cursor visible, move cursor to next line and reset colors
    out.write(f"\033[{n-1}B\n{"\u25AC"*(length+2)}\033[?25h\033[0m\n")
    return progress == length

if __name__ == '__main__':
    show_progress(length = 100,delay = 0.1)
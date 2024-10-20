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

def show_progress(start = 0, end = 100, length = 100, delay = 0.1) -> bool:
    # creating delay using time.sleep()
    from time import sleep as time_freeze
    from sys import stdout as out

    # Unicode points used 
    full_block_char: str = "\u2588"
    left_half_block: str = "\u258C"
    right_half_block: str = "\u2590"
    reset_colors: str = "\033[0m"
    make_cursor_invisible: str = "\033[?25l"
    make_cursor_visible: str = "\033[?25h"

    # make cursor invisible
    out.write("\033[?25l")

    # dictionary of foreground colors available
    foreground_colors: dict = {
        "Black": "\033[30m",
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Yellow": "\033[33m",
        "Blue": "\033[34m",
        "Magenta": "\033[35m",
        "Cyan": "\033[36m",
        "White": "\033[37m",
        "Default": "\033[39m",
        "Bright Black": "\033[90m",
        "Bright Red": "\033[91m",
        "Bright Green": "\033[92m",
        "Bright Yellow": "\033[93m",
        "Bright Blue": "\033[94m",
        "Bright Magenta": "\033[95m",
        "Bright Cyan": "\033[96m",
        "Bright White": "\033[97m",
    }
    # dictionary of background color
    background_colors: dict = {
        "Black": "\033[40m",
        "Red": "\033[41m",
        "Green": "\033[42m",
        "Yellow": "\033[43m",
        "Blue": "\033[44m",
        "Magenta": "\033[45m",
        "Cyan": "\033[46m",
        "White": "\033[47m",
        "Default": "\033[49m",
        "Bright Black": "\033[100m",
        "Bright Red": "\033[101m",
        "Bright Green": "\033[102m",
        "Bright Yellow": "\033[103m",
        "Bright Blue": "\033[104m",
        "Bright Magenta": "\033[105m",
        "Bright Cyan": "\033[106m",
        "Bright White": "\033[107m",
    }

    # initial settings
    fg_colors = cycle(foreground_colors.values())
    progress_to_blocks_ratio: float = length/(end-start)
    progress_bar_template: str = "{fg_color}" + left_half_block + "{m_blocks}{m_spaces}" + right_half_block + " {percent:4.2f}%  \033[0m\r"
    
    try:
        for progress in range(start, end+1):
            n_blocks: int = int((progress-start)*progress_to_blocks_ratio)
            progress_bar: str = progress_bar_template.format(fg_color=next(fg_colors), m_blocks=n_blocks*full_block_char, m_spaces=(length-n_blocks)*" ", percent=((progress-start)*100)/(end-start))
            out.write(progress_bar)
            out.flush()
            time_freeze(delay)
    except KeyboardInterrupt: pass

    # make cursor visible, move cursor to next line and reset colors
    out.write("\033[?25h\033[0m\n")
    return progress == length

if __name__ == '__main__':
    show_progress(length = 128,delay = 0.5)
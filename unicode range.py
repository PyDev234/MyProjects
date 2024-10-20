ranges = list()

# Just some example ranges ... 
# Plane 0 0000–ffff - Basic Multilingual Plane
ranges.append((0x0000, 0x001f, 'ASCII (Controls)'))
ranges.append((0x0020, 0x007f, 'ASCII'))
ranges.append((0x0100, 0x017f, 'Latin Extended-A'))
ranges.append((0x0180, 0x024f, 'Latin Extended-B'))
ranges.append((0x0250, 0x02af, 'IPA Extensions'))
ranges.append((0x0370, 0x03FF, 'Greek'))
ranges.append((0x4e00, 0x9fff, 'CJK Unified Ideographs')) 

# Plane 1 10000–1ffff - Supplementary Multilingual Plane
ranges.append((0x1f600, 0x1f64f, 'Emoticons'))
ranges.append((0x17000, 0x187ff, 'Tangut'))

for r in ranges:
    # print the header of each range
    print(f'{r[0]:x} - {r[1]:x} {r[2]}')
    j = 1
    for i in range(r[0], r[1]):
        if j % 80 == 0:
            print('')
        j += 1

        print(f'{str(chr(i))}', end='')
    print('\n')

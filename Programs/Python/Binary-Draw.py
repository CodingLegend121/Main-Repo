'''
So type either big or small then type

any of those numbers below

 |||||||||
 vvvvvvvvv


Examples For SMALL:

28822701900309504 - Creeper

9132670736085834306 - Alien Thing

218159447022786696 - Sword

4342219536296657468 - Smilee

4358035222334894652 - YinYang

4530074108892699 - Cursor

6184594508112997290 - Some Design Thing

18689653276278594 - Vampire Thing

Examples For BIG:


415729513483166676842633084859664810398398278051522258159600122677038128 - Frog

3590288666966718226236305765009541498633253174806281670841875286404004054352 - Skull










'''


from termcolor import colored


def binList(size, binary):
    binary = bin(int(binary))
    if binary[0] == '-':
        binary = binary.lstrip('-0b')
    else:
        binary = binary.lstrip('0b')
    binlist = []
    for char in binary:
        binlist += char
    binlist = list(map(int, binlist))
    if size == 'small':
        moreZero = 64 - len(binlist)
        add0 = 0
        while add0 < moreZero:
            binlist.insert(0, 0)
            add0 = add0 + 1
        for n, i in enumerate(binlist):
            if i == 0:
                binlist[n] = colored('0 ', 'white', 'on_white', attrs=['bold'])
        for n, i in enumerate(binlist):
            if i == 1:
                binlist[n] = colored('1 ', 'red', 'on_red')
        print(''.join(map(str, binlist[:8])))
        print(''.join(map(str, binlist[8:16])))
        print(''.join(map(str, binlist[16:24])))
        print(''.join(map(str, binlist[24:32])))
        print(''.join(map(str, binlist[32:40])))
        print(''.join(map(str, binlist[40:48])))
        print(''.join(map(str, binlist[48:56])))
        print(''.join(map(str, binlist[56:64])))
    if size == 'big':
        moreZero = 256 - len(binlist)
        add0 = 0
        while add0 < moreZero:
            binlist.insert(0, 0)
            add0 = add0 + 1
        for n, i in enumerate(binlist):
            if i == 0:
                binlist[n] = colored('0 ', 'white', 'on_white', attrs=['bold'])
        for n, i in enumerate(binlist):
            if i == 1:
                binlist[n] = colored('1 ', 'green', 'on_green')
        print(''.join(map(str, binlist[:16])))
        print(''.join(map(str, binlist[16:32])))
        print(''.join(map(str, binlist[32:48])))
        print(''.join(map(str, binlist[48:64])))
        print(''.join(map(str, binlist[64:80])))
        print(''.join(map(str, binlist[80:96])))
        print(''.join(map(str, binlist[96:112])))
        print(''.join(map(str, binlist[112:128])))
        print(''.join(map(str, binlist[128:144])))
        print(''.join(map(str, binlist[144:160])))
        print(''.join(map(str, binlist[160:176])))
        print(''.join(map(str, binlist[176:192])))
        print(''.join(map(str, binlist[192:208])))
        print(''.join(map(str, binlist[208:224])))
        print(''.join(map(str, binlist[224:240])))
        print(''.join(map(str, binlist[240:256])))


BinSize = input(colored('\n\n\n\nSmall [8x8]\n', 'green', attrs=[
                'bold']) + colored('Big [16x16]\n', 'red', attrs=['bold']))
if (BinSize in ['Big', 'big', 'B', 'b', 'BIG', '16x16', '16']):
    x = input('Number :')
    print('\n\n\n\n')
    binList('big', int(x))
    print('\n\n\n\n')
if (BinSize in ['Small', 'small', 'S', 's', 'SMALL', '8x8', '8']):
    x = input('Number :')
    print('\n\n\n\n')
    binList('small', int(x))
    print('\n\n\n\n')

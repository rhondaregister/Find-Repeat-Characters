def findRepeatCharacters(string):
    d = {}
    for c in string:
        if c in d:
            return 'The first repeating letter is "{}"'.format(c)
            break
        else:
            cl = set(k.lower() for k in d)
            d[c] = c
            print('"{}" is not a repeat character.'.format(c))
            if c.lower() in cl:
                print('...FYI, capital letters are considered unique characters around here.')
            continue
    return('No repeat characters found!')
    

print(findRepeatCharacters("Umlaut"))
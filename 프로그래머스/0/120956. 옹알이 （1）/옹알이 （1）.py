def solution(babbling):
    valid_sounds = ['aya', 'ye', 'woo', 'ma']
    sum1 = 0
    
    for word in babbling:
        for sound in valid_sounds:
            word = word.replace(sound, ' ', 1)
        if not any(sound in word for sound in valid_sounds) and word.strip() == '':
            sum1 += 1

    return sum1

def solution(babbling):
    valid_sounds = ['aya', 'ye', 'woo', 'ma']
    count = 0
    
    for word in babbling:
        for sound in valid_sounds:
            word = word.replace(sound, ' ', 1)
        if not any(sound in word for sound in valid_sounds) and word.strip() == '':
            count += 1

    return count

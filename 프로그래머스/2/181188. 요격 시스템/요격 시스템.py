def solution(targets):
    answer = 1
    targets.sort(reverse=True)
    start=targets[0][0]
    for s,e in targets:
        if e<=start:
            answer+=1
            start=s

    return answer
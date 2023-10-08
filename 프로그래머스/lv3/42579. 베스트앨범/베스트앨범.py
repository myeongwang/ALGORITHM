"""
def solution(genres, plays):
    
    genres_dic={}
    
    for genre in genres:
        if genre not in genres_dic:
            genres_dic[genre]=1
        else:
            genres_dic[genre]+=1
            
    plays_dic={}
    """
def solution(genres, plays):
    genres_dic = {}  # 각 장르별로 총 재생 횟수를 기록하는 딕셔너리
    plays_dic = {}   # 각 장르별로 (고유 번호, 재생 횟수)를 리스트로 기록하는 딕셔너리

    # genres와 plays 배열을 동시에 순회하면서 정보를 기록
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        print(genre,play)
        # genres_dic 업데이트
        if genre not in genres_dic:
            genres_dic[genre] = play
        else:
            genres_dic[genre] += play

        # plays_dic 업데이트
        if genre not in plays_dic:
            plays_dic[genre] = [(i, play)]
        else:
            plays_dic[genre].append((i, play))

    # genres_dic을 재생 횟수 내림차순으로 정렬
    sorted_genres = sorted(genres_dic.keys(), key=lambda x: genres_dic[x], reverse=True)
    print(sorted_genres)
    answer = []

    # 재생 횟수가 많은 장르부터 순회
    for genre in sorted_genres:
        # 해당 장르의 노래들을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬
        sorted_songs = sorted(plays_dic[genre], key=lambda x: (-x[1], x[0]))

        # 최대 2개까지 노래 선택
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])

    return answer

    
  

"""sdfaadf
"""
                   
        
        
   

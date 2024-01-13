# 프로그래머스 lv1 추억 점수

def solution(name, yearning, photo):
    answer = []
    
    # 사진들을 순서대로 조회하며 추억점수 계산
    for people in photo:
        # 각 사진의 추억점수를 저장할 temp변수
        temp = 0
        for person in people:
            # 해당하는 사람이 name에 있을 경우에만 실행
            if person in name:
                # 해당 사람의 인덱스를 찾아서, 해당 인덱스의 yearning점수를 더해줌
                idx = name.index(person)
                temp += yearning[idx]
        
        # 각 사진의 추억점수 총합을 answer에 추가해줌
        answer.append(temp)
    
    return answer
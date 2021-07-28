#Programmers #실패율
'''
실패율 = 스테이지도달 클리어못한 플레이어수 / 스테이지도달 플레이어수
전체스테이지: N
현재 멈춰있는 스테이지 번호 배열 : stages
return 실패율이 높은 스테이지부터 스테이지 번호 내림차순
stages 안에 수는 현재 스테이지 /// N+1은 클리어한사용자
실패율이 같은 스테이지는 작은번호스테이지가 먼저 오게
스테이지 도달 유저가 없으면 실패율은 0
'''
#MY Solution

#for문으로 단계의 사람의 수
#리스트에 튜플형태로 {단계의 사람수/전체사람수, 전체사람수}
#전체사람수-단계사람수 =>이전단계에서의 사람수를 제외
def solution(N, stages):
    user = len(stages)
    result=[]
    ans=[]
    for i in range(1,N+1):
        people = stages.count(i) #i단계에서 멈춘사람
        if people == 0:
            result.append((0,i))
            continue
        fail = people / user
        result.append((fail,i))
        user -= people
    result.sort(key= lambda x: (-x[0],x[1]))
    for i in range(N):
        a,b=result[i]
        ans.append(b)
    return ans
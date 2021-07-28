#Programmers #완주하지 못한 선수
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(completion)]
#MY Solution
#Other Solution
'''
import Collections

def solution(participant, completion):
	answer=collection.Counter(participant) - collections.Counter(completion)
	return list(answer.keys())[0]
'''
#해쉬함수
'''
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
'''
'''
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c:
            return p

    return participant[-1]

'''
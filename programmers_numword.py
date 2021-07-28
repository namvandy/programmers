#Programmers #숫자 문자열과 영단어
#MY Solution
def solution(s):
    
    word={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    answer=0
    i=0
    buf = ''
    result=''
    while i<len(s):
        if s[i].isalpha():
            buf += s[i]
        else:
            result += s[i]
        if buf in word:
            result += str(word[buf])
            buf = ''
        i+=1
        
    
    return int(result)
solution('one4seveneight')

#Other Solution
'''
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
'''
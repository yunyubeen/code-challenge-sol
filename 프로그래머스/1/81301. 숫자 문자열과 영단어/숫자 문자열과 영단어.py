def solution(s):
    english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for i, v in enumerate(english) :
        s = s.replace(english[i], num[i])
    return int(s)
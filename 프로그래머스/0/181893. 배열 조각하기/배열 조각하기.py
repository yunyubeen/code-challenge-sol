def solution(arr, query):
    result = []
    for i in range(len(query)):
        if i%2==0:
            arr = arr[:query[i] + 1]
        else :
            arr = arr[query[i]:]
    return arr


# 짝수 홀수 나누기
# 짝수 홀수 중에서 query 값으로 슬라이싱
# 결과는 슬라이싱 후 남은 배열 리턴

# 처음 시간 걸린 이유: 배열은 0부터 시작, 실수로 query[i] + 1, query[i]를 반대로 써버림..
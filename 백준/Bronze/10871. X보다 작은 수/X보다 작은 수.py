N, X =map(int, input().split())
A = list(map(int, input().split()))

result = [str(element) for element in A if element < X]
print(" ".join(result))

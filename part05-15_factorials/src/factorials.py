# Write your solution here
def factorials(n:int):
    result ={}
    if n>=1:
        result[1] = 1
    if n>=2:
        for i in range(2, n+1):
            result[i] = i* result[i-1]
    return result

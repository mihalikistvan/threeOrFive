def solution(number):
    if number <= 0:
        return 0
    returnValue = 0
    for i in range (0,number):
        if i % 3 == 0 or i % 5 == 0:
            returnValue = returnValue +i
    return returnValue
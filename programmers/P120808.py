def solution(denum1, num1, denum2, num2):
    # 통분하여 분수의 덧셈 구하기
    denum3 = denum1 * num2 + denum2 * num1
    num3 = num1 * num2
    
    # 더한 값을 기약분수로 나타내기
    if denum3 < num3:
        n = denum3
    else:
        n = num3
    
    for i in range(1, n+1):
        if (denum3%i)==(num3%i)==0:
            gcd = i
        
    result_numerator = denum3 // gcd
    result_denominator = num3 // gcd
    
    answer = []
    answer.append(result_numerator)
    answer.append(result_denominator)
    
    return answer
    
if __name__ == "__main__":
    result = solution(9, 2, 1, 3)
    print(result)
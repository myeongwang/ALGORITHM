def solution(inputPriceArr):
        global Price
        answer = 0
        for i in range(InputLen):
            if Price // inputPriceArr[i] > 0:
                answer += (Price // inputPriceArr[i])
                Price -= inputPriceArr[i] * (Price // inputPriceArr[i])
                
        return answer        
        
InputLen, Price= map(int, input().split())
inputPriceArr = []
for i in range(InputLen):
    inputPriceArr.append(int(input()))
 
inputPriceArr.sort(reverse=True)
print(solution(inputPriceArr))
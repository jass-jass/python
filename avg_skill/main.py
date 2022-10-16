import math

def main():
    N = int(input());
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))
    skill = [B[0]]
    count = [0]
    countries = [A[0]]
    
    for i in range(len(A)):
        for j in range(len(countries)):
            if A[i] == countries[j]:
                count[j] += 1
                skill[j] += B[i]
                break
            elif j >= len(countries):
                countries.append(A[i])
                count.append(1)
                skill.append(B[i])
    
    for i in range(len(skill)):
        skill[i] = math.floor(skill[i]/count[i])
    
    for i in range(len(B)):
        for j in range(len(countries)):
            if A[i] == countries[j]:
                B[i] = B[i] - skill[j]
                break
        print(B[i], end = " ")
                
main()

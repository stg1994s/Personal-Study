# for 문을 사용해서 1부터 10까지 자연수 중 홀수의 합을 구할 수 있도록 코딩해 보자.

i = 0
sum = 0

for i in range(1, 11, 2):
    sum=sum+i
    print("1에서 10까지 자연수 중 홀수의 합은 %d %sum")
    
# for n in range(10)
    #print(n, end=" ") # 그런식으로 나열되는 것을 확인할 수 있습니다.
    #i = 5

    #스트링을 했으니까 다른 표현을 써본다면?

for n in range(2, 8, 2): #1,3,5,7,9 이렇게 나옴 #2 4 6 짝수가 나열되는 것을 볼 수 있다. 어렵지 않지?
    print(n, end=" ")


print("\n"--------------------------------------------------------)
                                                                   # 이거 뭔지 아시죠? 역슬러시 한번 쓴거에요!

# 참고로 C/C++/JAVA에서
# 일반적인 for loop(반복문)
# for (int i=0; i<-10; i__ {
# .....
#}
# 뭐 다른 프로그램에선 이런식으로 정리를해!

# Java : forEach
# tnt arr[] = {1,2,3,4,5};
# for (int a : arr) {
# system.out.printin(); //배열의 개별 요소를 갔다가 인쇄하는 것.
#}

# 자바는 Var를 쓰는데 방식은 세미클론 (;) 과 비슷하다. 하여튼 재밌는게 많다.

# 열거형(enumeration)/시퀀스형(sequence)형 객체
# 나중엔 튜플이란게 있는데 앞으로 가니까 뒤로 바뀌죠.
# str = "python" # 문자열
#str = ('p', 'y', 't', 'h', 'o', 'n') # 튜플(tuple)
str = {'p', 'y', 't', 'h','o', 'n'} # 집합/set
#yhtnpo : 순서(index) 성분이 없음,
#print(Len(str))

# 리스트(list) 참고), javascript 배열 정의/초기화 동일
# print(len(str))
for s in str:
    print(s, end=" ")




str = "python" #파이썬이란 문자열이 있다고 가정하면 나열해보자
# print(len(str))
for s in str:
    print(s, end=" ") #이렇게 프린트를 런 돌리면, 보이는 것처럼 p y t h o n, 이렇게 글자간 공백이 띄워져서 나온다.\

for i in range(len(str)+1) :
    print(i)

print("\n....................")
for i in range(len(str)):
        print(str[i], end=" ")

for i in range(len(str)-1, -1, -1): # 역순(reverse) 이란 뜻
    print(i, end=" ") # 순서(index) : 0 ~ 길이-1
    # print(str[i] end=" ")

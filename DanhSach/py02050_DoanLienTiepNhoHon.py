t = int(input())
while t>0:
    t -= 1
    n = int(input())
    a = list(int(x) for x in input().split())
    st = list()
    for i in range(len(a)):
        while len(st) > 0 and a[i]>= a[st[-1]]:
            st.pop()
        if len(st) == 0:
            print(i+1, end = " ")
        else:
            print(i - st[-1], end= " ")
        st.append(i)
    print()
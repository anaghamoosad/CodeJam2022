def punchCard(R,C):
    for i in range(0, (2 * R) + 1):
        punchcard_list = ''
        for j in range(0, (2 * C) + 1):
            if i in {0, 1} and j in {0, 1}:
                punchcard_list+='.'
            else:
                if i % 2 == 0:
                    if j % 2 == 0:
                        punchcard_list +='+'
                    else:
                        punchcard_list +='-'
                else:
                    if j % 2 == 0:
                        punchcard_list +='|'
                    else:
                        punchcard_list +='.'
        print(punchcard_list)
    return ()

T = int(input())
for i in range(T):
    N = input().split()
    R = int(N[0])
    C = int(N[1])
    print("Case #{}:".format(i+1 ))
    punchCard(R,C)
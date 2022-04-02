def threeD_Printing():
    P1 = input().split()
    P2 = input().split()
    P3 = input().split()

    C = [int(P1[0]), int(P2[0]), int(P3[0])]
    M = [int(P1[1]), int(P2[1]), int(P3[1])]
    Y = [int(P1[2]), int(P2[2]), int(P3[2])]
    K = [int(P1[3]), int(P2[3]), int(P3[3])]

    total_units=1000000
    min_color_val=[]
    A=min(C)
    B = min(M)
    D = min(Y)
    N = min(K)

    min_color_val.append(min(C))
    min_color_val.append(min(M))
    min_color_val.append(min(Y))
    min_color_val.append(min(K))

    total_min_amount = sum(min_color_val)

    if total_min_amount == 1000000:
        final_color_amount = ' '.join(str(i) for i in min_color_val)
        return final_color_amount

    elif total_min_amount<0:
        return ("IMPOSSIBLE")

    else:
        result=[0,0,0,0]
        a=0
        flag=0
        for i in range(len(min_color_val)):
            a=a+min_color_val[i]
            if a >=total_units:
                flag=i
                break
        for j in range(flag+1):
            if j==flag:
                s=a-min_color_val[flag]
                result[j]=abs(total_units-s)
                break
            else:
                result[j]=min_color_val[j]

        if sum(result)==total_units:
            final_color_amount = ' '.join(str(i) for i in result)
            return final_color_amount
        else:
            return ("IMPOSSIBLE")



T = int(input())
for i in range(T):
    print("Case #{}: {}".format(i+1,threeD_Printing() ))


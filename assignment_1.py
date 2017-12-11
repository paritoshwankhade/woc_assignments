N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2): 
    print(str('-')*int((M-(3*i))/2)+str('.|.')*int(i)+str('-')*int((M-(3*i))/2))
print(str('-')*int((M-7)/2)+"WELCOME"+str('-')*int((M-7)/2))
for i in range(N-2,-1,-2): 
    print(str('-')*int((M-(3*i))/2)+str('.|.')*int(i)+str('-')*int((M-(3*i))/2)) #Enter Code Here

Problem-2:
tl;dr: Given a string of digits S, insert a minimum number of opening and closing parentheses into it such that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly between them. An opening parenthesis and a closing parenthesis that is further to its right are said to match if their nesting is empty, or if every parenthesis in their nesting matches with another parenthesis in their nesting. The nesting depth of a position p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))), ((2))((2))(1). The first three strings have minimum length among those that have the same digits in the same order, but the last one does not since ((22)1) also has the digits 221 and is shorter.

Solution:
THE CODE IS IN PYHTON3

T=int(input())
for k in range(0,T):
   
    string=input()
    final=''
    m=[]
    temp=0
    for i in range(len(string)):
        m.append(int(string[i]))
    for i in range(m[0]):
        final=final+'('
        temp+=1
    final=final+str(m[0])
    for j in range(1,len(m)):
        if(m[j]-m[j-1]>0):
            for i in range(m[j]-m[j-1]):
                final=final+'('
                temp+=1
            final=final+str(m[j])
        if(m[j]-m[j-1]<0):
            for i in range(m[j-1]-m[j]):
                final=final+')'
                temp-=1
            final=final+str(m[j])
        if(m[j]-m[j-1]==0):
               final=final+str(m[j])

    for i in range(temp):
        final+=')'
    print("Case #",(k+1),': ',final,sep='')
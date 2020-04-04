Problem-1:
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal (which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are the integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

Solution:
THE CODE IN PYTHON3


T=int(input())
for t in range(0,T):
            N=int(input())
            number=0
            number1=0
            su=0
            arr = [] 
            #print("Enter the entries rowwise:") 
            for i in range(N): # A for loop for row entries 
                a =[] 
                for j in range(N):      # A for loop for column entries 
                    b=(int(input())) 
                    while b not in range(1,N+1):
                        b=(int(input()))
                    a.append(b)
                arr.append(a)
            #print(arr)
            for i in range (0,N):
                su+=arr[i][i]
            diagonal_sum=su
            #print(diagonal_sum)
            r=[]
            c=[]
            for i in range(N):
                count=0
                for j in range(N):
                    for k in range(j+1,N):
                        if(arr[i][j]==arr[i][k]):
                            count=count+1
                            #print(count)
                r.append(count)
            #print(r)
            
            for j in range(N):
                count=0
                for i in range(N):
                    for k in range(i+1,N):
                        if(arr[i][j]==arr[k][j]):
                            count=count+1
                c.append(count)
            #print(c)
            for i in range(0,len(r)):
                if(r[i]==0):
                    number=number+r[i]
                else:
                    number=number+1
            for j in range(0,len(c)):
                if(c[j]==0):
                    number1=number1+c[j]
                else:
                    number1=number1+1
            print("Case #" + str(t+1) +" "+ str(diagonal_sum)+ " "+str(number) + " "+str(number1))
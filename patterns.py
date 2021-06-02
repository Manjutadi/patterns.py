* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

num=int(input())
for i in range(num):
    for j in range(num):
        print(j+1,end=" ")
    print()
     

2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
6 7 8 9 10 

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i+j,end=" ")
    print()

1 2 3 4 5 
5 4 3 2 1 
1 2 3 4 5 
5 4 3 2 1 
1 2 3 4 5 
n=int(input())
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        for j in range(n,0,-1):
            print(j,end=" ")
    print()


1 1 1 1 1 
1 2 3 4 5 
3 3 3 3 3 
1 2 3 4 5 
5 5 5 5 5 
n=int(input())
for i in range(n):
    if i%2==0:
        for j in range(1,n+1):
            print(i+1,end=" ")
    else:
        for j in range(1,n+1):
            print(j,end=" ")
    print()

1 2 3 4 5 
2 2 3 4 5 
3 2 3 4 5 
4 2 3 4 5 
5 2 3 4 5 
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()
   
                       

5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 

n=int(input())
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()
    
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1  
n=int(input())
for i in range(n):
    for j in range(n):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            if j%2==0:
                
                print("1",end=" ")
            else:
                print("0",end=" ")
        else:
            if j%2==0:
                print("0",end=" ")
            else:
                print("1",end=" ")
    print()


1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 
0 1 0 1 0 
1 0 1 0 1 

n=int(input())
for i in range(1,n+1):
    if i%2:
        temp=1
    else:
        temp=0
    for j in range(1,n+1):
        print(temp,end=" ")
        if temp==0:
            temp=1
        else:
            temp=0
    print()



n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
n=int(input())
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

*****
 ****
  ***
   **
    *
n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    
    1
   22
  333
 4444
55555
n=int(input())
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end="")
    print()


    1
   222
  33333
 4444444
555555555
n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()

    1
   123
  12345
 1234567
123456789
n=int(input())
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(1,2*i):
        print(k,end="")
    print()

    1
   10
  101
 1010
10101
n=int(input())
temp=1
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
       
        if k%2!=0:
            temp=1
        else:
            temp=0
        print(temp,end="")
    print()
    

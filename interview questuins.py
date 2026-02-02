'''n=int(input("enter the number"))
if n>0:
    print("positive number")
elif n==0:
    print("zero")
else:
    print("negatuve number")'''



#whether the number is even or odd

'''n=int(input("eneter the number"))
if n%2==0:
    print("even")
else:
    print("odd")    '''


#whwtwer the number is leap year or not

''''n=int(input("enter the year:"))
def checkyear(n):
    return(((n%4==0) and (n%100!=0)) or (n%400==0))
if (checkyear(n)):
    print("leap")
else:
    print("not leap year")    '''


#whwter the given the is larger

'''n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
if (n1>=n2) and (n1>=n3):
    print("n1 larger")
elif (n2>=n1) and (n2>=n3):
    print("n2 larger")
else:
    print("n3 larger")        '''



# python program to compete permutations of string
 
 
''''def vamshi(string,i=0):
    if i==len(string):
        print(" ".join(string))
    for j in range(i,len(string)):
        words=[c for c in string]
        words[i],words[j]=words[j],words[i]
        vamshi(words,i+1) 
vamshi("mur")'''





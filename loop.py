print("hello")
def hello():
    print("helllo")
def prime():
    num=int(input("enter number for prime"))
    for x in range(2,num):
        if num%x==0:
            print(num,"is not prime")
            break
        else:
            print(num, "is a prime")
            break
for x in range(5):
    if x<2 :
        print(x)
    elif x>2 :
        hello()
prime()

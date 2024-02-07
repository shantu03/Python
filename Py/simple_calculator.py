def show(a,b,c):
    d=0
    if(c=="+"): 
       d=a+b
    elif(c=="-"):
        d=a-b
    elif(c=="*"):
        d=a*b
    elif(c=="/"):
        d=a/b
    elif(c=="//"):
        d=a//b
    elif(c=="%"):
        d=a%b
    else :
        print("enter valid operation ")
        return None
    
    return d

while True:
    try:
      a=int(input("Enter first num "))
      b=int(input("Enter Second num "))
    except ValueError:
        print("Invalid numbers \n\n")
        continue
    while True:
        c=input("Enter operation ")
        d=show(a,b,c)
        if(d!=None): break
    
    print(d)
    again=input("Calculate again : yes/no  ")
    print("\n\n\n\n")
    if(again=="no") :break

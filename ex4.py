def outer(a,b):
    def inner():
        S=a+b
        return S    
    s=inner()+5
    print(s)





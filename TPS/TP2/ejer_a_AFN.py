# (ab, acb)*

print("Insert below the string: ")
string = str(input())

def q0(s):
    if not s: 
        print("accept") #Acepta el estado.
    if s[0] == "a": 
        return q1(s[1:])
    else:
        print("reject")

def q1(s):
    if not s:
        print("reject")
    #AFN debe probar los dos extremos.
    if (s[0] == "b" and q0(s[1:]) == "accept" or
        s[0] == "b" and q2(s[1:]) == "accept"):
        print("accept")
    else:
        print("reject")

def q2(s):
    if not s: 
        print("reject")
    if s[0] == "c": 
        return q0(s[1:])
    else:
        print("reject")

q0(string)

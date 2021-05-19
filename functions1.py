print("Below you can find the number. Press the number for your language")
print("1 = English")
print("2 = Italian")
s=input("Enter the input")

a=int(s)
#language(a)
def language(s):
    if s==1:
        print("Hello")
    elif s==2:
        print("Hola")
    elif s>=3:
        print("Select from the given options")
    else :
        print("fuck off")

language(a)

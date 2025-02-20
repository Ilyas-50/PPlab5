from re import * 
txt = "Hello world I Like Man"
x = split(r"(?=[A-Z])", txt)


if(x):
    print("Success")
else:
    print("Fail")
print(x)


from re import * 
txt = "Ppp WorlD world Hello"
x = findall(r"[A-Z][a-z]+", txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


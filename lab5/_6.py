from re import * 
txt = "hello world, man."
x = sub(r"[\s.,]", ':', txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


from re import * 
txt = "a_b hello_world Hello_world hello_World"
x = findall(r"[a-z]+_[a-z]+", txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


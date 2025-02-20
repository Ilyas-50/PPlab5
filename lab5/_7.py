from re import * 
txt = "hello_world kakeshli_kokko"

x = sub(r'_([a-z])', lambda m: m.group(1).upper(), txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


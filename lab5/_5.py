from re import * 
txt = "ajjjbn abb mmmbba ands ahdb"
x = findall(r"a.*?b", txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


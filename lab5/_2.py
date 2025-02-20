from re import * 
txt = "abbbc, abb, abbb, baaab"
x = findall(r"ab{3,4}", txt)
if(x):
    print("Success")
else:
    print("Fail")
print(x)


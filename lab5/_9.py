import re

text = "helloWorldJoy"
result = re.sub(r'(?=[A-Z])', ' ', text)
print(result)

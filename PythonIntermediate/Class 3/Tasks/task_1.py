import re

text = "test43543lfdsfdsfl534543fdgl432fr"
numbers = re.findall(r'\d+', text)

for number in numbers:
    print(number)

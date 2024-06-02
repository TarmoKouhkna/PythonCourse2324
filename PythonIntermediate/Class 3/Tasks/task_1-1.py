import re

text = "test43543lfdsfdsfl534543fdgl432fr"
text_without_numbers = re.sub(r'\d+', '', text)

print(text_without_numbers)

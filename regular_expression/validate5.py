import re

email = input("What's your email?").strip()

if re.search(".+@.+", email):
    print("vaild")
else:
    print("Invalid")
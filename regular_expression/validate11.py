import re

email = input("What's your email?").strip()

if re.search(r"^\w+@\w.+\.(com|edu|org|net)$", email):
    print("Valid")
else:
    print("Invalid")
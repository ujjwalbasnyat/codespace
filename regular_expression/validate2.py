email = input("What's your email?").strip()
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
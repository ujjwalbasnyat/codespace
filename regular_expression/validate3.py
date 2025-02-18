email = input("What's your email?").strip()

username, domain = email.split("@")
if username and domain.endswith(".edu"):
    print("vaild")
else:
    print("Invalid")


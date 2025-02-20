import re 

x = input("number:").strip()
if matches :=re.fullmatch(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9])$", x):
    print("True")
else:
    print("False")
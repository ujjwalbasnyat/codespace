# approach 1 
# with open("names.txt", 'r') as file:
#     lines = file.readlines()
# for line in lines:
#     print(f"hello,{line.rstrip()}")

# approach 2 
# with open("names.txt", 'r') as file:
#     for line in file:
#         print("hello", line.rstrip())

# sorting the names
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):
    print(f"hello, {name}")
print(len(names))
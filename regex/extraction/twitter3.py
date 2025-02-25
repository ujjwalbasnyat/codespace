url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(username)
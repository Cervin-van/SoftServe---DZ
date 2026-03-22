import re

text = input("")
Lens = len(text)
if Lens >= 6 and Lens <= 16:
    if (
        re.search(r"[a-z]", text)
        and re.search(r"[A-Z]", text)
        and re.search(r"[0-9]", text)
        and re.search(r"[$#@]", text)
    ):
        print("OK")
    else:
        print("Error")
else:
    print("Error")

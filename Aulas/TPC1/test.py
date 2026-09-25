import re #módulo para ER (regex)

pattern = re.compile(r"^1*(0|01)*$")

testing = ["", "011", "0001", "111"]

for s in testing:
    result = "Approved" if pattern.fullmatch(s) else "Rejected"
    print(f"{s!r}: {result}")


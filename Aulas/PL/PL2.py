from datetime import datetime
import re
from tokenize import tokenize


# Tests whether a string represents an ISO date, i.e., it has the format YYYY-MM-DD.

def iso_date(text):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}")

    if not pattern.fullmatch(text):
        return False

    try:
        datetime.strptime(text, "%Y-%m-%d") or datetime.strftime(text, "%d-%m-%Y")
        return True
    except ValueError:
        return False
print("Ex.2.1")
print(iso_date("2045-12-03"))
print(iso_date("2045-14-03"))

# Tests whether a string represents a floating point number, with optional
 # sign and exponent.

def float_num(word):
     pattern = re.compile(r"^[+-]?\d*\.\d+")

     if not pattern.fullmatch(word):
         return False
     else:
         return True
print("Ex.2.2")
print(float_num("-.03"))

#Tests whether a string is a valid email address, according to the simplified

def email(text):
    pattern = re.compile(r".*@(gmail|hotmail)\.(com|pt)")

    if not pattern.fullmatch(text):
        return False
    else:
        return True

print("Ex.2.3")
print(email("andre@gmail.com"))
print(email("nada@hotmail.pt"))
print(email("nada@hotmail.com"))
print(email("andre@nada.com"))

# Identify from a list of filenames, those that are 8.3 filenames

def filename83(files):
    pattern = re.compile(r"^.{1,8}\..{1,3}")
    result = []
    for f in files:
        if pattern.fullmatch(f):
            result.append(f)
    return result
print("Ex.2.4")
print(filename83(["AUTOEXEC.BAT", "CONFIG.SYS", "COMMAND.COM"]))
print(filename83(["DOOM.EXE", "MONKEY~1.BAT"]))


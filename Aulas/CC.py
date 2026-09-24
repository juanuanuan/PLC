import cmath
import doctest
import math
# Basic types and control


def break_seconds(secs):
    dias = secs // 86400
    secs = secs % 86400
    horas = secs // 3600
    secs = secs % 3600
    minutos = secs // 60
    segundos = secs % 60
    print(f"dias: {dias}, horas: {horas}, minutos: {minutos}. segundos: {segundos}")



def reverse_num(number):
    return str(number)[::-1]

doctest.run_docstring_examples(reverse_num, globals(), verbose=True)

# como so podemos usar opercoes aritmeticas:

def reverse_num2(number):
    var = 0
    invertido = 0
    while number > 0:
        var = number % 10
        number = number // 10
        invertido = invertido * 10
        invertido = var + invertido
    print(invertido)

reverse_num2(4567)


#Strings

def reverse_str(s):
    r = len(s) - 1
    news = ""
    for w in range(len(s)):
        news = news + s[r]
        r = r - 1
    print(news)

reverse_str("hello")

def camel_case(s):
    result = ""
    backLetter = False
    firstWord = True
    for c in s:
        if c.isalpha():
            if not backLetter:
                if firstWord:
                    result = result + c.lower()
                    firstWord = False
                else:
                    result = result + c.upper()
            else:
                result = result + c.lower()
            backLetter = True
        else: backLetter = False

    return result


print(camel_case("hello))))ok"))

#tuplos

def quadratic_formula(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    res1 = (-b + math.sqrt(d)) / (2 * a)
    res2 = (-b - math.sqrt(d)) / (2 * a)
    return (res1, res2)

print(quadratic_formula(4,2,-4))

def change(amount):
    res = []
    resto1 = amount // 200
    res.append((200, resto1))
    amount = amount - 200
    resto2 = amount // 100
    res.append((100, resto2))
    amount = amount - 100
    resto3 = amount // 50
    res.append((50, resto3))

    return res

print((change(350)))

def vigenere_cipher(key, text):
    res = ""
    for a in text:
        res += key.get(a, '?')
    return res

print(vigenere_cipher({"a" : "x", "b" : "y", "c" : "h", "e" : "m", "l" : "f", "o" : "b"}, "hello"))
print(vigenere_cipher({"a" : "x", "m" : "s", "p" : "h", "s" : "m", " " : " ", "o" : "b", "r" : "w", "k" : "v", "t" : "a", "e" : "b", "h" : "w"}, "x marks the spot"))


def swap_dict(d):
    res = {}
    for k,v in d.items():
        res.setdefault(v, []).append(k)
    return res

print(swap_dict({"a" : "x", "b" : "y", "c" : "h", "e" : "m", "l" : "f", "o" : "b"}))
print(swap_dict({"Jan": "Winter", "Fev": "Winter", "Mar": "Spring", "Apr": "Spring", "Dec": "Winter", "Jul" : "Summer"}))

def iso_strings(s1,s2):
    dic = {}
    for a, b in zip(s1,s2): #iterar duas strings ao mesmo tempo
        dic.setdefault(a, b)
    return dic

print(iso_strings("CABAC","WXYXW"))
print(iso_strings("HELLO","JELLO"))



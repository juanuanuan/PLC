import doctest

# Basic types and control


def break_seconds(secs):
    dias = secs // 86400
    secs = secs % 86400
    horas = secs // 3600
    secs = secs % 3600
    minutos = secs // 60
    segundos = secs % 60
    print(f"dias: {dias}, horas: {horas}, minutos: {minutos}. segundos: {segundos}")
 
doctest.run_docstring_examples(break_seconds, globals(), verbose=True)


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


camel_case("hello))))ok")


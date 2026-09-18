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

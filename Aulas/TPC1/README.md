## TPC1 PLC26

---
## Autoria

Aluno: João Pontes

Nº Mec.: A111657


**Foto:**


<img src="img.png" alt="Fotografia" width="110">

---

## Resumo

O objetivo deste trabalho é definir uma expressão regular e a gramática regular correspondente que gerem todas as strings sobre o alfabeto `{0,1}` que não contêm a substring `"011"`.

Para isso, é necessário construir uma expressão regular equivalente a uma gramática regular que aceite as strings sem a substring acima mencionada.

Sabendo que a string sem `"011"` apenas pode existir com blocos de `0` ou `"01"`,
se garantirmos única e exclusivamente que, num estado de um dado autómato representante da gramática, após a leitura de um `0`, é lido no máximo um `1` antes de o próximo `0` surgir (ou de a string terminar), cumprimos o objetivo.


---

## Resultados

[Expressão Regular](expressao.ipynb)

---
Calculadora de erros
====================

Vamos implementar uma calculadora de valores que possuem barras de erro (lembram
das aulas de física experimental?). Você deve implementar as quatro operações 
básicas (soma, subtração, multiplicação e divisão) com a precedência correta
da matemática.

Números podem ser "puros" ou com erro. Um número puro é declarado como 
simplemente como um float e pode participar de qualquer operação matemática::

  4.0
  3.14
  1.5 + 2.5

Números podem conter um erro associado, especificado em termos absolutos ou
relativos. O erro deve ser inserido dentro de parênteses logo após o número::

  3.1(0.1)
  5.25(10%)

Também deve ser possível atribuir variáveis e utilizá-las em expressões::

  pi = 3.14
  y = pi * 4.0

O parser deve aceitar as quatro operações, agrupamento com parênteses e 
operadores unários::

  1 + 1
  2 - 1
  3 * 2
  6 / 2
  2 * (3 + 4)
  +42
  -42


Rodando os testes
-----------------

Rode os testes com ``pytest tests.py``. A nota é o número de testes 
que passaram - 2.

Dicas
.....

Se o Python padrão for o Python 2:
  ``python3 -m pytest tests.py``
Para limitar a saída do pytest ao primeiro erro: 
  ``pytest tests.py --maxfail=1``
Iniciar shell interativo: 
  ``python3 calculadora.py ARQUIVO``
Instalar dependências:
  ``pip3 install ox-parser pytest --user -U``

**Atenção:** Não funciona em Python 3.5.
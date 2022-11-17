# fact e fibc são funções recursivas que fornecem
# fatorial e posição na seqência de Fibonacci de
# um número inteiro

def fact(x):
    if (x == 0 or x == 1):
        return 1
    if (x >= 2):
        return x*fact(x-1)

# Consideram-se 0, 1 os termos iniciais de
# posições 1, 2 na sequência de Fibonacci.

def fibc(x):
    if (x == 1):
        return 1
    if (x == 2):
        return 1
    if (x >= 3):
        return fibc(x-1) + fibc(x-2)

# Leitura do arquivo input.dat, cujo conteúdo é
# repassado à string input

test1 = ''
test2 = ''

f = open("test.data", "r")
for y in f:
    test1 += y
f.close()

g = open("test2.data", "r")
for y in g:
    test2 += y
g.close()

def table(string):
  table = string.split("\n\n")
  m = len(table)
  i = 0
  
  while (i < m):
    table[i] = table[i].split(' ')
    i += 1

  return table

teste1 = table(test1)
teste2 = table(test2)

def testtable(table):
  m = len(table)
  i = 1
  errors = []
  while (i < m):
    n = int(table[i][0])
    fac = fact(n)
    fib = fibc(n)
    if (int(table[i][1]) != fac or int(table[i][2]) != fib):
      errors += str(i)
    i += 1

  return errors

def output(table):
  err = testtable(table)
  k = len(err)
  n = 3
  i = 0
  if (k == 0):
    print("Arquivo com dados corretos")
  if (k  > 0):
    print("Arquivo com erros nas linhas:\n")
    while (i < k):
      for j in range(n):
        print(table[int(err[i])][j],end=' ')
      print("\n")
      i += 1

print("teste.data")
output(teste1)
print("\n")
print("teste2.data")
output(teste2)
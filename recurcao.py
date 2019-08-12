#1) Calcule a fatorial de 5. 5!
def fatorial(x):
    if (x == 1):
        return x;
    x = x * fatorial(x - 1);
    return x;
print(fatorial(5));

#2) Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de x^n.
def recursiva():
    x = int(input('N: '));
    n = int(input('N: '));
    if(n == 0):
        return 1;
    if(x > n):
        el = x ** n;
        return(el);
print(recursiva()); 

x = int(input('N: '));
n = int(input('N: '));
def função(x,n):  
    if(x == 1 or n == 1):
        return x;
    else:
        return x * função(x,n - 1);
print(função(x,n));

#3) Usando recursividade, calcule a soma de todos os valores de um array de números reais.
lista = [10,20,30,40,50];
v = 0
def soma(lista,v):
    if(v == len(lista)): 
        return 0;
    return lista[v] + soma(lista,v+1)
print(soma(lista,v))

#4) Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N.
# Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def media():
    N1=float(input('nota 1: '));
    N2=float(input('nota 2: '));
    media=float(N1+N2)/2;
    print('a sua media e:{}'.format(media));
media();

def soma (numero1,numero2):
    result = numero1+numero2;
    return result;

def exibe_soma(n1,n2):
    resultado = soma(n1,n2);
    print(resultado);
x = int(input('digite o primeiro numero: '));
y = int(input('digite o segundo numero: '));

exibe_soma(x,y);
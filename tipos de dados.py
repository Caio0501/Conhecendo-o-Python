#1

print('Alo Mundo');
"""
#2
"""
print('fale dois numeros para somar');
n1=int(input('me de um numero:'));
n2=int(input('me de outro numero:'));
print('soma e:');
print(n1 + n2);
"""
#3
"""
print('Me de as sua notas dos ultimos quatro bimetre');
N1=float(input('prmeiro bimestre:'));
N2=float(input('segundo bimestre:'));
N3=float(input('terseiro bimestre:'));
N4=float(input('quarto bimestre:'));
Media=float(N1+N2+N3+N4)/4;
print('a media e:{}'.format(Media));
"""
#4
"""
print('quantos metros deseja converter para centimetros?')
Metros=float(input('metros:'));
Centimetro =(Metros * 100);
print('centimetros:{}cm'.format(Centimetro));
"""
#5
"""
F=float(input('me de um valor em graus F:'));
C=(5*(F-32))/9
print('este valor em celcios sera:{}'.format(C));
"""
#6
"""
sexo= input('digite H para homen e M para mulher: ');
if(sexo=='H' or sexo=='h'):
    print('homen');
    Altura=float(input('me diga sua altura:'));
    P=(72.7*Altura)-58
    print('seu peso ideal e:{} '.format(P));
                
else:
    print('mulher');
    Altura=float(input('me diga sua altura:'));
    P=(62.1*Altura)-44.7
    print('seu peso ideal e:{} '.format(P));  

"""
#7
"""
print('Hello Word');
"""
#8
"""
print('me de 2 notas: ');
N1=float(input('nota 1: '));
N2=float(input('nota 2: '));
media=float(N1+N2)/2;
print('a sua media e:{}'.format(media));
"""
#9
"""
print('quantos metros deseja converter para centimetrso: ');
metro=float(input('metros: '));
centimetros=(metro * 100);
print('centimetos:{}cm'.format(centimetros));
"""
#10
"""
print('me de suas 4 notas bimestrais: ');
b1=float(input('nota 1: '));
b2=float(input('nota 2: '));
b3=float(input('nota 3: '));
b4=float(input('nota 4: '));
media=float(b1+b2+b3+b4)/4;
print('a sua media dos 4 bimestres e:{}'.format(media));
"""
#11
"""
print('me de as notas das suas 3 ultimas provavas valendo 10')
n1=float(input('nota 1: '));
n2=float(input('nota 2: '));
n3=float(input('nota 3: '));
soma=(n1+n2+n3);
if(soma >= 18):
    print('aprovado');
elif(soma <=17.9):
    print('prova final');
if(soma <=8.9):
   print('reprovado') ; 
"""
#12
"""
print('me de dois numeros');
n1=float(input('numero1: '));
n2=float(input('numero2: '));
if(n1>n2):
    print('o maior e:{}'.format(n1));
if(n2>n1):
    print('o maior e:{}'.format(n2));
"""
#13
"""
print('me de o peso do peixe');
peso=float(input('peso: '));
if (peso > 50):
    excesso = (peso-50);
    multa   = (excesso * 4);
else:
    excesso = ('ZERO');
    multa   = ('ZERO');
print('excesso de peso e:{}kg'.format(excesso),'por isso sua multa e de:{}$'.format(multa)) ;
"""
#14
"""
print('me de 3 numeros');
n1=int(input('n1: '));
n2=int(input('n2: '));
n3=int(input('n3: '));
if(n2>n1)and(n3>n1):
    if(n2<n3):
        print(n1);
        print(n2);
        print(n3);
    else:
        print(n1);
        print(n2);
        print(n3);        
elif(n1>n2)and(n3>n2):
    if(n1<n3):
        print(n2);
        print(n1);
        print(n3);
    else:
        print(n2);
        print(n3);
        print(n1);
elif(n1>n3)and(n2>n3):
    if(n1<n2):
        print(n3);
        print(n2);
        print(n1);
    else:
        print(n3);
        print(n1);
        print(n2);
if(n1==n2)or(n1==n3)or(n2==n3):
    print('ERRO 2 numeros iguais');
"""
#15
"""
print('me de um numero inteiro');
numero=int(input('numero: '));
if (numero)%2 == 0:
    print('o numero e par');
else:
    print('o numero e inpar');
"""    
#16
"""
SR=input('digite S para soma R para rais: ');
if(SR=='S'):
    print('soma');
    n1=float(input('me de um valor: '));
    n2=float(input('me de outro valor: '));
    soma=(n1+n2);
    print('a soma e:{}'.format(soma));
else:
    print('rais');
    n1=float(input('me de um valor: '));
    rais=(n1**0.5);
    print('a rais e:{}'.format(rais));
"""
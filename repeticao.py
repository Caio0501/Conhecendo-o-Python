#1 

con = 0;
soma = 0;
op=True;
print('digite "e" para fazer a media');
while(op):
	x=input('digite sua nota: ');
	if(x == 'e'):
		x = False;
		break;
	else:
		con=con+1;
		soma=soma+int(x);
media=str (soma / con);
print('a sua media e  ' + media);
"""
#2/3
"""
soma =0;
con=0;
while (con != 9):
	con = con + 1;
	soma = soma + con;
	print(con);
print(soma);
"""
#4 
"""

op=True;
cont = 0;
cont2= 0;
cont3= 0;
contador = 0;
print('digite sair para parar o registro');
while(op and contador !=15):
	idade=input('digite a idade:');
	contador = contador + 1
	#print(contador);
	if(idade == 'sair'):
		op=False;	
	elif (idade == '10'):
		cont = cont + 1;
		a = cont;
	elif (idade == '15'):
		cont2 = cont2 + 1;
		b = cont2;
	elif (idade >= '15'):
		cont3 = cont3 + 1;				
		c = cont3;
print('pessoas com 10 anos:{}'.format(a));
print('pessoas com 15 anos:{}'.format(b));
print('pessoas maiores de 15 anos:{}'.format(c));
"""	
#5
"""
cont = 0;
notas =['0'];
print('digite sair para parar o registro');
for nota in notas:
	nota = input('nota: ');
	if(nota == 'sair'):
		break;
	elif(nota !='sair'):
		notas.append(int(nota));
		cont = cont + 1;
notas.pop(0); 
print(notas);

soma = 0
media = 0
for nota in notas:
	soma =(soma + nota);
	media = soma/cont;
print(soma);
"""
#6
"""
lista = [0];
print('Coloque de a idade e a nota dos alunos!');
print('Notas menores que 6 reprovado, e maiores ou igual a 6 aprovado')
print('Coloque "sair" no nome parar o registro')
for name in lista:
	name= input('nome: ');
	if(name != 'sair'):
		nota= int(input('nota: '));
	if(name == 'sair'):
		break;
	if(nota <= 5):
			resu =('reprovado(a)');
	if(nota >= 6):
			resu=('aprovado(a)');
	NN=('Nome:{} Nota:{} {}'.format(name,nota,resu));	
	lista.append(NN);	
lista.pop(0);		
print(lista);

#7


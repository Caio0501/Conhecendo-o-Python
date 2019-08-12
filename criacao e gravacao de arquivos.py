

print('Agenda');
agenda = open('agenda.txt','w');
N_pessoa = int(input('quantas pessoas vc deseja cadastra: '));
for i in range(N_pessoa):
    nome = input('Nome: ');
    idade = input('idade: ');
    numero = input('numero: ');
    agenda.write(nome+';'+idade+';'+numero+'\n');
agenda.close();      





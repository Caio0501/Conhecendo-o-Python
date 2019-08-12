#Ordenar lista por BubbleSort
#Ordenar lista por SelectSort
#Ordenar lista por MergeSort

lista  = [7,6,5,4,3,2,1];
lista2 = [9,8,7,6,5,4,3,2,1,0];
def Bubblesort(lista):
    n = len(lista);
    for j in range(n):
        ordenado = False;
        for i in range(n-1):
            if (lista[i] > lista[i+1]):
                troca = lista[i];
                lista[i] , lista[i+1] =lista[i+1], lista[i] ;
                troca = lista[i+1];
                ordenado = True;
        if (ordenado == False):
            break;
    print(j, lista);
 
def SelectSort(lista2):
    for i in range(0,len(lista2)-1):
        valorminimo = i;
        for j  in range(i+1, len(lista2)):
            if(lista2[j] < lista2[valorminimo]):
                valorminimo = j
        if (valorminimo != i):
            lista2[i], lista2[valorminimo] = lista2[valorminimo], lista2[i];
    print(j, lista2)

###################################################################
bubble = Bubblesort(lista);
select = SelectSort(lista2);





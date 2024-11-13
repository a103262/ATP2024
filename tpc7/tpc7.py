### TPC7: Resolver a alínea anterior Cria uma aplicação Python que permita ao utilizador usar todas as funcionalidades pedidas nesta ficha.

### Exercício 1: Considere os seguintes comentários que definem um modelo para guardar os registos de temperatura e precipitação ao longo de vários dias, materializado na variável tabMeteo1:
# TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]
    # Data = (Int,Int,Int)
    # TempMin = Float
    # TempMax = Float
    # Precipitacao = Float

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

### 1.a) Calcula a temperatura média de cada dia, dando como resultado uma lista de pares: [(data, temperaturaMédia)]:

def medias(tabMeteo):
    res = [ ]
    for dia in tabMeteo:
        mediatemp = (dia [1]+ dia[2])/2
        res.append((dia[0],mediatemp))
    return res 

def guardaTabMeteo(t, fnome):
   f= open (fnome, "w")
   for data, tmin, tmax, precip in t:
       linha= f"{data[0]} :: {data[1]}::{data[2]}::{tmin}::{tmax}::{precip}\n"
       f.write(linha)
   f.close()
   return

def carregaTabMeteo (fnome):
    res = [ ]
    f= open(fnome)
    for linha in f:
        if linha != " ":
            campos = linha.split('::')
            data =(int(campos[0]),int(campos[1]),int(campos[2]))
            res.append((data, float(campos[3]), float(campos[4]),float(campus[5])))
    f.close()
    return res 


def minMin(tabMeteo):
    minima= tabMeteo[0][1]
    for data,tmin,tmax, precip in tabMeteo[1:]:
        if tmin<minima :
            minima = tmin 
    return minima

def amplTerm( tabMeteo):
    res =[]
    for data, tmin, tmax, _ in tabMeteo:
        res.append((data, tmax-tmin))
    return res 

def maxChuva( tabMeteo):
    max_prec= tabMeteo[0][3]
    max_data=tabMeteo[0][0]
    for data,_,_,precip in tabMeteo[1:]:
        if max_prec<precip:
            max_prec=precip 
            max_data=data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for data,_,_, precip in tabMeteo:
        if precip > p:
            res.append((data,precip))
    return res 

def maxPeriodoCalor(tabMeteo, p):
    consecutivos =0
    contador=0
    for *_, precip in tabMeteo:
        if precip<p:
            contador= contador+1 
        else:
            if contador> consecutivos:
                consecutivos =contador 
            contador = 0

    return consecutivos

def menu():
    print("1- calcular a temperatura média de cada dia ")
    print("2-guardar a tabela metereológica")
    print("3-carregar tabela metereológica")
    print("4-temperatura maxima mais baixa registada na tabela")
    print("5-calcula a amplitude térmica")
    print("6-o dia em que a precipitação teve o seu valor máximo")
    print("7- tabela metereológica e limite p e devolve os dias em que a precipitação foi superior a p")
    print("8-retorna o maior número consecutivo de dias onde a precipitação é abaixo de p")
    print("0- sair da aplicacao")

    opcao = int(input("qual opcao deseja selecionar?"))
    return opcao

op = menu
while op!= 0:
    if op== 1:
        medias (tabMeteo1)
        print(medias( tabMeteo1))
    elif op==2:
        guardaTabMeteo(tabMeteo1, "metereologia.txt")
    elif op==3:
        tabMeteo2 = carregaTabMeteo("metereologia.txt")
        print(tabMeteo2)
    elif op==4:
        print(minMin(tabMeteo1))
    elif op==5:
        print(amplTerm(tabMeteo1))
    elif op==6:
        print(maxChuva(tabMeteo1))
    elif op==7:
        print(diasChuvosos(tabMeteo1, 0.1))
    elif op==8:
        print(maxPeriodoCalor(tabMeteo1, 0.1))
    op=menu()
print("obrigada")


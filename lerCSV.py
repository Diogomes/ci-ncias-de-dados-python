'''
Vamos importar nosso arquivo de dados mpg.csv, que contém dados de economia de combustível de 234 carros.

mpg: milhas por galão
classe: classificação do carro
cty: cidade mpg
cyl: Nº de cilindros
deslocamento: deslocamento do motor em litros
drv: f = tração nas rodas dianteiras, r = tração nas rodas traseiras, 4 = 4x4
fl: combustível (e = etanol E85, d = diesel, r = regular, p = prêmio, c = GNV)
hwy: estrada mpg
fabricante: fabricante de automóveis
modelo: modelo de carro
trans: tipo de transmissão
ano: ano modelo


'''

import csv

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
    
mpg[:3] # Os três primeiros dicionarios na lista.

#csv.Dictreaderleu em cada linha do nosso arquivo csv como um dicionário.
# len mostra que nossa lista é composta por 234 dicionários.
len(mpg)

#keys nos fornece os nomes das colunas do nosso csv.

mpg[0].keys()

#É assim que se encontra a economia média de combustível em todos os carros. 
#Todos os valores nos dicionários são cadeias de caracteres, portanto, precisamos converter para flutuar.
sum(float(d['cty']) for d in mpg) / len(mpg)

#Da mesma forma, é assim que se encontra a economia média de combustível em todos os carros.
sum(float(d['hwy']) for d in mpg) / len(mpg)
#Use setpara retornar os valores exclusivos para o número de cilindros que os carros em nosso conjunto de dados possuem.

cylinders = set(d['cyl'] for d in mpg)
cylinders

#Aqui está um exemplo mais complexo em que agrupamos os carros
#por número de cilindros e encontramos a média de cty mpg para cada grupo.
CtyMpgByCyl = []

for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl

#Use setpara retornar os valores exclusivos para os tipos de classe em nosso conjunto de dados.
vehicleclass = set(d['class'] for d in mpg) # what are the class types
vehicleclass

#E aqui está um exemplo de como encontrar o mpg hwy médio para cada classe de veículo em nosso conjunto de dados.

HwyMpgByClass = []

for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
        if d['class'] == t: # if the cylinder amount type matches,
            summpg += float(d['hwy']) # add the hwy mpg
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1])
HwyMpgByClass

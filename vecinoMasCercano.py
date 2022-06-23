#--------------------LIBRERIAS A UTILIZAR------------------------------
from sklearn import datasets

dataset = datasets.load_breast_cancer()
print(datasets)

#verifico la informacion contenida en el dataset
pront('informacion en el datasets: ')

print(datasets.keys())

print()
#verifico las caracteristicas del dataset

print('caracteristicas del dataset: ')
print(dataset.DESCR)

#seleccionamos todas las columnas 
x=dataset.data

#defino los datos correspondientes a las  etiquietas
y=dataset.target


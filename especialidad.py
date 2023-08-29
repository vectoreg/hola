import random

calcular_valor_medido= lambda valor_nominal, tolerancia:valor_nominal+random.uniform(-tolerancia,tolerancia)

def verificar_instalacion(magnitud, valor_nominal, tolerancia):

try:
    valor_medido= calcular_valor_medido(valor_nominal, tolerancia )
    if abs(valor_medido-valor_nominal)<= tolerancia:


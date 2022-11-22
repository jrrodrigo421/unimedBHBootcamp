## Desafios UNIMED TECH

## As duas Torres:
##usei o mesmo codigo que ja estava no inicio do desafio
entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])
## adcionei aqui o calculo a ser feito, e fiz uma formatação na String colocando as duas casas decimais que pedia
ICM = distancia / (diametro1 + diametro2)
print(f'{ICM:.2f}')

## Cachorros Quentes:
## Aproveitando o codigo inicial, determinei apenas os valores separados para assim criar a expressao e imprimir a media:
valores = input().split()

cachorrosquentes = int(valores[0])
participantes = int(valores[1])
media = cachorrosquentes / participantes

print(f'{media:.2f}')

##Calculo da Viagem
## novamente, aproveitando o codigo inicial, separei as variaveis criei uma nova também e montei a expressão

valores = input().split()

tempo = int(valores[0])
velocidade = int(valores[1])
consumo = 12
total = (tempo * velocidade) / consumo

print(f'{total:.3f}')
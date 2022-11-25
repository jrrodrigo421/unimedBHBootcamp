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







#desafio Alfabeto


# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
letra = input()


# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
lista = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H,' 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#testes com FOR:
# for i in lista:
#   if letra in lista:
#     print(lista.index(letra))
#   else:
#     break


##resposta correta:
indice = lista.index(letra)
print(indice)


##Desafio do PAPAGAIO:

# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado


letra = input()

# while True:
#     try:
#           # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
#           # e imprima a saída de acordo com a situação das pernas do papagaio
#     except EOFError:
#         break

if letra == 'esquerda':
  print('ingles')
if letra == 'direita':
  print('frances')
if letra == 'nenhuma':
  print('portugues')
if letra == 'ambas':
  print('caiu')
else:
    letra = input()
    if letra == 'esquerda':
        print('ingles')
    if letra == 'direita':
        print('frances')
    if letra == 'nenhuma':
      print('portugues')
    if letra == 'ambas':
        print('caiu')
    else:
        letra = input()
        if letra == 'esquerda':
            print('ingles')
        if letra == 'direita':
            print('frances')
        if letra == 'nenhuma':
            print('portugues')
        if letra == 'ambas':
            print('caiu')
        else:
            letra = input()
            if letra == 'esquerda':
                print('ingles')
            if letra == 'direita':
                print('frances')
            if letra == 'nenhuma':
                print('portugues')
            if letra == 'ambas':
                print('caiu')
            else:
                exit

##Salario:


salario = int(input())

if salario <= 600:
    percentual = 17
    reajuste = (salario / 100) * percentual
    novo_salario = (salario / 100) * percentual + salario
    print('Novo salario:', "{:.2f}".format(novo_salario))
    print('Reajuste ganho:', "{:.2f}".format(reajuste))
    print('Em percentual: {} %'.format(percentual))
elif salario <= 900:
    percentual = 13
    reajuste = (salario / 100) * percentual
    novo_salario = (salario / 100) * percentual + salario
    print('Novo salario:', "{:.2f}".format(novo_salario))
    print('Reajuste ganho:', "{:.2f}".format(reajuste))
    print('Em percentual: {} %'.format(percentual))
elif salario <= 1500:
    percentual = 12
    reajuste = (salario / 100) * percentual
    novo_salario = (salario / 100) * percentual + salario
    print('Novo salario:', "{:.2f}".format(novo_salario))
    print('Reajuste ganho:', "{:.2f}".format(reajuste))
    print('Em percentual: {} %'.format(percentual))
elif salario <= 2000:
    percentual = 10
    reajuste = (salario / 100) * percentual
    novo_salario = (salario / 100) * percentual + salario
    print('Novo salario:', "{:.2f}".format(novo_salario))
    print('Reajuste ganho:', "{:.2f}".format(reajuste))
    print('Em percentual: {} %'.format(percentual))
else:
    percentual = 5
    reajuste = (salario / 100) * percentual
    novo_salario = (salario / 100) * percentual + salario
    print('Novo salario:', "{:.2f}".format(novo_salario))
    print('Reajuste ganho:', "{:.2f}".format(reajuste))
    print('Em percentual: {} %'.format(percentual))

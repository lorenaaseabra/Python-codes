#Finanças da casa [Faça os tratamentos de erros que achar necessário]
#Conversando com a tua familia, você resolveu fazer uma aplicação para calcular mensalmente os gastos da casa 
# dividir proporcionalmente com cada pessoa que tem renda. Para isso você deverá fazer uma aplicação 
# dividida em três etapas, a primeira consiste no cadastro de todas as pessoas da casa, 
# nesse cadastro você deve pedir o nome e a renda de cada pessoa. 
# A segunda etapa consiste no cadastro das contas, pra isso você deve pedir o nome de cada conta e o seu valor. 
# or fim, sua aplicação deve calcular PROPORCIONALMENTE o valor com que cada pessoa deve contribuir para pagar 
# as contas, informando o nome da pessoa e o valor. OBS: Usuários sem renda devem ser cadastrados 
# com a renda zerada; Caso a soma das rendas seja menos que a soma das contas, a aplicação deve avisar que a 
# família deve fazer corte de gastos;

#1-a primeira consiste no cadastro de todas as pessoas da casa, nesse cadastro você deve pedir
#  o nome e a renda de cada pessoa.
def cadastro_pessoas():
        pessoas = []
        #dados = {'cadastro','contas'}
        while True: # for cadastro in dados:
                nome = input("digite o nome (digite fim para finalizar): ")
                if nome  == "fim":
                        break 
                else:
                        renda = float(input("digite a renda (digite fim para finalizar): ")) 
                        pessoas.append(nome)
                        pessoas.append(renda)
                        
        return pessoas
#2-A segunda etapa consiste no cadastro das contas, pra isso você deve pedir o nome de cada conta e o seu valor
def cadastro_contas():
        bills  = []
        while True:
                nome_conta = input("digite o nome da conta (digite fim para finalizar): ")
                if nome_conta == "fim":
                        break 
                else:
                        valor = float(input("digite o valor da conta (digite fim para finalizar): ")) 
                        bills.append(nome_conta)
                        bills.append(valor)
        return bills


lista_pessoas = cadastro_pessoas()
lista_contas = cadastro_contas()
#3- sua aplicação deve calcular PROPORCIONALMENTE o valor com que cada pessoa deve contribuir 
# para pagar as contas, informando o nome da pessoa e o valor.

# pega index impar / valor total da renda da familia 
renda_total = 0
for i in range(len(lista_pessoas)):
        if i % 2 == 1:
                renda_total += lista_pessoas[i]

#[a, 300, b, 300, c, 1000] -> teste
                

#pega index impar contas/ valor da soma de todos os valores de conta
conta_total = 0
for i in range(len(lista_contas)):
        if i % 2 == 1:
                conta_total += lista_contas[i]


dicto_renda = {}
for i in range(0, len(lista_pessoas),2):
        dicto_renda[lista_pessoas[i]] = lista_pessoas[i+1]


for i in dicto_renda:
        porcentagem_a_pagar = dicto_renda.get(i) * 100/ renda_total
        valor_individual = (porcentagem_a_pagar/100) * conta_total
        print('o valor que', i, 'deve pagar é igual a: R$', valor_individual)
             





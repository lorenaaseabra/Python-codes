# Você trabalha na RIOT, empresa criadora do Valorant, jogo mundialmente famoso, no valorant existem 4funções
# de agentes, os iniciadores, os sentinelas, os controladores e os duelistas, elas são demonstradas no 
# dicionário abaixo
# 		Valorant = { ‘Iniciadores’ : {
# “Sova”: {“País”: "Rússia"},
# “Breach”{“País”: “Suecia”}
# },
# ‘Duelista’: {
# 	“Raze”: {"País": “Brasil”}
# }
# }


# Seu trabalho é preencher o dicionário com todos os nomes dos agentes, inclusive com o novo agente
# Chamber. ele será preenchido através de um arquivo que será passado pelo usuário e terá o seguinte padrão:

# Iniciadores,Sova,Rússia
# Iniciadores,Breach,Suecia
# Duelista,Raze,Brasil

# Além disso, tudo que você precisar fazer para funcionar o exercício deve estar em uma função com o nome da 
# ação que está sendo realizada, por exemplo:

# Se você precisar abrir um arquivo, deverá ser criada a função openFile()
# Se você precisa adicionar no dicionário, deverá criar uma função add_dicto()
	 
# Na parte principal do código só deve ter uma chamada de função e mais nada,  main(),
# onde deve conter todo o código nela.



def organization():
        global list_sentinela
        list_sentinela = []
        global list_controlador
        list_controlador = []
        global list_iniciador
        list_iniciador = []
        global list_duelista
        list_duelista = []
        file = open('valorant.txt', 'r')
        
        for line in file.readlines():
                virgula = line.index(',')
                if line[:virgula] == 'sentinela':  
                        list_sentinela.append(line[virgula:])
                if line[:virgula] == 'controlador':  
                        list_controlador.append(line[virgula:])
                if line[:virgula] == 'iniciador':
                        list_iniciador.append(line[virgula:])
                if line[:virgula] == 'duelista':
                        list_duelista.append(line[virgula:])
        file.close()

organization()

def details():
        for i in list_sentinela: 
                i.replace(',','')
                i.replace('\n','')
        
                

details()

#def open_dicto ():

#def functionduelista():
        #duelista = {}
        #for index in list_duelista: 
               #{ nome : {'pais': nomedopais}}
        #duelista = {[0] : {'país': [1]}}
        

        


print(list_duelista)
print(list_controlador)
print(list_iniciador)
print(list_sentinela)


        




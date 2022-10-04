#Faça a função registerBooks que irá receber como parâmetros: 
#name_book (uma string), names_author (uma lista de strings),
#classification (uma string). Essa função deverá preencher um dicionário chamado 
#"acervo" como na imagem abaixo. Obs: O dicionário acervo não deve estar no escopo da função e
#a função não deve ter nenhum retorno.

acervo = {}

def registerbooks(name_book, names_author,classification):
        acervo[classification] = {name_book:names_author}
        
#exemplos de teste
registerbooks('harry potter', ['jk', 'clarice'], 'SCFY')
registerbooks('percy',['x','y'],'fant')
print(acervo)



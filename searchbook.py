#Pesquisar livros Faça a função searchBooks que irá receber como parâmetro name_book e irá buscar 
# as informações no dicionário acervo e imprimir na tela TODAS as informações do livro, 
# conforme a imagem abaixo.
#classificação:
#Nome do livro:
#Autorres: \n

def searchbook():
        book_2 = []
        while(True):
                book = {}
                nome_livro = input('Digite o nome (digite fim para encerrar): ')
                if nome_livro != 'fim':
                        print("Informações do livro")
                        Classificacao = input('Digite a Classificação: ')
                        Autores = input('Digite os nomes dos autores: ')
                        book['nome_livro'] = nome_livro
                        book['Classificacao'] = Classificacao
                        book['Autores'] = Autores
                        book_2.append(book)
                else:
                        break
        return book_2

def buscando(lista):
        while(True):
                nome_Buscado = input('Digite o nome do livro que deseja buscar (digite fim para encerrar): ')
                for dicto in lista:
                        if nome_Buscado == dicto['nome_livro']:
                                print('Nome do livro: ' +dicto['nome_livro'])
                                print('Classificação: ' +dicto['Classificacao'])
                                print('Autores: ' +dicto['Autores'])
                if nome_Buscado == 'fim':
                        break

lista = searchbook()
buscando(lista)

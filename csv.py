import csv

def cadastro_livro(livros):
        while(True):
                book = {}
                nome = input('Digite o nome do livro(digite fim para encerrar): ')
                if nome != 'fim':
                        autores = input('Digite os nomes dos autores: ')
                        idioma = input('digite o idioma do livro:')
                        primeira_pub = int(input('Digite o ano de publicação:'))
                        vendas_aprox = input('digite a quantidade aproximada de livros vendidos:')
                        book['book'] = nome
                        book['Autor(es)'] = autores
                        book['idioma'] = idioma
                        book['primeira_pub'] = primeira_pub
                        book['vendas_aprox'] = vendas_aprox
                        livros.append(book)
                else:
                        break
                
        return livros

livros = []
livros = cadastro_livro(livros)

headers = ['book','Autor(es)','idioma','primeira_pub','vendas_aprox']
f = open('livros.csv','w')
w = csv.DictWriter(f,fieldnames=headers)
w.writeheader()
for dicto in livros:
        w.writerow(dicto)
f.close()

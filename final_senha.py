def change(string):
        string = string.lower()
        string = string.title()
        string = string.strip()
        string = string.replace('\n','')
        string = string.replace("a","@")
        string = string.replace("A","@")
        string = string.replace("i","1")
        string = string.replace("I","!")
        string = string.replace(' ','')
        string = string.replace('.','I\'mGroot')
        string = string.replace(',','I\'mGroot')
        string = string.replace(';','I\'mGroot')
        string = string.replace(':','I\'mGroot')
        
        return string

def math(string,number):

        print(string[:4] + string[-4:] + string[number:number+4])

        


string = ''
while True: #tratamento de erro
        string = input('digite um texto com no mínimo 200 palavras: ') 
        if len(string) < 200: 
                print('ERROR! A quantidade de caracteres é menor do que a permitida')
        else:
                break
        

while True: #tratamento de erro
        try: 
                number = int(input('informe um número diferente de zero ou do tamanho da frase -4:'))
                if number == 0 or number == len(string)-4: #seria p usar tratamento de erro?
                        print('informe um número possível!')

                string = change(string)

                math(string,number)

                resposta = input('Se você deseja continuar gerando senhas com essa frase digite S ou N:')
                
                if (resposta == 'S'):
                        continue
                elif (resposta == 'N'):
                        break 
                else:   
                        print('Digite apenas S ou N')
                
        except: 
                print('Digite apenas números!!')
        



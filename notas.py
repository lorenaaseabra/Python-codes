# Calcula nota de FP[Faça os tratamentos de erro necessários]
# Faça um algoritmo que receba do usuário os segufloates dados:
#  NotaP1, NotaP2, NotaListaM1, NotaListasM2, NotaTrabalho, PesoM1, PesoM2. 
# Seu algoritmo deve calcular a nota do aluno e mostrar a média final e se ele está Aprovado, 
# Reprovado ou Final. O calculo da nota deve seguir a formula da imagem

def verify(number):
        if number < 0 or number > 10:
                print('Informe apenas numeros entre 0 e 10')
                return True
        return False

def verify1(number):
        if(number == 0):
                print("Se divide numero por 0?")
                return True
        return False
        
while True:
        try:
                print("---------------------")
                notap1 = float(input('digite sua nota da primeira prova:'))
                check = verify(notap1)
                if(check):
                        continue
                notap2 = float(input('digite sua nota da segunda prova:'))
                check = verify(notap2)
                if(check):
                        continue
                notalista_1 = float(input('digite a média de suas listas 1:'))
                check = verify(notalista_1)
                if(check):
                        continue
                notalista_2 = float(input('digite a média de suas listas 2:'))
                check = verify(notalista_2)
                if(check):
                        continue
                pesom2= float(input('digite a quantidade de listas1 que teve/o peso:'))
                check = verify(pesom2)
                check1 = verify1(pesom2)
                if(check or check1):
                        continue
                pesom1= float(input('digite a quantidade de listas2 que teve/o peso:'))
                check = verify(pesom1)
                check1 = verify1(pesom1)
                if(check or check1):
                        continue
                
                media_final = ((((notap1 + notalista_1)/pesom1) + ((notap2 + notalista_2)/pesom2))/2)

                if media_final > 7:
                        print('Sua média foi', media_final, 'Você está aprovado!')
                elif media_final > 3 and media_final < 7:
                        print('Sua média foi', media_final, 'Você está na final! ')
                else:
                        print('Sua média foi', media_final, 'Você está reprovado!')
                break

        except: 
                print('Digite apenas números do tipo real')
                continue



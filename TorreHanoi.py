discos = input("Digite a quantidade de discos: ")
discos = int(discos)
A = list(range(discos, 0, -1))
A.reverse() #Inverto a lista apenas por questão de estética.
B = []
C = []
Cf = list(range(discos, 0, -1)) #Não sabia como fazer essa parte de maneira mais simples, embora acredite que seja possível.
Cf.reverse()
Torres = [A, B, C]
Jogadas = 0

def Mover(hasteo, hasted): #Essa função que move os discos entre as hastes, a sequência de ifs verifica se o movimento é valido ou não.
    global Jogadas
    if not hasteo:
        print("Movimento Invalido.\n")
    else:
        if hasted and hasteo[0] > hasted[0]:
            print("Movimento Invalido.\n")
            return None
        else:
            mov = hasteo.pop(0)
            hasted.insert(0, mov)
            Jogadas += 1

def Haste(check): #Essa função processa a jogada realizada e retorna a torre para a função "mover".
    check = int(check)
    if 1 <= check <= len(Torres):
        return Torres[check - 1]
    else:
        print("Por favor, escolha a torre 1, 2 ou 3.\n")
        return None

def Resolva(n, origem, destino, auxiliar): #Essa função resolve o jogo por recursão e mostra as jogadas realizadas.
    if n == 1:
        Mover(origem, destino)
        print("\nJogadas: " + str(Jogadas) + "\nHaste 1: " + str(A) + "\nHaste 2: " + str(B) + "\nHaste 3: " + str(C) + "\n")
        return
    Resolva(n - 1, origem, auxiliar, destino)
    Mover(origem, destino)
    print("\nJogadas: " + str(Jogadas) + "\nHaste 1: " + str(A) + "\nHaste 2: " + str(B) + "\nHaste 3: " + str(C) + "\n")
    Resolva(n - 1, auxiliar, destino, origem)

def Jogar(): #Essa função permite que você jogue o jogo, requisitando jogadas e enviando elas para a função "Haste".
    while C != Cf:
        mov1 = input("Digite a haste do disco que deseja mover: ")
        mov2 = input("Digite o destino do disco: ")
        if mov1 and mov2:
            hasteo = Haste(mov1)
            hasted = Haste(mov2)
            if hasteo is not None and hasted is not None:
                Mover(hasteo, hasted)
        print("\nJogadas: " + str(Jogadas) + "\nHaste 1: " + str(A) + "\nHaste 2: " + str(B) + "\nHaste 3: " + str(C) + "\n")

    print("\nParabens, voce venceu o jogo!\n")

print("\nJogadas: " + str(Jogadas) + "\nHaste 1: " + str(A) + "\nHaste 2: " + str(B) + "\nHaste 3: " + str(C) + "\n")

Opcoes = input("Escolha dentre as opcoes: \n1) Jogar\n2) Resolver para " + str(discos) + " Discos\n3) Sair\n> ") #Menu porco que deu mais trabalho do que deveria.
if Opcoes == '2':
    Resolva(discos, A, C, B)
elif Opcoes == '1':
    Jogar()
else:
    print("Adeus.")

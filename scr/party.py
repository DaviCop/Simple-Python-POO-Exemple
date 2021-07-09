from scr.personagem import *

class Party:

    def __init__(self):
        self.personagens = [False, False, False, False]

    def criacaoDePersonagem(self):
        self.verSlots()
        print("Insira o numero do slot de personagem que você deseja utilizar: ")

        myInput = [False, False, False]
        myInput[0] = int(input())
        if myInput[0] > 3:
            print("Deve ser um numero de 0 a 3.")
            self.criacaoDePersonagem()
        else:
            print("Insira o nome do personagem que você deseja criar: ")
            myInput[1] = input()
            print("Insira a classe do seu personagem: (Guerreiro, Mago)")
            myInput[2] = input()
            if myInput[2] == "Guerreiro" or myInput[2] == "Mago":
                self.personagens[myInput[0]] = Personagem(myInput[1], myInput[2])
                
            else:
                print("Insira uma classe valida!")
                self.criacaoDePersonagem()

        self.verSlots()

        myInput = [False, False, False]
        print("Você deseja criar outro personagem? (s,n)")
        myInput[0] = input()

        if myInput[0] == "s":
            self.criacaoDePersonagem()
        else:
            return 0


    def verSlots(self):
        for x in range(0,4):
            if self.personagens[x] == False:
                print("O Slot de Personagem", x, "Está Vazio!")
            else:
                print("Slot:", x, "Está Ocupado por:", self.personagens[x].nome, "Classe:", self.personagens[x].classe, "Nivel:", self.personagens[x].nivel)


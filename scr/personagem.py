class Personagem: #Classe de Objeto

    def __init__(self, nome, classe):#Construtor
        self.nome = nome
        self.classe = classe
        self.hp = 0
        self.hpMax = 0
        self.mp = 0
        self.forc = 0
        self.des = 0
        self.con = 0
        self.int = 0
        self.sab = 0
        self.car = 0
        self.xp = 0
        self.ca = 0
        self.nivel = 0
        self.dadoDeVida = 0
        self.dadoDeVidaQ = 0
        self.listaSkills = []
        self.equipamento = ["Armadura", "Arma"]
        self.inventario = []
        self.danoBase = 0

        if self.classe == "Guerreiro":
            self.forc = 3
            self.des = 1
            self.con = 2
            self.int = -1
            self.sab = 1
            self.car = 0
            self.dadoDeVida = 10
            self.hpMax = (self.dadoDeVida + self.con) 
            self.hp = self.hpMax
            self.nivel = 1
            self.ca = (10+self.des)
            self.dadoDeVidaQ = self.nivel
            self.listaSkills.append("Surto de açao")
            self.equipamento[0] = "Cota de malha"
            self.equipamento[1] = "Espada Grande"
            self.listaSkills.append("Pocao de vida")
            self.equipamentoManager()

        elif self.classe == "Mago":
            self.forc = -1
            self.des = 1
            self.con = 1
            self.int = 3
            self.sab = 2
            self.car = 0
            self.dadoDeVida = 6
            self.hpMax = (self.dadoDeVida + self.con) 
            self.hp = self.hpMax
            self.nivel = 1
            self.ca = (10+self.des)
            self.dadoDeVidaQ = self.nivel
            self.listaSkills.append("Raio de fogo")
            self.equipamento[0] = ""
            self.equipamento[1] = "Adaga"
            self.listaSkills.append("Pocao de vida")
            self.equipamentoManager()


        self.verificarHP()

    def setHP(self, hp):
        self.hp = hp
        self.verificarHP()
    
    def getHP(self):
        return self.hp

    def equipamentoManager(self):
        if self.equipamento[0] == "Cota de malha": #0 - Armadura
            self.ca = 16
        if self.equipamento[1] == "Espada Grande": #1 = Arma
            self.danoBase = 12
        if self.equipamento[1] == "Adaga":
            self.danoBase = 4


    def descansoCurto(self):
        self.hp += (self.hpMax/2)
        self.hp = round(self.hp)
        self.verificarHP

    def verificarHP(self):
        if self.hp > self.hpMax:
            self.hp = self.hpMax
        
    


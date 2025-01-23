class individuo():
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")
    
    def dizer_adeus(self):
        print(f"Até mais!")


class Humano(individuo):
    def __init__(self, nome, idade, especie, nacionalidade,sh_id):
        super().__init__(nome, idade, especie)
        self.nacionalidade = nacionalidade
        self.n_identificador = sh_id

    def dizer_nacionalidade(self):
        print(f"Eu sou {self.nacionalidade}")

class Cachorro(individuo):
    def __init__(self, nome, idade, especie, raca, tamanho_pelo):
        super().__init__(nome, idade, especie)
        self.raca = raca
        self.tamanho_pelo = tamanho_pelo

    def dizer_raca(self):
        print(f"Eu sou um cachorro da raça {self.raca}")

class Empresa(individuo):
    def __init__(self, nome, idade, especie, cnpj, ramo):
        super().__init__(nome, idade, especie)
        self.cnpj = cnpj
        self.ramo = ramo

    def dizer_cnpj(self):
        print(f"Meu CNPJ é {self.cnpj}")

class Masculino(Humano):
    def __init__(self, nome, idade, especie, nacionalidade, sh_id, barba):
        super().__init__(nome, idade, especie, nacionalidade, sh_id)
        self.barba = barba

    def tem_barba(self):
        if self.barba == True:
            print(f"Eu tenho barba")
        else:
            print(f"Eu não tenho barba")
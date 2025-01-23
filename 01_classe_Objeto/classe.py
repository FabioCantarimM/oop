
class Usuario:
    def __init__(self):
        self.__nome = None
        self.__email = None
        self.__senha = None
    
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_senha(self, senha):
        if len(senha) < 6:
            print("Senha muito curta")
        if len(senha) > 12:
            print("Senha muito longa")
        self.__senha = senha

    def get_senha(self):
        print(self.__senha)

    def saudacao(self):
        print(f"Olá, meu nome é {self.__nome}")

    def get_email(self):
        print(self.__email) 
    
    def logar(self):
        if self.__senha == "123456":
            print(f"Você está logado como {self.email}")
        else:
            print("Senha incorreta")

    def log_geral(self, nome, email, senha):
        print(f"O usuário {nome} está logado com o email {email} e senha {senha}")

    def solicitar_alteracao_senha(self, senha):
        self._alterar_senha(senha)

    def _alterar_senha(self, senha):
        self.__senha = senha

pessoa1 = Usuario()
pessoa1.set_nome(nome="João")
pessoa1.set_email(email="joao@a.com")
pessoa1.set_senha(senha="123")
pessoa1.saudacao()
pessoa1.get_email()
pessoa1.logar()

pessoa1.log_geral("João", "joao@a.com", "12356")
pessoa1.log_geral(nome="Pedro", senha="abcdef", email="pedro@abc.com")

pessoa2  = Usuario()
pessoa3  = Usuario()
pessoa4  = Usuario()
pessoa5  = Usuario()
pessoa6  = Usuario()


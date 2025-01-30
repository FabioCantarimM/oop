# 1. Variáveis e Tipos de Dados
# Variáveis são usadas para armazenar dados.
# Python é uma linguagem de tipagem dinâmica, ou seja, o tipo da variável é inferido automaticamente.

# Números inteiros
idade = 25
print("Idade:", idade)

# Números de ponto flutuante
altura = 1.75
print("Altura:", altura)

# Strings (texto)
nome = "João"
print("Nome:", nome)

# Booleanos (True ou False)
tem_carro = True
print("Tem carro?", tem_carro)

# 2. Operadores
# Operadores são usados para realizar operações em variáveis.

# Operadores aritméticos
soma = 10 + 5
subtracao = 10 - 5
multiplicacao = 10 * 5
divisao = 10 / 5
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

# Operadores de comparação
igual = (10 == 5)
diferente = (10 != 5)
maior_que = (10 > 5)
menor_que = (10 < 5)
print("10 é igual a 5?", igual)
print("10 é diferente de 5?", diferente)
print("10 é maior que 5?", maior_que)
print("10 é menor que 5?", menor_que)

# 3. Estruturas de Controle
# Estruturas de controle permitem que você tome decisões e repita ações.

# Condicional if-elif-else
if idade > 18:
    print(nome, "é maior de idade.")
elif idade == 18:
    print(nome, "tem exatamente 18 anos.")
else:
    print(nome, "é menor de idade.")

# Loop for
print("Contando de 1 a 5:")
for i in range(1, 6):
    print(i)

# Loop while
contador = 0
print("Contando até 5 com while:")
while contador < 5:
    print(contador)
    contador += 1

# 4. Funções
# Funções são blocos de código reutilizáveis que realizam uma tarefa específica.

def saudacao(nome):
    return "Olá, " + nome + "!"

mensagem = saudacao("Maria")
print(mensagem)

# 5. Listas
# Listas são coleções ordenadas e mutáveis de itens.

frutas = ["maçã", "banana", "laranja"]
print("Frutas:", frutas)

# Acessando elementos
print("Primeira fruta:", frutas[0])

# Adicionando elementos
frutas.append("uva")
print("Frutas após adicionar uva:", frutas)

# Removendo elementos
frutas.remove("banana")
print("Frutas após remover banana:", frutas)

# 6. Dicionários
# Dicionários são coleções de pares chave-valor.

pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "São Paulo"
}
print("Dicionário pessoa:", pessoa)

# Acessando valores
print("Nome da pessoa:", pessoa["nome"])

# Adicionando novos pares chave-valor
pessoa["profissao"] = "Engenheiro"
print("Dicionário após adicionar profissão:", pessoa)

# 7. Classes e Objetos
# Classes são modelos para criar objetos, que são instâncias das classes.

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        if self.especie == "cachorro":
            return "Au Au!"
        elif self.especie == "gato":
            return "Miau!"
        else:
            return "Som desconhecido."

# Criando objetos
cachorro = Animal("Rex", "cachorro")
gato = Animal("Mimi", "gato")

print(cachorro.nome, "faz:", cachorro.fazer_som())
print(gato.nome, "faz:", gato.fazer_som())

# 8. Tratamento de Exceções
# O tratamento de exceções permite lidar com erros de forma controlada.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
finally:
    print("Bloco finally sempre é executado.")

# 9. Módulos e Bibliotecas
# Módulos são arquivos Python que contêm funções e classes reutilizáveis.
# Bibliotecas são coleções de módulos.

import math

# Usando uma função da biblioteca math
raiz_quadrada = math.sqrt(25)
print("Raiz quadrada de 25:", raiz_quadrada)

# 10. Compreensão de Listas
# Compreensão de listas é uma forma concisa de criar listas.

numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros]
print("Quadrados dos números:", quadrados)
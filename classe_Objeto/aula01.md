# **Aprofundando em Classe e Objeto**

Uma **classe** é uma estrutura que define os atributos (dados) e métodos (funções) que um objeto dessa classe terá. Um **objeto** é uma instância de uma classe, ou seja, uma entidade concreta baseada no "molde" fornecido pela classe.

---

## **Detalhes Importantes sobre Classe e Objeto**

### 1. **Definição de Classe**
   - As classes são definidas com a palavra-chave `class`.
   - O nome da classe segue a convenção `CamelCase` (primeira letra maiúscula).
   - A classe pode conter um **construtor** (`__init__`), atributos e métodos.

   ```python
   class Pessoa:
       pass  # Classe vazia
   ```

### 2. **Criação de Objeto**
   - Para criar um objeto, chamamos o nome da classe como se fosse uma função.
   - O Python chama automaticamente o método especial `__init__` (se ele existir) ao criar um objeto.

   ```python
   # Criando uma classe básica
   class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome  # Atributo de instância
           self.idade = idade

   # Criando um objeto
   pessoa1 = Pessoa("João", 25)
   pessoa2 = Pessoa("Ana", 30)

   print(pessoa1.nome)  # João
   print(pessoa2.idade)  # 30
   ```

---

## **Atributos**

Os **atributos** são as características de um objeto. Eles podem ser:

### 1. **Atributos de Instância**
   - Pertencem a cada objeto individualmente.
   - Definidos dentro do método `__init__` ou diretamente no objeto.

   ```python
   class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome  # Atributo de instância
           self.idade = idade

   pessoa = Pessoa("Carlos", 40)
   print(pessoa.nome)  # Carlos
   ```

### 2. **Atributos de Classe**
   - São compartilhados entre todos os objetos de uma classe.
   - Definidos fora de métodos, dentro do corpo da classe.

   ```python
   class Pessoa:
       especie = "Humano"  # Atributo de classe

       def __init__(self, nome):
           self.nome = nome  # Atributo de instância

   p1 = Pessoa("Lucas")
   p2 = Pessoa("Maria")

   print(p1.especie)  # Humano
   print(p2.especie)  # Humano

   # Modificando o atributo de classe
   Pessoa.especie = "Homo Sapiens"
   print(p1.especie)  # Homo Sapiens
   print(p2.especie)  # Homo Sapiens
   ```

---

## **Métodos**

Os métodos definem os comportamentos de uma classe e são sempre associados a um objeto.

### Métodos mais usados:

### 1. **Métodos de Instância**
   - Operam nos atributos do objeto.
   - Sempre recebem o parâmetro `self`, que referencia o próprio objeto.

   ```python
   class Pessoa:
       def __init__(self, nome, idade):
           self.nome = nome
           self.idade = idade

       def apresentar(self):
           return f"Olá, eu sou {self.nome} e tenho {self.idade} anos."

   pessoa = Pessoa("Lucas", 20)
   print(pessoa.apresentar())  # Olá, eu sou Lucas e tenho 20 anos.
   ```

### 2. **Métodos de Classe**
   - Operam nos atributos de classe.
   - Usam o decorador `@classmethod` e recebem o parâmetro `cls`, que referencia a classe.

   ```python
   class Pessoa:
       especie = "Humano"

       @classmethod
       def mudar_especie(cls, nova_especie):
           cls.especie = nova_especie

   Pessoa.mudar_especie("Ciborgue")
   print(Pessoa.especie)  # Ciborgue
   ```

### 3. **Métodos Estáticos**
   - Não dependem de nenhum atributo de instância ou de classe.
   - Usam o decorador `@staticmethod`.

   ```python
   class Matematica:
       @staticmethod
       def soma(a, b):
           return a + b

   print(Matematica.soma(3, 5))  # 8
   ```

---

## **Modificadores de Acessibilidade**

Os atributos e métodos podem ter diferentes níveis de visibilidade:

### 1. **Público**
   - Qualquer parte do código pode acessá-lo.

   ```python
   class Pessoa:
       def __init__(self, nome):
           self.nome = nome  # Público

   pessoa = Pessoa("João")
   print(pessoa.nome)  # João
   ```

### 2. **Protegido**
   - Indicado por um `_` (underscore).
   - É uma convenção para indicar que o atributo/método não deve ser acessado diretamente.

   ```python
   class Pessoa:
       def __init__(self, nome):
           self._nome = nome  # Protegido

   pessoa = Pessoa("Maria")
   print(pessoa._nome)  # Maria (acessível, mas desencorajado)
   ```

### 3. **Privado**
   - Indicado por `__` (dois underscores).
   - Não pode ser acessado diretamente fora da classe.

   ```python
   class Pessoa:
       def __init__(self, nome):
           self.__nome = nome  # Privado

   pessoa = Pessoa("José")
   # print(pessoa.__nome)  # AttributeError: 'Pessoa' object has no attribute '__nome'
   ```

   Para acessar atributos privados, usamos **métodos getters e setters**.

---

## **Exemplo Completo: Criando uma Classe Completa**

```python
class Pessoa:
    especie = "Humano"  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade

    def apresentar(self):  # Método de instância
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

    @classmethod
    def mudar_especie(cls, nova_especie):
        cls.especie = nova_especie

    @staticmethod
    def boas_vindas():
        return "Bem-vindo à classe Pessoa!"

# Usando a classe
print(Pessoa.boas_vindas())  # Método estático

pessoa1 = Pessoa("Ana", 28)
print(pessoa1.apresentar())  # Olá, meu nome é Ana e tenho 28 anos.

Pessoa.mudar_especie("Homo Sapiens")
print(Pessoa.especie)  # Homo Sapiens
```

Esse aprofundamento cobre a **definição de classe**, **atributos**, **métodos** e as práticas mais comuns.

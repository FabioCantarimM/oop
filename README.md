**Introdução à Programação Orientada a Objetos (OOP)**
------------------------------------------------------

A OOP é um paradigma de programação que organiza o código em torno de **objetos**, que combinam dados (**atributos**) e comportamentos (**métodos**). Em Python, tudo é tratado como um objeto, e a OOP é amplamente utilizada por sua clareza e flexibilidade.

### **Tópicos Principais**

1.  **Classe e Objeto**
    
2.  **Atributos e Métodos**
    
3.  **Encapsulamento**
    
4.  **Herança**
    
5.  **Polimorfismo**
    

### **1\. Classe e Objeto**

*   **Classe**: É como um molde ou plano para criar objetos.
    
*   **Objeto**: É uma instância de uma classe.
    

`# Criando uma classe  class Pessoa:      pass  # Criando um objeto da classe  pessoa1 = Pessoa()  print(type(pessoa1))  #` 

### **2\. Atributos e Métodos**

*   **Atributos**: São dados armazenados dentro de objetos (ex.: nome, idade).
    
*   **Métodos**: São funções definidas dentro de uma classe para manipular atributos ou realizar ações.
    

`   class Pessoa:      def __init__(self, nome, idade):          self.nome = nome  # Atributo          self.idade = idade  # Atributo      def apresentar(self):  # Método          print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")  # Criando um objeto  pessoa1 = Pessoa("João", 30)  pessoa1.apresentar()  # Olá, meu nome é João e tenho 30 anos.   `

### **3\. Encapsulamento**

O encapsulamento protege os dados de um objeto contra acessos indevidos, permitindo controlar a visibilidade de atributos e métodos.

*   **Público**: Acessível de qualquer lugar (ex.: self.nome).
    
*   **Protegido**: Sinalizado com um \_ (ex.: self.\_idade).
    
*   **Privado**: Sinalizado com \_\_ (ex.: self.\_\_salario).
    

`   class ContaBancaria:      def __init__(self, titular, saldo):          self.titular = titular  # Público          self._saldo = saldo  # Protegido      def depositar(self, valor):          self._saldo += valor      def _mostrar_saldo(self):  # Método protegido          return f"Saldo: R${self._saldo}"  # Usando a classe  conta = ContaBancaria("Maria", 500)  conta.depositar(200)  print(conta._mostrar_saldo())  # Saldo: R$700   `

### **4\. Herança**

A herança permite que uma classe herde atributos e métodos de outra classe, promovendo o reuso de código.

`   class Animal:      def __init__(self, nome):          self.nome = nome      def falar(self):          pass  # Método genérico a ser sobrescrito  class Cachorro(Animal):      def falar(self):          return f"{self.nome} diz: Au au!"  class Gato(Animal):      def falar(self):          return f"{self.nome} diz: Miau!"  # Criando objetos  dog = Cachorro("Rex")  cat = Gato("Luna")  print(dog.falar())  # Rex diz: Au au!  print(cat.falar())  # Luna diz: Miau!   `

### **5\. Polimorfismo**

O polimorfismo permite que diferentes objetos usem o mesmo método de maneira específica para cada classe.

`   animais = [Cachorro("Rex"), Gato("Luna")]  for animal in animais:      print(animal.falar())  # Rex diz: Au au!  # Luna diz: Miau!   `

### **Resumo**

A OOP é um poderoso paradigma que facilita:

*   **Reutilização de código**: Herança e polimorfismo.
    
*   **Organização**: Código modular com classes.
    
*   **Segurança**: Controle de acesso com encapsulamento.
    

Se quiser, podemos aprofundar algum desses tópicos ou criar mais exemplos práticos! 🚀
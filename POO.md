# **Programação Orientada a Objetos (POO) com Python**

## **1. Fundamentos da POO**
A **Programação Orientada a Objetos (POO)** organiza o código para representar conceitos do mundo real. Ela facilita a reutilização de código e a manutenção de sistemas complexos.

### **1.1 Paradigmas de Programação**
Existem vários paradigmas de programação:
- **Procedural**: Baseado em sequências de comandos (Ex: C, Pascal).
- **POO**: Código estruturado em **objetos** que combinam **dados** e **comportamentos** (Ex: Python, Java, C++).
- **Funcional**: Computação baseada na avaliação de funções matemáticas (Ex: Haskell, Lisp).
- **Lógico**: Baseado em regras lógicas (Ex: Prolog).
- **Declarativo**: Define **o que** deve ser feito, sem especificar **como** (Ex: SQL, HTML).

### **1.2 Abstração**
A **abstração** foca apenas nos aspectos essenciais de um objeto, ocultando detalhes desnecessários.

#### **Exemplo de Classe Abstrata**
```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        pass
```
Essa classe abstrata obriga subclasses a implementar o método `mover()`.

---

## **2. Conceitos de POO em Python**

### **2.1 Classes e Objetos**
Uma **classe** é um molde para criar objetos. Um **objeto** é uma instância de uma classe.

#### **Exemplo de Classe e Objeto**
```python
class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor

meu_carro = Carro("Ferrari", "488", "vermelho")
print(meu_carro.marca)  # Saída: Ferrari
```

### **2.2 Métodos e Atributos**
- **Atributos**: Características do objeto.
- **Métodos**: Ações que o objeto pode executar.

#### **Exemplo de Método**
```python
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Carro: {self.marca} {self.modelo}"

carro1 = Carro("Toyota", "Corolla")
print(carro1.descricao())  # Saída: Carro: Toyota Corolla
```

### **2.3 Atributos de Instância vs. Classe**
- **Atributos de Instância**: Específicos para cada objeto.
- **Atributos de Classe**: Compartilhados por todas as instâncias.

```python
class Carro:
    rodas = 4  # Atributo de classe

    def __init__(self, marca):
        self.marca = marca  # Atributo de instância

print(Carro.rodas)  # Saída: 4
```

---

## **3. Princípios da POO**

### **3.1 Encapsulamento**
Protege os dados de acesso externo.

#### **Exemplo com Atributos Privados**
```python
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def consultar_saldo(self):
        return f"Saldo: R${self.__saldo:.2f}"

conta = ContaBancaria("Maria", 1000)
print(conta.consultar_saldo())  # Saída: Saldo: R$1000.00
```

### **3.2 Herança**
Permite que uma classe herde atributos e métodos de outra.

#### **Exemplo de Herança**
```python
class Veiculo:
    def __init__(self, marca):
        self.marca = marca

    def info(self):
        return f"Veículo da marca {self.marca}"

class Carro(Veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

carro = Carro("Toyota", "Corolla")
print(carro.info())  # Saída: Veículo da marca Toyota
```

### **3.3 Polimorfismo**
Métodos podem ser sobrescritos em subclasses.

```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

animais = [Cachorro(), Gato()]
for animal in animais:
    print(animal.fazer_som())  # Saída: Au Au! Miau!
```

---







# Programação Orientada a Objetos em Python  

# Sumário Interativo
- [Programação Orientada a Objetos em Python](#programação-orientada-a-objetos-em-python)
  - [1. Conceito Central](#1-conceito-central)
  - [2. Classes e Objetos](#2-classes-e-objetos)
  - [3. Encapsulamento e Propriedades](#3-encapsulamento-e-propriedades)
  - [4. Métodos de Classe e Estáticos](#4-métodos-de-classe-e-estáticos)
  - [5. Herança](#5-herança)
  - [6. Polimorfismo](#6-polimorfismo)
  - [7. Composição](#7-composição)
  - [8. Dunder (Magic) Methods](#8-dunder-magic-methods)
  - [9. Boas Práticas de Projeto](#9-boas-práticas-de-projeto)
  - [10. Projeto de Exemplo: Sistema de Biblioteca (Resumo)](#10-projeto-de-exemplo-sistema-de-biblioteca-resumo)

- [Lista de Exercícios de POO](#lista-de-exercícios-de-poo)

- [Referências](#referências)


## Paradigma de Programação

Um **paradigma de programação** descreve como estruturar programas. Existem vários paradigmas, como:

- **Procedural:** Enfatiza uma sequência de instruções, onde o programa é dividido em funções (exemplo: C).  
- **Orientado a Objetos:** Foca em objetos que combinam dados e comportamentos (exemplos: Java, C++, Python).  
- **Funcional:** Trata o código como funções matemáticas puras, evitando mudanças de estado (exemplo: Haskell).  
- **Lógico:** Baseia-se em declarações lógicas e regras para derivar conclusões (exemplo: Prolog).  
- **Declarativo:** Especifica o que o programa deve fazer, sem detalhar como (exemplos: SQL, HTML).

---

## Introdução à Programação Orientada a Objetos

A Programação Orientada a Objetos (POO) organiza o desenvolvimento de software em torno de **objetos**, representando entidades do mundo real ou conceitos abstratos.
Essa abordagem melhora a **Legibilidade**, **Reusabilidade** e **Manutenção** do código.

---

## 1. Abstração

O primeiro passo para se programar utilizando POO é abstrair as informações necessárias para a utilização do nosso código.
A **abstração** consiste em representar um objeto real apenas com as informações necessárias ao contexto do sistema, ignorando detalhes supérfluos. 

Por exemplo:

<img src="images/abstraction.jpg" alt="Abstração" width="500">

- **Abstração Visual de um Carro**: Pode-se representar cor, modelo e forma, omitindo detalhes de engenharia.  

- **Abstração Funcional de um Carro**: Foca em características mecânicas, como sistema de freios, motor e embreagem, se o objetivo for simular o desempenho.

Ao definir quais informações são mais relevantes, reduzimos a complexidade e facilitamos a manutenção.

---

## 2. Classe e Objeto

A **Classe** é o “molde” de um objeto, ela descreve quais dados (atributos) e comportamentos (métodos) o objeto deve ter.

O **Objeto** é a realização concreta de uma classe, tendo seu próprio estado e podendo executar comportamentos definidos na classe.

<img src="images/class.jpg" alt="classe" width="500">

No caso de um carro, a Classe é o molde que descreve detalhadamente as características e comportamentos que o carro pode realizar.

---

## 3. Atributos

**Atributos** são as características que armazenam o estado de um objeto. 

<img src="images/atributes.jpg" alt="Atributos" width="500">

No exemplo de um carro, os atributos poderiam ser “cor”, “modelo”, "ano".

---

## 4. Métodos

Os **Métodos** são funções que definem os comportamentos de um objeto. 


Por exemplo, um carro pode ter métodos como “acelerar”, “frear” ou “ligarMotor”, que manipulam ou consultam os atributos.

---

### 5. Instância e Instanciação

Após definirmos a Classe, elementos e métodos do nosso objetos,  precisamos criar ele, para isso usamos a instanciação

- **Instância**: É o objeto propriamente dito. Para a classe “Carro” um *Carro vermelho 2024* é sua instância.  
- **Instanciação**: É o processo de criar a instância na memória.

<img src="images/instantiation.jpg" alt="Instanciação" width="500">

O molde (classe) descreve como o carro deve ser, mas o carro de verdade (instância) só existe após a construção (instanciação).

---

### Classes e Objetos em Python


```python
# 1. Definição da Classe
class Student:
    # 2. Método Construtor (__init__)
    def __init__(self, name):
        # 3. Atribuição de Atributo
        self.name = name

# 4. Criação do Objeto (Instanciação)
student_instance = Student("Diego") #

# 5. Acesso e Impressão do Atributo
print(student_instance.name)
```

O código define uma classe Student que funciona como um molde para criar objetos de estudantes. 

O método __init__ é o construtor, executado automaticamente sempre que um novo objeto é criado, e sua função é inicializar os atributos do objeto. 

O parâmetro self representa a instância específica do objeto que está sendo criada, permitindo que cada objeto Student tenha seus próprios dados. 

Ao executar Student("Diego"), um novo objeto é criado, e o método __init__ usa self para atribuir o valor "Diego" ao seu atributo name, que é então acessado e impresso na tela.

```python
class Student:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    def __str__(self):
        return f"Aluno: {self.name}, Média: {self.average():.2f}"

    def average(self):
        return sum(self.notes) / len(self.notes)


minhas_notas = [9.2, 8.5, 7.0]
aluno = Student("Diego", minhas_notas)

print(aluno)
```

No código a cima implementamos o método average() que calcula a média das notes (em uma lista), e usamos o metodo __str__ formatando a saída para impressão. Assim, aluno = Student("Diego", minhas_notas) cria um objeto que "sabe" seu nome, suas notas e como calcular sua própria média.

__str__: Para usuários. É o que aparece com print(). O objetivo é ser legível e amigável.
print(aluno) chama aluno.__str__().

__repr__: Para desenvolvedores. É usado para depuração (debug). O objetivo é ser uma representação técnica e inequívoca do objeto, idealmente um código que possa recriá-lo.
repr(aluno) chama aluno.__repr__().

Regra principal: Se o __str__ não for definido, o print() usará o __repr__ no lugar dele.

**`@classmethod` e `@staticmethod`** são **decoradores** usados para definir métodos em classes Python que **não funcionam como métodos de instância** (que usam `self`).

---
### Decoradores de Classes

#### `@classmethod`

* O método recebe a **classe** como primeiro argumento, chamado de `cls`.
* Pode acessar e modificar atributos da classe.

Exemplo:

```python
class Pessoa:
    contador = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    @classmethod
    def criar_anonimo(cls):
        return cls("Anônimo")  # retorna uma nova instância da classe

    @classmethod
    def total(cls):
        return cls.contador
```

**Uso:**

```python
p1 = Pessoa("Diego")
p2 = Pessoa.criar_anonimo()
print(Pessoa.total())  # Saída: 2
```

---

### 🔹 `@staticmethod`

* O método **não recebe nem `self` nem `cls`**.
* É um método comum, apenas agrupado dentro da classe por organização.
* Não pode acessar nem modificar atributos da instância ou da classe.

#### Exemplo:

```python
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
```

**Uso:**

```python
print(Calculadora.somar(2, 3))  # Saída: 5
```

---

### Resumo Rápido

| Decorador       | Primeiro parâmetro | Acessa atributos de | Uso típico                            |
| --------------- | ------------------ | ------------------- | ------------------------------------- |
| `@classmethod`  | `cls`              | Classe              | Fábricas de objetos, contadores, etc. |
| `@staticmethod` | nenhum             | Nenhum              | Funções utilitárias ligadas à classe  |

Se quiser, posso gerar mais exemplos ou exercícios para fixar.

---


## Referências

## Documentação Oficial do Python
- https://docs.python.org/3/  
- https://docs.python.org/3/tutorial/modules.html  
- https://docs.python.org/3/py-modindex.html  
- https://docs.python.org/3/tutorial/errors.html#exceptions  
- https://docs.python.org/3/tutorial/classes.html  

## Tutoriais e Artigos Técnicos
- **TutorialsPoint** – Sintaxe Básica  
  - https://www.tutorialspoint.com/python/python_basic_syntax.htm  
- **Programiz** – Conversão de Tipos  
  - https://www.programiz.com/python-programming/type-conversion-and-casting  
- **Real Python**  
  - Variáveis: https://realpython.com/python-variables/  
  - Exceções: https://realpython.com/python-exceptions/  
  - Módulos e Pacotes: https://realpython.com/python-modules-packages/  
  - Lambda: https://realpython.com/python-lambda/  
  - POO: https://realpython.com/python3-object-oriented-programming/  
- **DataCamp** – Decorators  
  - https://www.datacamp.com/tutorial/decorators-python  
- **PythonBasics** – Decorators  
  - https://pythonbasics.org/decorators/  
- **TutorialsTeacher** – Magic (Dunder) Methods  
  - https://www.tutorialsteacher.com/python/magic-methods-in-python  

## W3Schools – Seção Python
- Página principal: https://www.w3schools.com/python/  
- Variáveis: https://www.w3schools.com/python/python_variables.asp  
- Listas: https://www.w3schools.com/python/python_lists.asp  
- Tuplas: https://www.w3schools.com/python/python_tuples.asp  
- Sets: https://www.w3schools.com/python/python_sets.asp  
- Dicionários: https://www.w3schools.com/python/python_dictionaries.asp  
- Inheritance: https://www.w3schools.com/python/python_inheritance.asp  
- Lambda: https://www.w3schools.com/python/python_lambda.asp  
- Iterators: https://www.w3schools.com/python/python_iterators.asp  

## Livros
- *Python Fluente* — Luciano Ramalho  

---

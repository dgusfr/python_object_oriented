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

## Introdução à Programação Orientada a Objetos

A Programação Orientada a Objetos (POO) organiza o desenvolvimento de software em torno de **objetos**, representando entidades do mundo real ou conceitos abstratos. Esse paradigma torna o código mais intuitivo e modular, pois cada objeto encapsula dados e comportamentos de maneira clara.

---

### 1. Paradigma de Programação

Um **paradigma de programação** descreve como resolver problemas e estruturar programas. Existem vários paradigmas, como:

- **Procedural:** Enfatiza uma sequência de instruções, onde o programa é dividido em funções (exemplo: C).  
- **Orientado a Objetos:** Foca em objetos que combinam dados e comportamentos (exemplos: Java, C++, Python).  
- **Funcional:** Trata o código como funções matemáticas puras, evitando mudanças de estado (exemplo: Haskell).  
- **Lógico:** Baseia-se em declarações lógicas e regras para derivar conclusões (exemplo: Prolog).  
- **Declarativo:** Especifica o que o programa deve fazer, sem detalhar como (exemplos: SQL, HTML).

---

### 3. Por que Usar POO?

- **Legibilidade**: O código é organizado em “blocos” que correspondem a entidades do problema (por exemplo, “Carro”, “Cliente” etc.).  
- **Reusabilidade**: As classes podem ser aproveitadas em diversas partes do sistema ou em outros projetos.  
- **Manutenção Facilitada**: Alterações são centralizadas em cada classe, facilitando testes e correções.  

*Exemplo de abordagem:*  
Em um sistema que calcula a área de triângulos, a abordagem procedural exigiria várias variáveis e funções separadas para cada triângulo. Com POO, podemos ter uma classe “Triângulo” que agrupe os dados (lados) e comportamentos (cálculo da área) em um só lugar, tornando o código mais organizado.

---

### 4. Abstração

A **abstração** consiste em representar um objeto real apenas com as informações necessárias ao contexto do sistema, ignorando detalhes supérfluos. Por exemplo:

<img src="images/abstraction.jpg" alt="Abstração" width="600">

- **Abstração Visual de um Carro**: Pode-se representar cor, modelo e forma, omitindo detalhes de engenharia.  
- **Abstração Funcional de um Carro**: Foca em características mecânicas, como sistema de freios, motor e embreagem, se o objetivo for simular o desempenho.

Ao definir quais informações são mais relevantes, os atributos e métodos de uma classe variam conforme o nível de detalhe escolhido. Isso ajuda a reduzir a complexidade e a facilitar a manutenção.

---

### 5. Instância e Instanciação

- **Instância**: É o objeto propriamente dito. Se a classe “Carro” é o “molde”, então um *Carro vermelho 2024* é uma instância específica daquele molde.  
- **Instanciação**: É o processo de criar a instância na memória. Em Java, quando usamos um operador para criar o objeto, esse espaço é alocado na memória e uma referência é retornada para ser usada no programa.

<img src="images/instantiation.jpg" alt="Instanciação" width="600">

Visualize como se estivéssemos construindo uma carro: o molde (classe) descreve como o carro deve ser, mas o carro de verdade (instância) só existe após a construção (instanciação).

---

## Classe, Objeto, Atributos e Métodos

A **POO** baseia-se em quatro conceitos essenciais:

1. **Classe**  
   É o “molde” de um objeto. Descreve quais dados (atributos) e comportamentos (métodos) o objeto deve ter.

2. **Objeto**  
   É a realização concreta de uma classe, criado em tempo de execução. Cada objeto tem seu próprio estado e pode executar comportamentos definidos na classe.

<img src="images/class.jpg" alt="ClasseJava" width="600">

3. **Atributos**  
   São as características que armazenam o estado de um objeto. No exemplo de um carro, os atributos poderiam ser “cor”, “modelo”, “velocidade”.

<img src="images/atributes.jpg" alt="Atributos" width="600">

4. **Métodos**  
   São funções que definem os comportamentos de um objeto. Por exemplo, um carro pode ter métodos como “acelerar”, “frear” ou “ligarMotor”, que manipulam ou consultam os atributos.

---

### Exemplo Conceitual 

- **Classe**: “Carro”
  - **Atributos**: cor, modelo, velocidadeAtual
  - **Métodos**: acelerar(), frear(), ligarMotor()

- **Objeto**: Carro específico (por exemplo, um carro vermelho, modelo “XYZ”, velocidade atual de X km/h)
  - Quando chamamos `acelerar()`, o objeto altera o valor do atributo “velocidadeAtual”
  - Se chamamos `frear()`, a velocidade diminui.

Nesse esquema, a classe descreve o que o carro pode ter e fazer; o objeto é um carro individual em uso. Os atributos guardam os dados (velocidade, cor), e os métodos definem os comportamentos (acelerar, frear).

---
---

## 1. Conceito Central  
POO modela o software em **objetos** que unem dados e comportamentos. Cada objeto pertence a uma **classe**, o molde que define atributos e métodos. Essa abordagem reflete o mundo real e simplifica a evolução do código.

---

## 2. Classes e Objetos  

### Introdução Teórica  
Uma classe define atributos (estado) e métodos (ações). Ao instanciar a classe, você obtém um objeto com seu próprio estado.

### Exemplo Prático  
```python
class Pessoa:
    especie = "Humano"          # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome        # atributo de instância
        self.idade = idade

    def apresentar(self):
        return f"Sou {self.nome}, tenho {self.idade} anos."

p1 = Pessoa("Ana", 30)
print(p1.apresentar())
```

### Explicação

`especie` é compartilhado por todas as instâncias. `self.nome` e `self.idade` pertencem apenas ao objeto criado. O método `apresentar` usa esses atributos para construir a mensagem.

### Aplicações no Mundo Real

Modelar usuários, produtos e pedidos em sistemas web, encapsulando lógica de negócio dentro de cada classe.

### Exercício

Implemente a classe `Carro` com marca, modelo e ano. Adicione método `idade()` que devolve quantos anos o carro possui.

---

## 3. Encapsulamento e Propriedades

### Introdução Teórica

Encapsular é ocultar detalhes internos. Use um sublinhado para indicar atributo “privado” e controle o acesso com `@property`.

### Exemplo Prático

```python
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo     # protegido

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
```

### Explicação

`_saldo` não deve ser modificado fora da classe. A propriedade expõe apenas leitura. A regra de depósito garante integridade.

### Aplicações

Validação de dados sensíveis, como senhas ou limites de crédito.

### Exercício

Adicione a `Conta` o método `sacar`, validando se há saldo suficiente.

---

## 4. Métodos de Classe e Estáticos

### Introdução Teórica

`@classmethod` recebe a classe como primeiro parâmetro (`cls`). Útil para fábricas de objetos. `@staticmethod` é uma função utilitária ligada à classe, mas sem acesso a `cls` nem `self`.

### Exemplo Prático

```python
class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5/9)

    @staticmethod
    def kelvin_para_celsius(k):
        return k - 273.15
```

---

## 5. Herança

### Introdução Teórica

Uma classe filha herda atributos e métodos da classe pai, reduzindo duplicação e permitindo especialização.

### Exemplo Prático

```python
class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        base = super().apresentar()
        return f"{base} e ganho R${self.salario}."
```

### Explicação

`super()` chama implementações da classe pai. O método é sobrescrito para incluir o salário.

### Exercício

Crie `Gerente` herdando de `Funcionario` e acrescente bônus anual calculado como 10 % do salário.

---

## 6. Polimorfismo

### Introdução Teórica

Objetos diferentes podem responder à mesma mensagem. Em Python, o polimorfismo é natural: se o método existe, ele será chamado, independentemente do tipo.

### Exemplo Prático

```python
def apresentar_entidade(entidade):
    print(entidade.apresentar())

apresentar_entidade(Funcionario("Bruno", 25, 3500))
apresentar_entidade(Pessoa("Carla", 40))
```

### Aplicações

Escrever código genérico que trabalha com qualquer objeto que respeite uma interface implícita.

---

## 7. Composição

### Introdução Teórica

Composição combina objetos para formar estruturas mais complexas e favorece reutilização sobre herança.

### Exemplo Prático

```python
class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco
```

A classe `Cliente` contém um objeto `Endereco`, delegando a ele responsabilidades de endereço.

---

## 8. Dunder (Magic) Methods

### Introdução Teórica

Dunder methods personalizam operadores e representações. Implementar `__add__`, `__len__`, `__repr__`, `__eq__` dá comportamento natural aos objetos.

### Exemplo Prático

```python
class Vetor:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, outro):
        return Vetor(self.x + outro.x, self.y + outro.y)

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def __repr__(self):
        return f"Vetor({self.x}, {self.y})"
```

---

## 9. Boas Práticas de Projeto

* Mantenha cada classe focada em uma única responsabilidade.
* Prefira composição quando a relação não for “é um”, mas “tem um”.
* Documente contratos públicos com docstrings.
* Escreva testes unitários para cada método crítico.

---

## 10. Projeto de Exemplo: Sistema de Biblioteca (Resumo)

Defina classes `Livro`, `Usuario`, `Emprestimo` e `Biblioteca`.
`Biblioteca` possui listas de livros e usuários, métodos para cadastrar, buscar e emprestar.
`Emprestimo` registra data de retirada e devolução, usando dunder `__repr__` para exibição clara.
Implemente validações no método `emprestar` para verificar disponibilidade.
Esse pequeno domínio mostra classes cooperando via composição, herança opcional para usuários especiais (Administrador).

---


# Lista de Exercícios de POO


## 1. Exercício 1 — Classe `Retângulo`

Crie uma classe `Retangulo` que receba base e altura no construtor.  
Implemente:

- Método `area()` que devolve a área.  
- Método `perimetro()` que devolve o perímetro.  
- Dunder `__repr__` para exibir `Retangulo(base=..., altura=...)`.

Escreva um script que leia dois retângulos, exiba área e perímetro de cada um e indique qual possui maior área.

---

## 2. Exercício 2 — Herança e Polimorfismo em `Veículo`

Crie a classe base `Veiculo` com atributo `velocidade`.  
Crie duas classes filhas:

- `Carro` com atributo adicional `portas`.  
- `Moto` com atributo adicional `cilindradas`.

Ambas devem sobrescrever o método `descrever()` herdado da classe pai para incluir seus detalhes.  
Escreva uma função `mostrar_info(veiculo)` que receba qualquer veículo e chame `descrever()`, demonstrando polimorfismo.

---

## 3. Exercício 3 — Dunder Methods em `Fracao`

Implemente a classe `Fracao` com numerador e denominador.  
Adicione:

- Validação para denominador diferente de zero.  
- `__add__`, `__sub__` e `__mul__` para somar, subtrair e multiplicar frações.  
- `__repr__` retornando `"Fracao(n/d)"`.  

Crie um script que leia duas frações do usuário e exiba os resultados das três operações.

---

## 4. Projeto — Sistema de Biblioteca Simplificado

**Objetivo**: modelar uma pequena biblioteca que gerencia livros e empréstimos.  

### Requisitos

1. **Classes principais**  
   - `Livro` → título, autor, ano, total de exemplares e exemplares disponíveis.  
   - `Usuario` → nome, e-mail e lista de livros emprestados.  
   - `Biblioteca` → coleções de livros e usuários.

2. **Métodos essenciais**  
   - `Biblioteca.adicionar_livro(livro)`  
   - `Biblioteca.cadastrar_usuario(usuario)`  
   - `Biblioteca.emprestar(titulo, usuario)` com validações de disponibilidade.  
   - `Biblioteca.devolver(titulo, usuario)` que atualiza status e datas.  

3. **Relatórios**  
   - Método para listar livros disponíveis ordenados por ano.  
   - Método para listar usuários e quantidade de livros emprestados.

4. **Extras sugeridos**  
   - Dunder `__repr__` para `Livro` e `Usuario`.  
   - Persistência simples em JSON para salvar e carregar dados.  
   - Tratamento de exceções para casos de livro inexistente ou usuário não cadastrado.

Implemente testes manuais em um arquivo `main.py` que:

1. Cadastre três livros e dois usuários.  
2. Realize dois empréstimos e uma devolução.  
3. Exiba os relatórios.

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

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

# POO com Pyhton

## Classes e Objetos 

A **Classe** é o "molde" de um objeto. Ela define um conjunto de atributos (dados) e métodos (comportamentos) que suas instâncias, os objetos, terão. O **Objeto** é a realização concreta de uma classe, uma instância específica que ocupa um espaço na memória e possui os atributos e comportamentos definidos pela classe.

**Exemplo de classe (`Restaurant`):**
Este código define o que *todo* restaurante terá: um nome, um tipo de cozinha e um menu, além de ações como adicionar itens a esse menu.

*models/restaurant.py*

```python
class Restaurant:
    def __init__(self, name, type_cuisine):
        self.name = name.title()
        self.type_cuisine = type_cuisine
```

**Criando um objeto (`coco_bambu`) a partir da classe `Restaurant`:**
Aqui, `coco_bambu` é o objeto, uma instância específica da classe `Restaurant`. Ele tem seu próprio nome ("Coco Bambu") e pode ter seu próprio cardápio, independente de outros objetos de restaurante que possam ser criados.

*app.py*

```python
from models.restaurant import Restaurant

# Instanciando (criando) um objeto da classe Restaurant
coco_bambu = Restaurant("Coco Bambu", "Frutos do Mar")

# O arquivo app.py instancia (cria) um objeto a partir da classe Restaurant
# e utiliza seus métodos para construir a lógica da aplicação.
```

---

<br>
<br>
<br>

___

## Decoradores

Decoradores em Python são funções que recebem outra função como argumento e retornam uma nova função com um comportamento modificado. Eles permitem adicionar funcionalidades antes ou depois da execução da função original, sem alterar seu código diretamente. São usados com a sintaxe **@decorador** acima da função que será modificada.

**Exemplo de decorador (`@property`):**
No nosso código, usamos o `@property` para transformar o método `price()` em um atributo. Isso nos permite acessar `item._price` de forma segura através de `item.price`, como se fosse uma variável pública, mas com a lógica de um método.

*models/menu/item\_menu.py*

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self._price = price # Atributo "protegido"

    @property
    def price(self):
        return self._price
```

### Dunder Methods (Métodos Mágicos)

Dunder (Double Underscore) Methods são métodos especiais com nomes que começam e terminam com dois underscores.

  * **`__init__`**: É o construtor da classe. Ele é chamado automaticamente quando um novo objeto é criado (instanciado) e serve para inicializar os atributos do objeto.

    *models/restaurant.py*

    ```python
    class Restaurant:
        def __init__(self, name, type_cuisine):
            self.name = name.title()
            self.type_cuisine = type_cuisine
            self._active = False
            self._menu = []
    ```

  * **`__str__` e `__repr__`**: Ambos criam representações em string de um objeto. 
  A convenção é que `__str__` seja para o usuário final (legível e informal), enquanto `__repr__` seja para o desenvolvedor (inequívoco, idealmente recriando o objeto). 
  Se `__str__` não for definido, o Python usará `__repr__` em seu lugar.

    *models/menu/item\_menu.py*

    ```python
    class MenuItem:
        # ... __init__ e @property price ...

        def __str__(self):
            # Usado quando você faz print(meu_objeto)
            return f"{self.name}: R$ {self.price:.2f}"

        def __repr__(self):
            # Usado para depuração ou ao inspecionar o objeto
            return f"MenuItem(name={self.name}, price={self.price})"
    ```

### Métodos de Classe, Estáticos e Propriedades

  * **`@staticmethod`**: É um método que pertence a uma classe, mas não tem acesso à instância (`self`) nem à classe (`cls`). Ele funciona como uma função comum que está organizada dentro do escopo da classe por razões de lógica. É usado para criar funções utilitárias que têm relação com a classe, mas não dependem de nenhum de seus dados.

    *Exemplo hipotético para `Restaurant`:*

    ```python
    class Restaurant:
        # ... outros métodos ...

        @staticmethod
        def business_hours():
            # Não precisa de 'self' ou 'cls', é apenas uma informação relacionada
            return "De segunda a sexta, das 8h às 22h."

    # Como usar:
    print(Restaurant.business_hours())
    ```

  * **`@classmethod`**: Este método recebe a classe como o primeiro argumento (`cls`) em vez da instância (`self`). É comumente usado para criar "fábricas" (factory methods), que são maneiras alternativas de construir objetos da classe.

    *Exemplo hipotético para `Restaurant`:*

    ```python
    class Restaurant:
        # ... outros métodos ...

        @classmethod
        def from_dict(cls, data):
            # 'cls' aqui é a própria classe Restaurant
            # Este método cria uma instância de restaurante a partir de um dicionário
            return cls(data['name'], data['type_cuisine'])

    # Como usar:
    restaurant_data = {'name': 'A Baianeira', 'type_cuisine': 'Baiana'}
    a_baianeira = Restaurant.from_dict(restaurant_data)
    ```

---

<br>
<br>
<br>

___

## Herança

Herança é um pilar da Programação Orientada a Objetos que permite que uma classe (chamada de classe filha ou subclasse) herde atributos e métodos de outra classe (classe mãe ou superclasse).

**Exemplo com as classes `MenuItem`, `Dish` e `Drink`:**

Primeiro, temos a classe mãe `MenuItem`, que define o que todo item do menu deve ter: um nome e um preço.

*models/menu/item\_menu.py*

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
```

Agora, criamos as classes filhas `Drink` e `Dish`. Elas herdam de `MenuItem` e, portanto, já possuem os atributos `name` e `price`. Usamos `super().__init__(name, price)` para chamar o construtor da classe mãe e garantir que esses atributos sejam inicializados. Em seguida, cada classe filha adiciona seus próprios atributos e métodos específicos.

*models/menu/drink.py*

```python
from models.menu.item_menu import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price):
        # Chama o construtor da classe mãe (MenuItem)
        super().__init__(name, price)
        # Adiciona um atributo específico da classe Drink
        self.type = "Bebida"
```

*models/menu/dish.py*

```python
from models.menu.item_menu import MenuItem

class Dish(MenuItem):
    def __init__(self, name, price):
        # Chama o construtor da classe mãe (MenuItem)
        super().__init__(name, price)
        # Adiciona um atributo específico da classe Dish
        self.type = "Prato"
```

Dessa forma, tanto `Drink` quanto `Dish` reutilizam a lógica de `MenuItem`, evitando a repetição de código e mantendo uma estrutura organizada. Um objeto `Drink`, por exemplo, terá acesso à propriedade `price` definida em `MenuItem` e ao atributo `type` definido em sua própria classe.

---

<br>
<br>
<br>

___

## Polimorfismo

**Polimorfismo** (do grego, "muitas formas") é a capacidade de objetos de diferentes classes responderem à mesma chamada de método, cada um de sua própria maneira. 

Em outras palavras, um mesmo método pode ter comportamentos diferentes dependendo da classe do objeto que o está executando. 

**Exemplo com `apply_discount`:**

A classe `MenuItem` define que todo item do menu *deve* ter um método `apply_discount`, mas não diz *como* ele funciona. 

As classes filhas, `Drink` e `Dish`, herdam essa obrigação e implementam o método de formas diferentes: 

`Drink` aplica um desconto de 5%, enquanto `Dish` aplica 3%. 

Isso é polimorfismo em ação: o mesmo método `apply_discount` se comporta de maneira distinta para cada tipo de objeto.

*drink.py*

```python
class Drink(MenuItem):
    # ...
    def apply_discount(self):
        # Implementação específica para Bebida: desconto de 5%
        self._price -= self._price * 0.05
```

*dish.py*

```python
class Dish(MenuItem):
    # ...
    def apply_discount(self):
        # Implementação específica para Prato: desconto de 3%
        self._price -= self._price * 0.03
```

-----

### Métodos Abstratos

Um **método abstrato** é um método declarado em uma classe mãe (chamada de Classe Base Abstrata ou ABC), mas que não possui implementação. 

Ao decorar um método com `@abstractmethod`, você **obriga** todas as classes filhas a implementarem sua própria versão daquele método. Se uma classe filha não o fizer, o Python gerará um erro, impedindo a criação de objetos daquela classe.

Uma classe que contém pelo menos um método abstrato não pode ser instanciada diretamente. Ela serve como um "contrato" ou um "molde", garantindo que todas as subclasses sigam uma estrutura específica.

**Quando usar:** Use métodos abstratos quando um comportamento é comum a todas as classes filhas, mas a implementação desse comportamento é tão específica para cada uma que não faz sentido definir uma lógica padrão na classe mãe. 

No nosso exemplo, todo `MenuItem` deve ter um desconto aplicável, mas o valor do desconto só faz sentido quando sabemos se é um `prato` ou uma `bebida`.

*models/menu/item\_menu.py*

```python
from abc import ABC, abstractmethod

# Ao herdar de ABC, a classe se torna uma Classe Base Abstrata
class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self._price = price

    # Este decorador força as classes filhas a implementarem este método
    @abstractmethod
    def apply_discount(self):
        # A implementação é vazia, pois é apenas um contrato
        pass
```

---

<br>
<br>
<br>

___


# Наследование
механизм ООП, который позволяет описать новый класс на основе уже существующего (родительского), 
при этом свойства и функциональность родительского класса заимствуются новым классом.
class Employee:
    pass

class Developer(Employee):
    pass

## Функция super()
 — это встроенная функция в Python, которая позволяет обращаться к методам родительского класса из дочернего класса.  
 
 class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return print(f'{self.first} {self.last}')

    def code(self):
        print("I'm coding as an employee.")

  class Developer(Employee):
    raise_amt = 1.10
    # Переопределяем метод базового класса
    def __init__(self, first, last, pay, prog_lang):
        # Вызываем метод базового класса
        super().__init__(first, last, pay)
        # Дополнительный код
        self.prog_lang = prog_lang


dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')

## Функция issubclass()
 — функция, которая используется для проверки, наследуется ли какой-либо класс от другого. Возвращает True, если первый 
 аргумент является подклассом второго аргумента, иначе возвращает False.
 
## Функция isinstance()
 — функция, которая используется для проверки принадлежности объекта к определенному классу. Возвращает True, если 
 объект является экземпляром указанного класса. Функция также вернет True, если класс, с которым объект сопоставляется, 
 является родительским для того класса, из которого сам объект был создан.

 class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise ValueError('Складывать можно только объекты Employee и дочерние от них.')
        return self.pay + other.pay


dev_1 = Developer('Ivan', 'Ivanov', 60000, 'Python')
dev_2 = Developer('Petr', 'Petrov', 70000, 'Java')
print(dev_1 + dev_2)
emp_1 = Employee('Petr', 'Petrov', 50000)
print(dev_1 + emp_1)
print(dev_2 + 10000)

# Задачи
## task_1:
Cоздать класс для разработчиков, установить ставку индексации ЗП 10%
Создать двух разработчиков
1. Создать класс, наследуемый от базового
2. Переопределить атрибут класса
3. Создать два экземпляра класса
   
## task_2:
Добавить разработчикам атрибут "язык программирования"
1. Создать инициализатор
2. Вызвать super()
3. Дописать атрибут prog_lang

## task_3:
Реализовать магический метод add и добавить проверку на сложение только с другими
экземплярами класса Employee и дочерних классов


# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Латашенко А.Д.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(capacity_volume, (int, float)):
            if occupied_volume > 0:
                self.occupied_volume = occupied_volume # объем жидкости
            else:
                raise ValueError
        else:
            raise TypeError


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.

glass_2_1 = Glass(200, 100) # экземпляр класса
print(glass_2_1.capacity_volume)
print(glass_2_1.occupied_volume)

glass_2_2 = Glass(500, 50) #экземпляр класса
print(glass_2_2.capacity_volume)
print(glass_2_2.occupied_volume)

# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)

class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(capacity_volume, (int, float)):
            if occupied_volume > 0:
                self.occupied_volume = occupied_volume # объем жидкости
            else:
                raise ValueError
        else:
            raise TypeError

glass_3_1 = GlassDefaultArg(200, 50)
glass_3_2 = GlassDefaultArg(200, 100)
print(glass_3_1.capacity_volume)
print(glass_3_1.occupied_volume)

# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)

print('=========')
glass_4_1 = GlassDefaultListArg(200)
print(glass_4_1.occupied_volume)

glass_4_2 = GlassDefaultListArg(200)
print(glass_4_2.occupied_volume)

glass_4_3 = GlassDefaultListArg(200)
print(glass_4_3.occupied_volume)


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.

class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume # объем стакана
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(capacity_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume  # объем жидкости
            else:
                raise ValueError
        else:
            raise TypeError

    def add_water(self, adding_water):
        space = self.capacity_volume - self.occupied_volume # пустое место
        self.occupied_volume += adding_water
        if self.occupied_volume > self.capacity_volume:
            return adding_water
        '''
        Проверить, верна ли формула (!!!)
        '''

    def remove_water(self, removing_water):
        pass

glass_5_1 = GlassAddRemove(100)
glass_5_1.add_water(100)


# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

glass_6_1 = GlassAddRemove(200, 100)
print(type(glass_6_1))
glass_6_2 = GlassAddRemove(500, 50)
print(type(glass_6_2))
glass_6_3 = GlassAddRemove(100, 0)
print(type(glass_6_3))

print(type(GlassAddRemove))

print(dir(glass_6_1))
# print(GlassAddRemove.__dict__)
# print(glass_6_1.__dict__)

# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.
class GlassDir:
    def __init__(self, capacity_volume, occupied_volume):
        print(dir(self))
        print(self.__dict__)

        self.capacity_volume = capacity_volume
        print(dir(self))
        print(self.__dict__)

        self.occupied_volume = occupied_volume
        print(dir(self))
        print(self.__dict__)

glass_7_1 = GlassDir(200, 100)

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.



# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
	def __init__(f, a=2):
		f.a = a
		
	def print_me(p):
		print(p.a)
		
d.print_me(d())		

# 10. Исправьте
class A:
	def __init__(self, a):
		if 10 < a < 50:
			return
		self.a = a;	

# Объясните так реализовывать __init__ нельзя?
		
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# 

class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:



    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...

























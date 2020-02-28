# class Point:
#     # x = 0
#     # y = 0

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def coordinates(self):
#         print(f'Координаты: x {self.x}, y {self.y}')
    
#     def __repr__(self):
#         return f'Point x: {self.x}, y: {self.y}'

# my_point = Point(11, 3)
# # my_point.coordinates()
# # my_point.x = 10
# # my_point.y = -5
# # my_point.coordinates()
# print(my_point)



class Product:
    def __init__(self, name, price, stock=0, discount=0, max_discount=20):
        self.name = name.strip()
        if len(self.name) < 2:
            raise ValueError('Название товара должно быть 2 символа или больше')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.discount = abs(float(discount))
        self.max_discount = abs(float(max_discount))
        if self.max_discount > 99:
            raise ValueError('Слишком большая максимальная скидка')
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Недостаточно товара на складе')
            # Здесь мы можем как-то взаимодействовать с учетной/бухгалтерской системой
        self.stock -= items_count

    def get_color(self):
        raise NotImplementedError

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

# product1 = Product('Товар', 100, stock=10)
# product1.sell(5)
# print(product1)

class Phone(Product):
    def __init__(self, name, price, color, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color

    def get_color(self):
        return f'Цвет корпуса: {self.color}'

    def get_memory_size(self):
        # Выводим размер памяти в гигабайтах
        pass 

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Sofa(Product):
    def __init__(self, name, price, color, texture, stock=0, discount=0, max_discount=20):
        super().__init__(name, price, stock, discount, max_discount)
        self.color = color
        self.texture = texture

    def get_color(self):
        return f'Цвет обивки: {self.color}. Тип ткани: {self.texture}'

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

my_phone = Phone('iPhone', 60000, 'Черный')
# print(my_phone)
# print(my_phone.color)
print(my_phone.get_color())

sofa1 = Sofa('Большой диван', 25312.4, 'желтый', 'Велюр')
# print(sofa1)
# print(sofa1.color)
# print(sofa1.texture)
print(sofa1.get_color())


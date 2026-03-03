class Rectangle:
    def __init__(self, width, heidht):
        self.width = width
        self.heidht = heidht

    def area(self):
        return self.width * self.heidht

    def perimeter(self):
        return 2 * (self.width + self.heidht)

    def __str__(self):
        return f'Прямоугольник(ширина={self.width}, высота={self.heidht})'

rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(8, 5)
rectangle3 = Rectangle(9, 6)

print(rectangle1)
print(f'Площадь: {rectangle1.area()}')
print(f'Периметр: {rectangle1.perimeter()}')


print(rectangle2)
print(f'Площадь: {rectangle2.area()}')
print(f'Периметр: {rectangle2.perimeter()}')

print(rectangle3)
print(f'Площадь: {rectangle3.area()}')
print(f'Периметр: {rectangle3.perimeter()}')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def addition(self):
        result = self.a + self.b
        print(f'{self.a} + {self.b} = {result}')
        return result

    def multiplication(self):
        result = self.a * self.b
        print(f'{self.a} * {self.b} = {result}')
        return result

    def subtraction(self):
        result = self.a - self.b
        print(f'{self.a} - {self.b} = {result}')
        return result

    def division(self):
        result = self.a / self.b
        print(f'{self.a} / {self.b} = {result}')
        return result

math1 = Math(3, 4)
math1.addition()
math1.multiplication()
math1.subtraction()
math1.division()



class Button:
    def __init__(self, text, locator=''):
        self.text = text
        self.type = 'кнопка'
        self.locator = locator

    def click(self):
        return 'Клик по кнопке'

button1 = Button('TextBox')
button2 = Button('CheckBox')
button3 = Button('Radio')
button4 = Button('WebTables')
button5 = Button('Buttons')
button6 = Button('Links')
button7 = Button('BrokenLinks')
button8 = Button('Upload')
button9 = Button('DynamicProperties')

print(f'Кнопка 1: {button1.text}, {button1.type}, {button1.locator}')
print(f'Кнопка 2: {button2.text}, {button2.type}, {button2.locator}')
print(f'Кнопка 3: {button3.text}, {button3.type}, {button3.locator}')
print(f'Кнопка 4: {button4.text}, {button4.type}, {button4.locator}')
print(f'Кнопка 5: {button5.text}, {button5.type}, {button5.locator}')
print(f'Кнопка 6: {button6.text}, {button6.type}, {button6.locator}')
print(f'Кнопка 7: {button7.text}, {button7.type}, {button7.locator}')
print(f'Кнопка 8: {button8.text}, {button8.type}, {button8.locator}')
print(f'Кнопка 9: {button9.text}, {button9.type}, {button9.locator}')

print(f'Нажатие на кнопку 1: {button1.click()}')
print(f'Нажатие на кнопку 2: {button2.click()}')
print(f'Нажатие на кнопку 3: {button3.click()}')
print(f'Нажатие на кнопку 4: {button4.click()}')
print(f'Нажатие на кнопку 5: {button5.click()}')
print(f'Нажатие на кнопку 6: {button6.click()}')
print(f'Нажатие на кнопку 7: {button7.click()}')
print(f'Нажатие на кнопку 8: {button8.click()}')
print(f'Нажатие на кнопку 9: {button9.click()}')


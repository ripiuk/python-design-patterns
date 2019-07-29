"""
Прототип — це породжуючий патерн, який дозволяє копіювати
об’єкти будь-якої складності без прив’язки до їхніх конкретних класів.
Усі класи-Прототипи мають спільний інтерфейс.
Тому ви можете копіювати об’єкти, не звертаючи уваги на їхні конкретні
типи та бути завжди впевненими в тому, що отримаєте точну копію.
Клонування здійснюється самим об’єктом-прототипу,
що дозволяє йому скопіювати значення всіх полів, навіть приватних.

Переваги:
    Дозволяє клонувати об’єкти без прив’язки до їхніх конкретних класів.
    Менша кількість повторювань коду ініціалізації об’єктів.
    Прискорює створення об’єктів.
    Альтернатива створенню підкласів під час конструювання складних об’єктів.
Недоліки:
    Складно клонувати складові об’єкти, що мають посилання на інші об’єкти.
"""
import copy


class Shape:

    def __init__(self):
        self._x = None
        self._y = None
        self._color = None

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str):
        self._color = value


class Circle(Shape):

    def __init__(self):
        super().__init__()
        self._height = None
        self._width = None

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    def __str__(self):
        return "Circle. X: {}, Y: {}, Height: {}, Width: {}".format(
            self.x, self.y, self.height, self.width)


class Rectangle(Shape):

    def __init__(self):
        super().__init__()
        self._radius = None

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: int):
        self._radius = value


class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    prototype = Prototype()
    circle1 = Circle()

    circle1.x = 10
    circle1.y = 10
    circle1.height = 50
    circle1.width = 300

    prototype.register(1, circle1)
    circle2 = prototype.clone(1)
    circle2.x = 20
    circle2.y = 20
    print(circle1, circle2, sep='\n')


# ================ Output ================
# Circle. X: 10, Y: 10, Height: 50, Width: 300
# Circle. X: 20, Y: 20, Height: 50, Width: 300

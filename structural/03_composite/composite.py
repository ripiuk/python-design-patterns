"""
Компонувальник — це структурний патерн,
який дозволяє створювати дерево об’єктів та працювати з ним так само,
як і з одиничним об’єктом.

Компонувальник давно став синонімом всіх завдань,
пов’язаних з побудовою дерева об’єктів.
Всі операції компонувальника базуються на рекурсії
та «підсумовуванні» результатів на гілках дерева.

Переваги:
  Спрощує архітектуру клієнта при роботі зі складним деревом компонентів.
  Полегшує додавання нових видів компонентів.
Недоліки:
  Створює занадто загальний дизайн класів.
"""
import typing as typ
from abc import ABC, abstractmethod


class Graphic(ABC):

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


class Dot(Graphic):

    def __init__(self):
        self.x = self.y = 0

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print("Drew {} object. X={}, Y={}".format(
            type(self).__name__, self.x, self.y))


class Circle(Dot):

    def __init__(self):
        super().__init__()
        self._radius = 0

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: int) -> None:
        self._radius = value

    def draw(self) -> None:
        print("Drew {} object. X={}, Y={}, Radius={}".format(
            type(self).__name__, self.x, self.y, self.radius))


class CompositeGraphic(Graphic):

    def __init__(self):
        self.graphics = list()  # type: typ.List[Graphic]

    def move(self, x: int, y: int) -> None:
        for graphic in self.graphics:
            graphic.move(x, y)

    def draw(self) -> None:
        for graphic in self.graphics:
            graphic.draw()

    def add(self, graphic: Graphic) -> None:
        self.graphics.append(graphic)

    def remove(self, graphic: Graphic) -> None:
        self.graphics.remove(graphic)


if __name__ == "__main__":
    dot = Dot()
    dot.move(x=10, y=-10)

    circle = Circle()
    circle.radius = 50
    circle.move(x=20, y=2)

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()
    graphic1.add(dot)
    graphic2.add(circle)

    general_graphic = CompositeGraphic()
    general_graphic.add(graphic1)
    general_graphic.add(graphic2)

    general_graphic.draw()


# ================ Output ================
# Drew Dot object. X=10, Y=-10
# Drew Circle object. X=20, Y=2, Radius=50

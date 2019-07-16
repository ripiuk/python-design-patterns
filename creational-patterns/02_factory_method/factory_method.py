"""
Фабричний метод — це породжуючий патерн проектування,
який вирішує проблему створення різних продуктів,
без прив’язки коду до конкретних класів продуктів.

Фабричний метод задає метод, який необхідно використовувати замість виклику оператора
new для створення об’єктів-продуктів. Підкласи можуть перевизначити цей метод,
щоб змінювати тип створюваних продуктів.

Переваги:
    Позбавляє клас від прив’язки до конкретних класів продуктів.
    Виділяє код виробництва продуктів в одне місце, спрощуючи підтримку коду.
    Спрощує додавання нових продуктів до програми.
    Реалізує принцип відкритості/закритості.
Недоліки:
    Може призвести до створення великих паралельних ієрархій класів,
        адже для кожного класу продукту потрібно створити власний підклас творця.

Паттерн Фабричный метод  — это устройство классов, при котором подклассы могут
переопределять тип создаваемого в суперклассе продукта. Если вы имеете иерархию продуктов
и абстрактный создающий метод, который переопределяется в подклассах,
то перед вами паттерн Фабричный метод.

Полезен, когда есть некоторая общая обработка в классе,
но необходимый подкласс динамически определяется во время выполнения.
Иными словами, когда клиент не знает, какой именно подкласс ему может понадобиться.
"""
import platform
from abc import ABC, abstractmethod


# ====== Buttons ======

class Button:

    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def weight(self) -> int:
        pass

    @property
    @abstractmethod
    def color(self) -> str:
        pass


class WinButton(Button):

    @property
    def height(self) -> int:
        return 10

    @property
    def weight(self) -> int:
        return 20

    @property
    def color(self) -> str:
        return "Blue"


class LinuxButton(Button):

    @property
    def height(self) -> int:
        return 15

    @property
    def weight(self) -> int:
        return 25

    @property
    def color(self) -> str:
        return "Grey"


# ====== Dialogs ======

class Dialog(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    def draw(self) -> None:
        button = self.create_button()
        print("Drawing button. Height: {}, Weight: {}, Color: {}".format(
            button.height, button.weight, button.color
        ))


class WinDialog(Dialog):

    def create_button(self) -> WinButton:
        return WinButton()


class LinuxDialog(Dialog):

    def create_button(self) -> LinuxButton:
        return LinuxButton()


# ====== Application ======

if __name__ == "__main__":
    platform_factories = {
        "Linux": LinuxDialog,
        "Windows": WinDialog,
    }
    my_os = platform.system()

    dialog = platform_factories.get(my_os)
    if not dialog:
        Exception("Unknown operation system")

    dialog = dialog()
    dialog.draw()

"""
Міст — це структурний патерн,
який розділяє бізнес-логіку або великий клас на кілька окремих ієрархій,
які можна розвивати далі окремо одну від одної.

Одна з цих ієрархій (абстракція) отримає посилання на
об’єкти іншої ієрархії (реалізація) і буде делегувати їм основну роботу.
Завдяки тому, що всі реалізації будуть дотримуватись спільного інтерфейсу,
їх можна буде взаємозамінювати всередині абстракції.

Переваги:
  Дозволяє будувати платформо-незалежні програми.
  Приховує зайві або небезпечні деталі реалізації від клієнтського коду.
  Реалізує принцип відкритості/закритості.
Недоліки:
  Ускладнює код програми внаслідок введення додаткових класів.
"""
import typing as typ
from functools import wraps


def when_turned_on(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.is_enabled:
            print("Please turn on the {} first".format(type(self).__name__))
            return
        method(self, *args, **kwargs)
    return wrapper


class Device:

    def __init__(self):
        self.is_enabled = False
        self.channel = 1
        self.volume = 10
        self.channel_step = 1

    def enable(self):
        self.is_enabled = True
        print("Turning on {}".format(
            type(self).__name__))

    def disable(self):
        self.is_enabled = False
        print("Turning off {}".format(
            type(self).__name__))

    @when_turned_on
    def set_volume(self, value: typ.Union[int, float]):
        self.volume = value if value > 0 else 0
        print("Set {} volume: {}".format(
            type(self).__name__, self.volume))

    @when_turned_on
    def set_channel(self, value: typ.Union[int, float]):
        self.channel = value if value >= 0 else 0
        print("Set {} channel: {}".format(
            type(self).__name__, self.channel))


class Remote:

    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        self.device.disable() if self.device.is_enabled else self.device.enable()

    def volume_up(self):
        self.device.set_volume(self.device.volume + 10)

    def volume_down(self):
        self.device.set_volume(self.device.volume - 10)

    def next_channel(self):
        self.device.set_channel(self.device.channel + self.device.channel_step)

    def previous_channel(self):
        self.device.set_channel(self.device.channel - self.device.channel_step)


class AdvancedRemote(Remote):
    """Можна розширювать клас пультів не чіпаючи клас пристроїв"""

    def mute(self):
        self.device.set_volume(0)


class TV(Device):
    pass


class Radio(Device):

    def __init__(self):
        super().__init__()
        self.channel = 99.0
        self.channel_step = 0.2


if __name__ == "__main__":
    tv = TV()
    tv_remote = Remote(tv)
    tv_remote.next_channel()
    tv_remote.toggle_power()
    tv_remote.next_channel()

    print('\n')
    radio = Radio()
    radio_remote = AdvancedRemote(radio)
    radio_remote.next_channel()
    radio_remote.toggle_power()
    radio_remote.next_channel()
    radio_remote.mute()


# ================ Output ================
# Please turn on the TV first
# Turning on TV
# Set TV channel: 2
#
# Please turn on the Radio first
# Turning on Radio
# Set Radio channel: 99.2
# Set Radio volume: 0

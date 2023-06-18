from game.components.power_ups.power_up import PowerUp
from game.utils.constants import FUEL, SPEED_TYPE

class Speed(PowerUp):
    def __init__(self):
        super().__init__(FUEL, SPEED_TYPE)
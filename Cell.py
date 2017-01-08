from Game import *
from Block import *
import uuid
from Food import Food

class Cell(MoveableBlock):
    DEAD_COLOR = (128, 128, 128)

    OBJECT_ENEMIES = 0
    OBJECT_FOOD = 1

    def __init__(self, game, x, y, color, energy, logic):
        MoveableBlock.__init__(self, game, x, y, color)

        self._energy = energy
        self._logic = logic
        self._is_alive = True

        self.uuid = uuid.uuid4()

    def tick(self):
        if not self._is_alive:
            return

        detected_objects = []

        if self._energy <= self._logic.low_energy:
            self._logic.on_low_energy(self)
        elif self._energy >= self._logic.high_energy:
            self._logic.on_high_energy(self)
        elif self._detect_objects(detected_objects, Cell.OBJECT_ENEMIES):
            self._logic.on_enemies_detected(self, [obj for obj in detected_objects if isinstance(obj, Cell)])
        elif self._detect_objects(detected_objects, Cell.OBJECT_FOOD):
            self._logic.on_food_detected(self, [obj for obj in detected_objects if isinstance(obj, Food)])
        else:
            self._logic.on_idle(self)

        self._energy -= 1

        if self._energy <= 0:
            self._kill()
            return

    def _kill(self):
        self._is_alive = False
        self.color = Cell.DEAD_COLOR

    ## TODO: Right now anything is an enemy
    def _detect_objects(self, detected_objects, object_type):
        detected_food = False
        detected_enemy = False

        if len(detected_objects) == 0:
            for x in range(-2, 3):
                for y in range(-2, 3):
                    obj = self._game.grid.get(self.x + x, self.y + y)

                    if obj is not None:
                        detected_objects.append(obj)

                        if isinstance(obj, Food):
                            detected_food = True
                        elif obj.uuid != self.uuid:
                            detected_enemy = True
        else:
            for obj in detected_objects:
                    if isinstance(obj, Food):
                        detected_food = True
                    elif obj.uuid != self.uuid:
                        detected_enemy = True


        return (object_type == Cell.OBJECT_ENEMIES and detected_enemy) or (object_type == Cell.OBJECT_FOOD and detected_food)

    ###########

    def move_toward(self, other): 
        x = 0
        y = 0

        if self.x > other.x:
            x = -1
        elif self.x < other.x:
            x = 1

        if self.y > other.y:
            y = -1
        elif self.y < other.y:
            y = 1

        if (x != 0 or y != 0) and self.move(self.x + x, self.y + y):
            self._energy -= 1
            return True
        else:
            return False

    def move_random(self):
        x = randint(-1, 1)
        y = randint(-1, 1)

        if (x != 0 or y != 0) and self.move(self.x + x, self.y + y):
            self._energy -= 1
            return True
        else:
            return False


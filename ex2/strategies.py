from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.creatures import TransformCapability, HealCapability


class BattleStrategy(ABC):
    def __init__(self, creature: Creature) -> None:
        self._creature = creature

    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def act(self) -> None:
        print(self._creature.attack())

    def is_valid(self) -> bool:
        if isinstance(self._creature, Creature):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def act(self) -> None:
        if self.is_valid():
            print(self._creature.transform())  # type: ignore
            print(self._creature.attack())
            print(self._creature.revert())  # type: ignore
        else:
            raise Exception(f"Invalid creature '{self._creature._name}' for"
                            "this aggressive strategy")

    def is_valid(self) -> bool:
        if isinstance(self._creature, TransformCapability):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def act(self) -> None:
        if self.is_valid():
            print(self._creature.attack())
            print(self._creature.heal(self._creature))  # type: ignore
        else:
            raise Exception(f"Invalid creature '{self._creature._name}' for"
                            "this defensive strategy")

    def is_valid(self) -> bool:
        if isinstance(self._creature, HealCapability):
            return True
        return False

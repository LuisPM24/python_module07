from ex0 import CreatureFactory, FlameFactory, AquaFactory


def creature_tester(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack(), end="\n\n")


def battle(flame_factory: FlameFactory, aqua_factory: AquaFactory
           ) -> None:
    creature_1 = flame_factory.create_base()
    creature_2 = aqua_factory.create_base()
    print(creature_1.describe())
    print("vs.")
    print(creature_2.describe())
    print(creature_1.attack())
    print(creature_2.attack())


def main() -> None:
    print("Testing factory")
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    creature_tester(flame_factory)
    print("Testing factory")
    creature_tester(aqua_factory)
    print("Testing battle")
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()

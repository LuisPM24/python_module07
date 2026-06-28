from ex0 import FlameFactory, AquaFactory


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
    flameling = FlameFactory().create_base()
    pyrodon = FlameFactory().create_evolved()
    print(flameling.describe())
    print(flameling.attack())
    print(pyrodon.describe())
    print(pyrodon.attack(), end="\n\n")
    print("Testing factory")
    aquabub = AquaFactory().create_base()
    torragon = AquaFactory().create_evolved()
    print(aquabub.describe())
    print(aquabub.attack())
    print(torragon.describe())
    print(torragon.attack(), end="\n\n")
    print("Testing battle")
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()

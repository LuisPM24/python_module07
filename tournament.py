from ex0 import FlameFactory
from ex1.creature_factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategies import BattleStrategy


def single_battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]
                  ) -> None:
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                print("\n* Battle *")
                fact_1, strat_1 = opponents[i]
                fact_2, strat_2 = opponents[j]
                comb_1 = fact_1.create_base()
                comb_2 = fact_2.create_base()
                print(comb_1.describe())
                print("vs.")
                print(comb_2.describe())
                print("now fight!")
                strat_1.act()
                strat_2.act()
    except Exception as e:
        print(f"Battle error, aborting torunament: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    heal_factory = HealingCreatureFactory()
    morph_factory = TransformCreatureFactory()
    normal_flameling = NormalStrategy(flame_factory.create_base())
    aggr_flameling = AggressiveStrategy(flame_factory.create_base())
    def_sproutling = DefensiveStrategy(heal_factory.create_base())
    aggr_morphagon = AggressiveStrategy(morph_factory.create_base())
    set1 = [
        (flame_factory, normal_flameling),
        (heal_factory, def_sproutling)
    ]
    set2 = [
        (flame_factory, aggr_flameling),
        (heal_factory, def_sproutling)
    ]
    set3 = [
        (flame_factory, normal_flameling),
        (heal_factory, def_sproutling),
        (morph_factory, aggr_morphagon)

    ]

    print("*** Tournaments ***")
    print("Tournament 0: basic\n")
    single_battle(set1)
    print("\nTornament 1: Error\n")
    single_battle(set2)
    print("\nTornament 2: Multiple\n")
    single_battle(set3)


if __name__ == "__main__":
    main()

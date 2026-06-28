from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def main() -> None:
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    sproutling = heal_factory.create_base()
    bloomelle = heal_factory.create_evolved()
    shiftling = transform_factory.create_base()
    morphagon = transform_factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(sproutling.describe())
    print(sproutling.attack())
    if isinstance(sproutling, HealCapability):
        print(sproutling.heal(bloomelle))
    print(" evolved:")
    print(bloomelle.describe())
    print(bloomelle.attack())
    if isinstance(bloomelle, HealCapability):
        print(bloomelle.heal(sproutling))

    print("\nTesting Creature with transform capability")
    print(" base:")
    print(shiftling.describe())
    print(shiftling.attack())
    if isinstance(shiftling, TransformCapability):
        print(shiftling.transform())
    print(shiftling.attack())
    if isinstance(shiftling, TransformCapability):
        print(shiftling.revert())
    print(" evolved:")
    print(morphagon.describe())
    print(morphagon.attack())
    if isinstance(morphagon, TransformCapability):
        print(morphagon.transform())
    print(morphagon.attack())
    if isinstance(morphagon, TransformCapability):
        print(morphagon.revert())


if __name__ == "__main__":
    main()

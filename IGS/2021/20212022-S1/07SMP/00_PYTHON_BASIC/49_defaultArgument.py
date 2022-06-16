
def describe_pet(animal_type="cat", pet_name="john"):

	print(f"I have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name}")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

describe_pet("dog")
describe_pet()
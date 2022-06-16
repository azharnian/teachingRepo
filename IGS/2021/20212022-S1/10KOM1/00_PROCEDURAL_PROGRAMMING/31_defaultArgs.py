
def describe_pet(pet_name, animal_type="dog"):
	print(f"\nI have a {animal_type}")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet(pet_name='moliey', animal_type='pig')
describe_pet('willie')

# .upper(), .lower(), .title() # Method Default dari Ob. Str
# DEBBIE     debbie    Debbie
#Equivalent Function

describe_pet('debbie', 'hen')
describe_pet(animal_type='hen', pet_name='debbie')
describe_pet(pet_name='debbie', animal_type='hen')

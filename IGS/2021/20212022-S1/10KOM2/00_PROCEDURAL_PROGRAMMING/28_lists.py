#storing data -> variable
bicycle1 = 'trek'
bicycle2 = 'polygon'
bicycles = ['trek', 'polygon', 'brompton', 'cannodale']
print(bicycles)

#list -> index(alamat) dan value(data)
print(bicycles[1].title()) #polygon
print(bicycles[0])

msg = f"My first bicycle was a {bicycles[0].title()}"
print(msg)

print(bicycles[-1]) #cannodale
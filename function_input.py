def greet(name):
  print(f"Hello, {name}")
  print(f"How are you, {name} ")
  print(f"Good luck, {name} ")

greet("Djon")

def greet_with(name, location):
  print(f'Hello {name}')
  print(f"What is it like in {location}")

greet_with("Jack Bauer", "Nowhere")
greet_with(location = "Lviv", name = "Igor")    # именованные аргументы

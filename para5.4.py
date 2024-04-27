import inspect


class Human:
    def __init__(self, age, height, name="Jason"):
        self.age = age
        self.name = name
        self.secondname = "Statham"

sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)
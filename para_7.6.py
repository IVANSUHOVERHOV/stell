class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"I will help your with your {self.work}.  Afterwards I will help you with {work}"


helper = Helper("Homework")
print(helper("cleaning"))
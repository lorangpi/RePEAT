from Formula import Formula


class AtomicFormula(Formula):
    
    def __init__(self, atom):
        self.name = atom
        self.getName()

    def getName(self):
        return self.name

    def __str__(self):
        return str(self.name)


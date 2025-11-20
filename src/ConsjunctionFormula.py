from Formula import Formula
from AtomicFormula import AtomicFormula

class ConjunctionFormula(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.Conjunction(left, right)
        

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def __str__(self):
        return self.conjunction

    def Conjunction(self, left, right):
        if not( isinstance(left, AtomicFormula) or isinstance(right, AtomicFormula)):
            self.conjunction = str(left) + "&" + str(right)
        else:
            self.conjunction = "(" + str(left) + "&" + str(right) + ")"
        return self.conjunction

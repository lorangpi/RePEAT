from Formula import Formula
from AtomicFormula import AtomicFormula

class DisjunctionFormula(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.Disjunction(left, right)
        

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def __str__(self):
        return self.disjunction

    def Disjunction(self, left, right):
        if not( isinstance(left, AtomicFormula) or isinstance(right, AtomicFormula)):
            self.disjunction = str(left) + "|" + str(right)
        else:
            self.disjunction = "(" + str(left) + "|" + str(right) + ")"
        return self.disjunction

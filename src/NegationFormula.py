from Formula import Formula
from antlr4 import *
from AtomicFormula import AtomicFormula
from ConsjunctionFormula import ConjunctionFormula
from DisjunctionFormula import DisjunctionFormula
from ModalOpFormula import ModalOpFormula

class NegationFormula(Formula):

    def __init__(self, negation):
        self.negation = negation
        self.result = self.Negation(negation)
        self.back()
    
    def __str__(self):
        return self.result

    def Negation(self, neg):
        if isinstance(neg, ConjunctionFormula):
            left = neg.getLeft()
            right = neg.getRight()
            result = self.Negation(left) + "|" + self.Negation(right)
        elif isinstance(neg, DisjunctionFormula):
            left = neg.getLeft()
            right = neg.getRight()
            result = self.Negation(left) + "&" + self.Negation(right)
        else:
            if isinstance(neg, AtomicFormula) or isinstance(neg, ModalOpFormula) or (type(neg) is str and neg[0].isalpha()):
                result = "¬" + "(" + str(neg) + ")"
            else:
                result = "¬" + str(neg)     
        return result

    def back(self):
        return self.result

from Formula import Formula
from antlr4 import *
from AtomicFormula import AtomicFormula
from ConsjunctionFormula import ConjunctionFormula
from DisjunctionFormula import DisjunctionFormula

class ModalOpFormula(Formula):

    def __init__(self, agent, formula):
        self.formula = formula
        self.agent = agent
        self.Operation(formula)
    
    def __str__(self):
        return self.operation

    def Operation(self, form):
        if isinstance(form, AtomicFormula) or isinstance(form, ModalOpFormula) or isinstance(form, ConjunctionFormula) or isinstance(form, DisjunctionFormula) or str(form)[0] in ('-', '!', '¬'):
            self.operation = "Op" + str(self.agent) + "(" + str(self.formula) + ")"
        else:
            self.operation = "Op" + str(self.agent) + str(self.formula) 
        return self.operation
# Generated from Formula.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete listener for a parse tree produced by FormulaParser.
class FormulaListener(ParseTreeListener):

    # Enter a parse tree produced by FormulaParser#modal_operator.
    def enterModal_operator(self, ctx:FormulaParser.Modal_operatorContext):
        pass

    # Exit a parse tree produced by FormulaParser#modal_operator.
    def exitModal_operator(self, ctx:FormulaParser.Modal_operatorContext):
        pass


    # Enter a parse tree produced by FormulaParser#parens.
    def enterParens(self, ctx:FormulaParser.ParensContext):
        pass

    # Exit a parse tree produced by FormulaParser#parens.
    def exitParens(self, ctx:FormulaParser.ParensContext):
        pass


    # Enter a parse tree produced by FormulaParser#negation.
    def enterNegation(self, ctx:FormulaParser.NegationContext):
        pass

    # Exit a parse tree produced by FormulaParser#negation.
    def exitNegation(self, ctx:FormulaParser.NegationContext):
        pass


    # Enter a parse tree produced by FormulaParser#conjunction.
    def enterConjunction(self, ctx:FormulaParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by FormulaParser#conjunction.
    def exitConjunction(self, ctx:FormulaParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by FormulaParser#disjunction.
    def enterDisjunction(self, ctx:FormulaParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by FormulaParser#disjunction.
    def exitDisjunction(self, ctx:FormulaParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by FormulaParser#atom.
    def enterAtom(self, ctx:FormulaParser.AtomContext):
        pass

    # Exit a parse tree produced by FormulaParser#atom.
    def exitAtom(self, ctx:FormulaParser.AtomContext):
        pass



del FormulaParser
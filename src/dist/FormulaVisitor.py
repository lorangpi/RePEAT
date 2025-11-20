# Generated from Formula.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete generic visitor for a parse tree produced by FormulaParser.

class FormulaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FormulaParser#modal_operator.
    def visitModal_operator(self, ctx:FormulaParser.Modal_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#parens.
    def visitParens(self, ctx:FormulaParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#negation.
    def visitNegation(self, ctx:FormulaParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#conjunction.
    def visitConjunction(self, ctx:FormulaParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#disjunction.
    def visitDisjunction(self, ctx:FormulaParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FormulaParser#atom.
    def visitAtom(self, ctx:FormulaParser.AtomContext):
        return self.visitChildren(ctx)



del FormulaParser
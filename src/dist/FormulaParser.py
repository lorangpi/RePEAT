# Generated from Formula.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\62\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2%\n\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\7\2-\n\2\f\2\16\2\60\13\2\3\2\2\3\2\3\2\2")
        buf.write("\2\29\2$\3\2\2\2\4\5\b\2\1\2\5%\7\n\2\2\6\7\7\3\2\2\7")
        buf.write("\b\5\2\2\2\b\t\7\4\2\2\t%\3\2\2\2\n\13\7\5\2\2\13\f\5")
        buf.write("\2\2\2\f\r\7\4\2\2\r%\3\2\2\2\16\17\7\6\2\2\17\20\5\2")
        buf.write("\2\2\20\21\7\4\2\2\21%\3\2\2\2\22\23\7\7\2\2\23\24\5\2")
        buf.write("\2\2\24\25\7\4\2\2\25%\3\2\2\2\26\27\7\r\2\2\27\30\5\2")
        buf.write("\2\2\30\31\7\3\2\2\31\32\5\2\2\2\32\33\7\4\2\2\33%\3\2")
        buf.write("\2\2\34\35\7\b\2\2\35\36\5\2\2\2\36\37\7\4\2\2\37%\3\2")
        buf.write("\2\2 !\7\t\2\2!\"\5\2\2\2\"#\7\4\2\2#%\3\2\2\2$\4\3\2")
        buf.write("\2\2$\6\3\2\2\2$\n\3\2\2\2$\16\3\2\2\2$\22\3\2\2\2$\26")
        buf.write("\3\2\2\2$\34\3\2\2\2$ \3\2\2\2%.\3\2\2\2&\'\f\13\2\2\'")
        buf.write("(\7\13\2\2(-\5\2\2\f)*\f\n\2\2*+\7\f\2\2+-\5\2\2\13,&")
        buf.write("\3\2\2\2,)\3\2\2\2-\60\3\2\2\2.,\3\2\2\2./\3\2\2\2/\3")
        buf.write("\3\2\2\2\60.\3\2\2\2\5$,.")
        return buf.getvalue()


class FormulaParser ( Parser ):

    grammarFileName = "Formula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-('", "'\u00AC('", "'!('", 
                     "'Box('", "'B('", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Op'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LOWER_NAME", "OP_AND", "OP_OR", "MODAL_OP", "NEG", 
                      "WS" ]

    RULE_formula = 0

    ruleNames =  [ "formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LOWER_NAME=8
    OP_AND=9
    OP_OR=10
    MODAL_OP=11
    NEG=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FormulaParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Modal_operatorContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MODAL_OP(self):
            return self.getToken(FormulaParser.MODAL_OP, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FormulaParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModal_operator" ):
                listener.enterModal_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModal_operator" ):
                listener.exitModal_operator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModal_operator" ):
                return visitor.visitModal_operator(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(FormulaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NegationContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(FormulaParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegation" ):
                return visitor.visitNegation(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FormulaParser.FormulaContext,i)

        def OP_AND(self):
            return self.getToken(FormulaParser.OP_AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunction" ):
                listener.enterConjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunction" ):
                listener.exitConjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunction" ):
                return visitor.visitConjunction(self)
            else:
                return visitor.visitChildren(self)


    class DisjunctionContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FormulaParser.FormulaContext)
            else:
                return self.getTypedRuleContext(FormulaParser.FormulaContext,i)

        def OP_OR(self):
            return self.getToken(FormulaParser.OP_OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunction" ):
                listener.enterDisjunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunction" ):
                listener.exitDisjunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunction" ):
                return visitor.visitDisjunction(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FormulaParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOWER_NAME(self):
            return self.getToken(FormulaParser.LOWER_NAME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FormulaParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FormulaParser.LOWER_NAME]:
                localctx = FormulaParser.AtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(FormulaParser.LOWER_NAME)
                pass
            elif token in [FormulaParser.T__0]:
                localctx = FormulaParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(FormulaParser.T__0)
                self.state = 5
                self.formula(0)
                self.state = 6
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.T__2]:
                localctx = FormulaParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(FormulaParser.T__2)
                self.state = 9
                self.formula(0)
                self.state = 10
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.T__3]:
                localctx = FormulaParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(FormulaParser.T__3)
                self.state = 13
                self.formula(0)
                self.state = 14
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.T__4]:
                localctx = FormulaParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.match(FormulaParser.T__4)
                self.state = 17
                self.formula(0)
                self.state = 18
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.MODAL_OP]:
                localctx = FormulaParser.Modal_operatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(FormulaParser.MODAL_OP)
                self.state = 21
                self.formula(0)
                self.state = 22
                self.match(FormulaParser.T__0)
                self.state = 23
                self.formula(0)
                self.state = 24
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.T__5]:
                localctx = FormulaParser.Modal_operatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(FormulaParser.T__5)
                self.state = 27
                self.formula(0)
                self.state = 28
                self.match(FormulaParser.T__1)
                pass
            elif token in [FormulaParser.T__6]:
                localctx = FormulaParser.Modal_operatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(FormulaParser.T__6)
                self.state = 31
                self.formula(0)
                self.state = 32
                self.match(FormulaParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = FormulaParser.ConjunctionContext(self, FormulaParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 36
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 37
                        self.match(FormulaParser.OP_AND)
                        self.state = 38
                        self.formula(10)
                        pass

                    elif la_ == 2:
                        localctx = FormulaParser.DisjunctionContext(self, FormulaParser.FormulaContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 39
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 40
                        self.match(FormulaParser.OP_OR)
                        self.state = 41
                        self.formula(9)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         





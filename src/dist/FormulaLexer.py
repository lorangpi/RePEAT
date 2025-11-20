# Generated from Formula.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3")
        buf.write("\13\5\13C\n\13\3\f\3\f\3\r\3\r\3\r\5\rJ\n\r\3\16\3\16")
        buf.write("\7\16N\n\16\f\16\16\16Q\13\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("W\n\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\6\23a\n")
        buf.write("\23\r\23\16\23b\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\2\23\2\25\2\27\2\31\2\33\n\35\13\37\f!\r")
        buf.write("#\16%\17\3\2\t\3\2c|\3\2C\\\3\2\62;\4\2\60\60xx\5\2--")
        buf.write("``~~\5\2##//\u00ae\u00ae\5\2\13\f\17\17\"\"\2g\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2")
        buf.write("\2\5)\3\2\2\2\7+\3\2\2\2\t.\3\2\2\2\13\61\3\2\2\2\r\64")
        buf.write("\3\2\2\2\179\3\2\2\2\21<\3\2\2\2\23>\3\2\2\2\25B\3\2\2")
        buf.write("\2\27D\3\2\2\2\31I\3\2\2\2\33K\3\2\2\2\35V\3\2\2\2\37")
        buf.write("X\3\2\2\2!Z\3\2\2\2#]\3\2\2\2%`\3\2\2\2\'(\7*\2\2(\4\3")
        buf.write("\2\2\2)*\7+\2\2*\6\3\2\2\2+,\7/\2\2,-\7*\2\2-\b\3\2\2")
        buf.write("\2./\7\u00ae\2\2/\60\7*\2\2\60\n\3\2\2\2\61\62\7#\2\2")
        buf.write("\62\63\7*\2\2\63\f\3\2\2\2\64\65\7D\2\2\65\66\7q\2\2\66")
        buf.write("\67\7z\2\2\678\7*\2\28\16\3\2\2\29:\7D\2\2:;\7*\2\2;\20")
        buf.write("\3\2\2\2<=\t\2\2\2=\22\3\2\2\2>?\t\3\2\2?\24\3\2\2\2@")
        buf.write("C\5\21\t\2AC\5\23\n\2B@\3\2\2\2BA\3\2\2\2C\26\3\2\2\2")
        buf.write("DE\t\4\2\2E\30\3\2\2\2FJ\5\25\13\2GJ\5\27\f\2HJ\7a\2\2")
        buf.write("IF\3\2\2\2IG\3\2\2\2IH\3\2\2\2J\32\3\2\2\2KO\5\21\t\2")
        buf.write("LN\5\31\r\2ML\3\2\2\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\34")
        buf.write("\3\2\2\2QO\3\2\2\2RW\7(\2\2ST\7(\2\2TW\7(\2\2UW\t\5\2")
        buf.write("\2VR\3\2\2\2VS\3\2\2\2VU\3\2\2\2W\36\3\2\2\2XY\t\6\2\2")
        buf.write("Y \3\2\2\2Z[\7Q\2\2[\\\7r\2\2\\\"\3\2\2\2]^\t\7\2\2^$")
        buf.write("\3\2\2\2_a\t\b\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2")
        buf.write("\2\2cd\3\2\2\2de\b\23\2\2e&\3\2\2\2\b\2BIOVb\3\b\2\2")
        return buf.getvalue()


class FormulaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    LOWER_NAME = 8
    OP_AND = 9
    OP_OR = 10
    MODAL_OP = 11
    NEG = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'-('", "'\u00AC('", "'!('", "'Box('", "'B('", 
            "'Op'" ]

    symbolicNames = [ "<INVALID>",
            "LOWER_NAME", "OP_AND", "OP_OR", "MODAL_OP", "NEG", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "LOWER", "UPPER", "LETTER", "DIGIT", "ANYCHAR", "LOWER_NAME", 
                  "OP_AND", "OP_OR", "MODAL_OP", "NEG", "WS" ]

    grammarFileName = "Formula.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



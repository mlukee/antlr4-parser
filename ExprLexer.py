# Generated from .\Expr.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,77,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,4,3,33,8,3,11,3,12,3,34,1,3,1,3,4,3,39,8,3,11,3,12,
        3,40,3,3,43,8,3,1,4,4,4,46,8,4,11,4,12,4,47,1,4,5,4,51,8,4,10,4,
        12,4,54,9,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,3,10,67,
        8,10,1,10,1,10,1,11,4,11,72,8,11,11,11,12,11,73,1,11,1,11,0,0,12,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,3,
        1,0,48,57,2,0,65,90,97,122,2,0,9,9,32,32,83,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,32,1,0,0,0,9,45,1,0,0,
        0,11,55,1,0,0,0,13,57,1,0,0,0,15,59,1,0,0,0,17,61,1,0,0,0,19,63,
        1,0,0,0,21,66,1,0,0,0,23,71,1,0,0,0,25,26,5,61,0,0,26,2,1,0,0,0,
        27,28,5,40,0,0,28,4,1,0,0,0,29,30,5,41,0,0,30,6,1,0,0,0,31,33,7,
        0,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,
        42,1,0,0,0,36,38,5,46,0,0,37,39,7,0,0,0,38,37,1,0,0,0,39,40,1,0,
        0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,36,1,0,0,0,42,43,
        1,0,0,0,43,8,1,0,0,0,44,46,7,1,0,0,45,44,1,0,0,0,46,47,1,0,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,52,1,0,0,0,49,51,7,0,0,0,50,49,1,0,0,
        0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,10,1,0,0,0,54,52,
        1,0,0,0,55,56,5,42,0,0,56,12,1,0,0,0,57,58,5,47,0,0,58,14,1,0,0,
        0,59,60,5,94,0,0,60,16,1,0,0,0,61,62,5,43,0,0,62,18,1,0,0,0,63,64,
        5,45,0,0,64,20,1,0,0,0,65,67,5,13,0,0,66,65,1,0,0,0,66,67,1,0,0,
        0,67,68,1,0,0,0,68,69,5,10,0,0,69,22,1,0,0,0,70,72,7,2,0,0,71,70,
        1,0,0,0,72,73,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,
        75,76,6,11,0,0,76,24,1,0,0,0,8,0,34,40,42,47,52,66,73,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    FLOAT = 4
    VARIABLE = 5
    MUL = 6
    DIV = 7
    POW = 8
    ADD = 9
    SUB = 10
    NEWLINE = 11
    IGNORE = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'*'", "'/'", "'^'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "FLOAT", "VARIABLE", "MUL", "DIV", "POW", "ADD", "SUB", "NEWLINE", 
            "IGNORE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "FLOAT", "VARIABLE", "MUL", "DIV", 
                  "POW", "ADD", "SUB", "NEWLINE", "IGNORE" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


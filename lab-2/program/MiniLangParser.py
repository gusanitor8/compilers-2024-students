# Generated from MiniLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,114,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,26,8,1,11,
        1,12,1,27,1,1,1,1,1,1,1,1,1,1,3,1,35,8,1,1,1,1,1,1,1,1,1,1,1,1,1,
        4,1,43,8,1,11,1,12,1,44,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,54,8,1,10,
        1,12,1,57,9,1,3,1,59,8,1,1,1,1,1,1,1,1,1,1,1,4,1,66,8,1,11,1,12,
        1,67,1,1,1,1,1,1,1,1,3,1,74,8,1,1,1,1,1,1,1,1,1,1,1,5,1,81,8,1,10,
        1,12,1,84,9,1,3,1,86,8,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,3,2,98,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,109,8,2,10,
        2,12,2,112,9,2,1,2,0,1,4,3,0,2,4,0,3,1,0,10,11,1,0,12,13,1,0,14,
        15,131,0,7,1,0,0,0,2,88,1,0,0,0,4,97,1,0,0,0,6,8,3,2,1,0,7,6,1,0,
        0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,3,4,
        2,0,12,13,5,22,0,0,13,89,1,0,0,0,14,15,5,19,0,0,15,16,5,16,0,0,16,
        17,3,4,2,0,17,18,5,22,0,0,18,89,1,0,0,0,19,20,5,1,0,0,20,21,3,4,
        2,0,21,25,5,2,0,0,22,23,5,22,0,0,23,24,5,21,0,0,24,26,3,2,1,0,25,
        22,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,34,1,0,0,
        0,29,30,5,22,0,0,30,31,5,3,0,0,31,32,5,22,0,0,32,33,5,21,0,0,33,
        35,3,2,1,0,34,29,1,0,0,0,34,35,1,0,0,0,35,89,1,0,0,0,36,37,5,4,0,
        0,37,38,3,4,2,0,38,42,5,5,0,0,39,40,5,22,0,0,40,41,5,21,0,0,41,43,
        3,2,1,0,42,39,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,
        45,89,1,0,0,0,46,89,5,22,0,0,47,48,5,8,0,0,48,49,5,19,0,0,49,58,
        5,17,0,0,50,55,5,19,0,0,51,52,5,6,0,0,52,54,5,19,0,0,53,51,1,0,0,
        0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,59,1,0,0,0,57,55,
        1,0,0,0,58,50,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,18,0,0,
        61,65,5,7,0,0,62,63,5,22,0,0,63,64,5,21,0,0,64,66,3,2,1,0,65,62,
        1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,73,1,0,0,0,
        69,70,5,22,0,0,70,71,5,21,0,0,71,72,5,9,0,0,72,74,3,4,2,0,73,69,
        1,0,0,0,73,74,1,0,0,0,74,89,1,0,0,0,75,76,5,19,0,0,76,85,5,17,0,
        0,77,82,3,4,2,0,78,79,5,6,0,0,79,81,3,4,2,0,80,78,1,0,0,0,81,84,
        1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,
        85,77,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,89,5,18,0,0,88,11,1,
        0,0,0,88,14,1,0,0,0,88,19,1,0,0,0,88,36,1,0,0,0,88,46,1,0,0,0,88,
        47,1,0,0,0,88,75,1,0,0,0,89,3,1,0,0,0,90,91,6,2,-1,0,91,98,5,20,
        0,0,92,98,5,19,0,0,93,94,5,17,0,0,94,95,3,4,2,0,95,96,5,18,0,0,96,
        98,1,0,0,0,97,90,1,0,0,0,97,92,1,0,0,0,97,93,1,0,0,0,98,110,1,0,
        0,0,99,100,10,6,0,0,100,101,7,0,0,0,101,109,3,4,2,7,102,103,10,5,
        0,0,103,104,7,1,0,0,104,109,3,4,2,6,105,106,10,4,0,0,106,107,7,2,
        0,0,107,109,3,4,2,5,108,99,1,0,0,0,108,102,1,0,0,0,108,105,1,0,0,
        0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,5,1,0,0,0,
        112,110,1,0,0,0,14,9,27,34,44,55,58,67,73,82,85,88,97,108,110
    ]

class MiniLangParser ( Parser ):

    grammarFileName = "MiniLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "','", "':'", "'def'", "'return'", "'*'", "'/'", 
                     "'+'", "'-'", "'=='", "'!='", "'='", "'('", "')'", 
                     "<INVALID>", "<INVALID>", "'    '" ]

    symbolicNames = [ "<INVALID>", "IF", "THEN", "ELSE", "WHILE", "DO", 
                      "COMMA", "COLON", "DEF", "RETURN", "MUL", "DIV", "ADD", 
                      "SUB", "EQ", "NEQ", "EQQ", "LPAREN", "RPAREN", "ID", 
                      "INT", "TAB", "NEWLINE", "WS", "COMM" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    IF=1
    THEN=2
    ELSE=3
    WHILE=4
    DO=5
    COMMA=6
    COLON=7
    DEF=8
    RETURN=9
    MUL=10
    DIV=11
    ADD=12
    SUB=13
    EQ=14
    NEQ=15
    EQQ=16
    LPAREN=17
    RPAREN=18
    ID=19
    INT=20
    TAB=21
    NEWLINE=22
    WS=23
    COMM=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def getRuleIndex(self):
            return MiniLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MiniLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5898514) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniLangParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def THEN(self):
            return self.getToken(MiniLangParser.THEN, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)
        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.TAB)
            else:
                return self.getToken(MiniLangParser.TAB, i)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)

        def ELSE(self):
            return self.getToken(MiniLangParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)


    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class CallFunctionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunction" ):
                listener.enterCallFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunction" ):
                listener.exitCallFunction(self)


    class DeclareFunctionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEF(self):
            return self.getToken(MiniLangParser.DEF, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.ID)
            else:
                return self.getToken(MiniLangParser.ID, i)
        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)
        def COLON(self):
            return self.getToken(MiniLangParser.COLON, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)
        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.TAB)
            else:
                return self.getToken(MiniLangParser.TAB, i)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)

        def RETURN(self):
            return self.getToken(MiniLangParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.COMMA)
            else:
                return self.getToken(MiniLangParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareFunction" ):
                listener.enterDeclareFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareFunction" ):
                listener.exitDeclareFunction(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)
        def EQQ(self):
            return self.getToken(MiniLangParser.EQQ, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(MiniLangParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)


    class WhileStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MiniLangParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def DO(self):
            return self.getToken(MiniLangParser.DO, 0)
        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.NEWLINE)
            else:
                return self.getToken(MiniLangParser.NEWLINE, i)
        def TAB(self, i:int=None):
            if i is None:
                return self.getTokens(MiniLangParser.TAB)
            else:
                return self.getToken(MiniLangParser.TAB, i)
        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.StatContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.StatContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)



    def stat(self):

        localctx = MiniLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = MiniLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = MiniLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(MiniLangParser.ID)
                self.state = 15
                self.match(MiniLangParser.EQQ)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = MiniLangParser.IfStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(MiniLangParser.IF)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(MiniLangParser.THEN)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 22
                        self.match(MiniLangParser.NEWLINE)
                        self.state = 23
                        self.match(MiniLangParser.TAB)
                        self.state = 24
                        self.stat()

                    else:
                        raise NoViableAltException(self)
                    self.state = 27 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                self.state = 34
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 29
                    self.match(MiniLangParser.NEWLINE)
                    self.state = 30
                    self.match(MiniLangParser.ELSE)
                    self.state = 31
                    self.match(MiniLangParser.NEWLINE)
                    self.state = 32
                    self.match(MiniLangParser.TAB)
                    self.state = 33
                    self.stat()


                pass

            elif la_ == 4:
                localctx = MiniLangParser.WhileStatContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(MiniLangParser.WHILE)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(MiniLangParser.DO)
                self.state = 42 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 39
                        self.match(MiniLangParser.NEWLINE)
                        self.state = 40
                        self.match(MiniLangParser.TAB)
                        self.state = 41
                        self.stat()

                    else:
                        raise NoViableAltException(self)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 5:
                localctx = MiniLangParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(MiniLangParser.NEWLINE)
                pass

            elif la_ == 6:
                localctx = MiniLangParser.DeclareFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.match(MiniLangParser.DEF)
                self.state = 48
                self.match(MiniLangParser.ID)
                self.state = 49
                self.match(MiniLangParser.LPAREN)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 50
                    self.match(MiniLangParser.ID)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 51
                        self.match(MiniLangParser.COMMA)
                        self.state = 52
                        self.match(MiniLangParser.ID)
                        self.state = 57
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 60
                self.match(MiniLangParser.RPAREN)
                self.state = 61
                self.match(MiniLangParser.COLON)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 62
                        self.match(MiniLangParser.NEWLINE)
                        self.state = 63
                        self.match(MiniLangParser.TAB)
                        self.state = 64
                        self.stat()

                    else:
                        raise NoViableAltException(self)
                    self.state = 67 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 73
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 69
                    self.match(MiniLangParser.NEWLINE)
                    self.state = 70
                    self.match(MiniLangParser.TAB)
                    self.state = 71
                    self.match(MiniLangParser.RETURN)
                    self.state = 72
                    self.expr(0)


                pass

            elif la_ == 7:
                localctx = MiniLangParser.CallFunctionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.match(MiniLangParser.ID)
                self.state = 76
                self.match(MiniLangParser.LPAREN)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1703936) != 0):
                    self.state = 77
                    self.expr(0)
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==6:
                        self.state = 78
                        self.match(MiniLangParser.COMMA)
                        self.state = 79
                        self.expr(0)
                        self.state = 84
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 87
                self.match(MiniLangParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(MiniLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(MiniLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(MiniLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(MiniLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def ADD(self):
            return self.getToken(MiniLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniLangParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniLangParser.ExprContext,i)

        def EQ(self):
            return self.getToken(MiniLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(MiniLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MiniLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = MiniLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 91
                self.match(MiniLangParser.INT)
                pass
            elif token in [19]:
                localctx = MiniLangParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(MiniLangParser.ID)
                pass
            elif token in [17]:
                localctx = MiniLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(MiniLangParser.LPAREN)
                self.state = 94
                self.expr(0)
                self.state = 95
                self.match(MiniLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 108
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MiniLangParser.MulDivContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 100
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 101
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = MiniLangParser.AddSubContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 102
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 103
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 104
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = MiniLangParser.ComparisonContext(self, MiniLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 105
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 106
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 107
                        self.expr(5)
                        pass

             
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         





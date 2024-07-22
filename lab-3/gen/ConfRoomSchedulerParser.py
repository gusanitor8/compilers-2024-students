# Generated from ConfRoomScheduler.g4 by ANTLR 4.13.1
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
        4,1,16,82,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,71,8,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,84,0,9,1,0,0,0,2,
        22,1,0,0,0,4,70,1,0,0,0,6,72,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,
        11,1,0,0,0,11,9,1,0,0,0,11,12,1,0,0,0,12,1,1,0,0,0,13,14,3,4,2,0,
        14,15,5,15,0,0,15,23,1,0,0,0,16,17,3,6,3,0,17,18,5,15,0,0,18,23,
        1,0,0,0,19,20,5,11,0,0,20,23,5,15,0,0,21,23,5,15,0,0,22,13,1,0,0,
        0,22,16,1,0,0,0,22,19,1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,5,
        1,0,0,25,26,5,14,0,0,26,27,5,2,0,0,27,28,5,14,0,0,28,29,5,3,0,0,
        29,30,5,9,0,0,30,31,5,4,0,0,31,32,5,10,0,0,32,33,5,5,0,0,33,34,5,
        10,0,0,34,35,5,6,0,0,35,71,5,12,0,0,36,37,5,2,0,0,37,38,5,14,0,0,
        38,39,5,3,0,0,39,40,5,9,0,0,40,41,5,4,0,0,41,42,5,10,0,0,42,43,5,
        5,0,0,43,44,5,10,0,0,44,45,5,6,0,0,45,71,5,12,0,0,46,47,5,2,0,0,
        47,48,5,14,0,0,48,49,5,3,0,0,49,50,5,9,0,0,50,51,5,4,0,0,51,52,5,
        10,0,0,52,53,5,5,0,0,53,54,5,10,0,0,54,55,5,6,0,0,55,56,5,12,0,0,
        56,57,5,7,0,0,57,71,5,13,0,0,58,59,5,1,0,0,59,60,5,14,0,0,60,61,
        5,2,0,0,61,62,5,14,0,0,62,63,5,3,0,0,63,64,5,9,0,0,64,65,5,4,0,0,
        65,66,5,10,0,0,66,67,5,5,0,0,67,68,5,10,0,0,68,69,5,6,0,0,69,71,
        5,12,0,0,70,24,1,0,0,0,70,36,1,0,0,0,70,46,1,0,0,0,70,58,1,0,0,0,
        71,5,1,0,0,0,72,73,5,8,0,0,73,74,5,14,0,0,74,75,5,3,0,0,75,76,5,
        9,0,0,76,77,5,4,0,0,77,78,5,10,0,0,78,79,5,5,0,0,79,80,5,10,0,0,
        80,7,1,0,0,0,3,11,22,70
    ]

class ConfRoomSchedulerParser ( Parser ):

    grammarFileName = "ConfRoomScheduler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'NOMBRE'", "'RESERVAR'", "'PARA'", "'DE'", 
                     "'A'", "'TYPE'", "'DESC'", "'CANCELAR'", "<INVALID>", 
                     "<INVALID>", "'LISTAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DATE", "TIME", "LIST", "ROOMTYPE", "DESC", 
                      "ID", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_reserve = 2
    RULE_cancel = 3

    ruleNames =  [ "prog", "stat", "reserve", "cancel" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    DATE=9
    TIME=10
    LIST=11
    ROOMTYPE=12
    DESC=13
    ID=14
    NEWLINE=15
    WS=16

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
                return self.getTypedRuleContexts(ConfRoomSchedulerParser.StatContext)
            else:
                return self.getTypedRuleContext(ConfRoomSchedulerParser.StatContext,i)


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ConfRoomSchedulerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35078) != 0)):
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
            return ConfRoomSchedulerParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class ListStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LIST(self):
            return self.getToken(ConfRoomSchedulerParser.LIST, 0)
        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListStat" ):
                listener.enterListStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListStat" ):
                listener.exitListStat(self)


    class ReserveStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reserve(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.ReserveContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveStat" ):
                listener.enterReserveStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveStat" ):
                listener.exitReserveStat(self)


    class CancelStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cancel(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.CancelContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancelStat" ):
                listener.enterCancelStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancelStat" ):
                listener.exitCancelStat(self)



    def stat(self):

        localctx = ConfRoomSchedulerParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                localctx = ConfRoomSchedulerParser.ReserveStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.reserve()
                self.state = 14
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [8]:
                localctx = ConfRoomSchedulerParser.CancelStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.cancel()
                self.state = 17
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [11]:
                localctx = ConfRoomSchedulerParser.ListStatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(ConfRoomSchedulerParser.LIST)
                self.state = 20
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [15]:
                localctx = ConfRoomSchedulerParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReserveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_reserve

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReserveNoNameContext(ReserveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.ReserveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)
        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)
        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)
        def ROOMTYPE(self):
            return self.getToken(ConfRoomSchedulerParser.ROOMTYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveNoName" ):
                listener.enterReserveNoName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveNoName" ):
                listener.exitReserveNoName(self)


    class ReserveWithNameContext(ReserveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.ReserveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ConfRoomSchedulerParser.ID, 0)
        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)
        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)
        def ROOMTYPE(self):
            return self.getToken(ConfRoomSchedulerParser.ROOMTYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveWithName" ):
                listener.enterReserveWithName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveWithName" ):
                listener.exitReserveWithName(self)


    class ReserveNoNameDescContext(ReserveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.ReserveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ConfRoomSchedulerParser.ID, 0)
        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)
        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)
        def ROOMTYPE(self):
            return self.getToken(ConfRoomSchedulerParser.ROOMTYPE, 0)
        def DESC(self):
            return self.getToken(ConfRoomSchedulerParser.DESC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveNoNameDesc" ):
                listener.enterReserveNoNameDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveNoNameDesc" ):
                listener.exitReserveNoNameDesc(self)


    class ReserveNameDescContext(ReserveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.ReserveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.ID)
            else:
                return self.getToken(ConfRoomSchedulerParser.ID, i)
        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)
        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)
        def ROOMTYPE(self):
            return self.getToken(ConfRoomSchedulerParser.ROOMTYPE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveNameDesc" ):
                listener.enterReserveNameDesc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveNameDesc" ):
                listener.exitReserveNameDesc(self)



    def reserve(self):

        localctx = ConfRoomSchedulerParser.ReserveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_reserve)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ConfRoomSchedulerParser.ReserveNoNameContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(ConfRoomSchedulerParser.T__0)
                self.state = 25
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 26
                self.match(ConfRoomSchedulerParser.T__1)
                self.state = 27
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 28
                self.match(ConfRoomSchedulerParser.T__2)
                self.state = 29
                self.match(ConfRoomSchedulerParser.DATE)
                self.state = 30
                self.match(ConfRoomSchedulerParser.T__3)
                self.state = 31
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 32
                self.match(ConfRoomSchedulerParser.T__4)
                self.state = 33
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 34
                self.match(ConfRoomSchedulerParser.T__5)
                self.state = 35
                self.match(ConfRoomSchedulerParser.ROOMTYPE)
                pass

            elif la_ == 2:
                localctx = ConfRoomSchedulerParser.ReserveWithNameContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(ConfRoomSchedulerParser.T__1)
                self.state = 37
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 38
                self.match(ConfRoomSchedulerParser.T__2)
                self.state = 39
                self.match(ConfRoomSchedulerParser.DATE)
                self.state = 40
                self.match(ConfRoomSchedulerParser.T__3)
                self.state = 41
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 42
                self.match(ConfRoomSchedulerParser.T__4)
                self.state = 43
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 44
                self.match(ConfRoomSchedulerParser.T__5)
                self.state = 45
                self.match(ConfRoomSchedulerParser.ROOMTYPE)
                pass

            elif la_ == 3:
                localctx = ConfRoomSchedulerParser.ReserveNoNameDescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(ConfRoomSchedulerParser.T__1)
                self.state = 47
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 48
                self.match(ConfRoomSchedulerParser.T__2)
                self.state = 49
                self.match(ConfRoomSchedulerParser.DATE)
                self.state = 50
                self.match(ConfRoomSchedulerParser.T__3)
                self.state = 51
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 52
                self.match(ConfRoomSchedulerParser.T__4)
                self.state = 53
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 54
                self.match(ConfRoomSchedulerParser.T__5)
                self.state = 55
                self.match(ConfRoomSchedulerParser.ROOMTYPE)
                self.state = 56
                self.match(ConfRoomSchedulerParser.T__6)
                self.state = 57
                self.match(ConfRoomSchedulerParser.DESC)
                pass

            elif la_ == 4:
                localctx = ConfRoomSchedulerParser.ReserveNameDescContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 58
                self.match(ConfRoomSchedulerParser.T__0)
                self.state = 59
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 60
                self.match(ConfRoomSchedulerParser.T__1)
                self.state = 61
                self.match(ConfRoomSchedulerParser.ID)
                self.state = 62
                self.match(ConfRoomSchedulerParser.T__2)
                self.state = 63
                self.match(ConfRoomSchedulerParser.DATE)
                self.state = 64
                self.match(ConfRoomSchedulerParser.T__3)
                self.state = 65
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 66
                self.match(ConfRoomSchedulerParser.T__4)
                self.state = 67
                self.match(ConfRoomSchedulerParser.TIME)
                self.state = 68
                self.match(ConfRoomSchedulerParser.T__5)
                self.state = 69
                self.match(ConfRoomSchedulerParser.ROOMTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CancelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConfRoomSchedulerParser.ID, 0)

        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_cancel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancel" ):
                listener.enterCancel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancel" ):
                listener.exitCancel(self)




    def cancel(self):

        localctx = ConfRoomSchedulerParser.CancelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cancel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ConfRoomSchedulerParser.T__7)
            self.state = 73
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 74
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 75
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 76
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 77
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 78
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 79
            self.match(ConfRoomSchedulerParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






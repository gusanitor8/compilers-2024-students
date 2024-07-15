grammar MiniLang;

prog:   stat+ ;

stat:   expr NEWLINE                                                        # printExpr
    |   INTR ID EQQ expr NEWLINE                                            # assignInt
    |   STR ID EQQ expr NEWLINE                                             # assignStr
    |   IF expr THEN (NEWLINE TAB stat)+ (NEWLINE ELSE NEWLINE TAB stat)?   # ifStat
    |   WHILE expr DO (NEWLINE TAB stat)+                                   # whileStat
    |   NEWLINE                                                             # blank
    |   DEF ID LPAREN (ID (COMMA ID)*)? RPAREN COLON (NEWLINE TAB stat)+ (NEWLINE TAB RETURN expr)?    # declareFunction
    |   ID LPAREN (expr (COMMA expr)*)? RPAREN                              # callFunction
    ;



expr:   expr (MUL|DIV) expr          # MulDiv
    |   expr (ADD|SUB) expr          # AddSub
    |   expr (EQ|NEQ) expr        # Comparison
    |   INT                          # int
    |   ID                           # id
    |   LPAREN expr RPAREN           # parens
    ;

IF : 'if' ; // match if
THEN : 'then' ; // match then
ELSE : 'else' ; // match else
WHILE : 'while' ; // match while
DO : 'do' ; // match do
COMMA : ',' ; // match comma
COLON : ':' ; // match colon
DEF : 'def' ; // match def
RETURN : 'return' ; // match return

MUL : '*' ; // define token for multiplication
DIV : '/' ; // define token for division
ADD : '+' ; // define token for addition
SUB : '-' ; // define token for subtraction

EQ : '==' ; // define token for equality
NEQ : '!=' ; // define token for inequality
EQQ : '=' ; // define token for assignment

LPAREN : '(' ; // define token for left parenthesis
RPAREN : ')' ; // define token for right parenthesis

ID  : [a-zA-Z]+ ; // match identifiers
INT : [0-9]+ ; // match integers

//data types
INTR : 'int' ;
STR : 'str' ;

TAB : '    ' ; // toss out tabs
NEWLINE:'\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS  : [ \t]+ -> skip ; // toss out whitespace
COMM : '//' .*? '\n' -> skip ; // toss out comments
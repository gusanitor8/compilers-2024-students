grammar ConfRoomScheduler;

prog: stat+ ;

stat: reserve NEWLINE                # reserveStat
    | cancel NEWLINE                 # cancelStat
    | LIST NEWLINE                   # listStat
    | NEWLINE                        # blank
    ;

reserve: 'NOMBRE' ID 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'TYPE' ROOMTYPE   #reserveNoName
    | 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'TYPE' ROOMTYPE                  #reserveWithName
    | 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'TYPE' ROOMTYPE 'DESC' DESC      #reserveNoNameDesc
    | 'NOMBRE' ID 'RESERVAR' ID 'PARA' DATE 'DE' TIME 'A' TIME 'TYPE' ROOMTYPE      #reserveNameDesc
    ;


cancel: 'CANCELAR' ID 'PARA' DATE 'DE' TIME 'A' TIME ;

DATE: DIGIT DIGIT '/' DIGIT DIGIT '/' DIGIT DIGIT DIGIT DIGIT ; 
TIME: DIGIT DIGIT ':' DIGIT DIGIT ;
LIST: 'LISTAR' ;
ROOMTYPE: 'Sala' | 'Auditorio' | 'Laboratorio' ;
DESC : '"'[a-zA-Z0-9 ]+'"';
ID  : [a-zA-Z0-9]+ ; 
NEWLINE: '\r'? '\n' ; 
WS  : [ \t]+ -> skip ; 

fragment DIGIT : [0-9] ;

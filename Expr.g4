grammar Expr;

prog : star+ ;
star : expr NEWLINE                 # printExpr
     | VARIABLE '=' expr NEWLINE    # assign
	 | NEWLINE                      # blank
	 ;
expr : expr op=('*'|'/'|'^') expr   # mulDivPow
	 | expr op=('+'|'-') expr       # addSub
	 | FLOAT                        # number
	 | '-' FLOAT                    # minNumber
	 | VARIABLE                     # variable
	 | '(' expr ')'                 # parens
     ;

FLOAT : [0-9]+('.'[0-9]+)?;
VARIABLE : [a-zA-Z]+[0-9]* ;
MUL : '*' ; 
DIV : '/' ;
POW : '^' ;
ADD : '+' ;
SUB : '-' ;

NEWLINE : '\r'? '\n' ;
IGNORE : [ \t]+ -> skip ; // skip spaces, tabs

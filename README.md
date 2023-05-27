# antlr4-parser

First I needed to install ANTLR. I just followed instructions on [their website](https://www.antlr.org/). I used Python as programming language, but there are also other languages that are supported. For the Python, I also installed **antlr4-python3-runtime** with the following command `pip install antlr4-python3-runtime`, because Pyton interpreter couldn't locate antlr4 library.

I used this grammar(the file is also included in repository by the name **Expr.g4**):
```
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

```

I used the following command to create a project from the grammar: `antlr4 -no-listener -visitor -Dlanguage=Python3 .\Expr4.g4 -o dest`.

After that, I created `EvalVisitor.py` file, and override methods from `ExprParser`.

Next, I also created `Main.py` file, in which I inicialized all classes, and `example.expr` file, for examples.

For running the program, I used `python .\Main.py .\example.expr`.

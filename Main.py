import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalVisitor import EvalVisitor
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    print(tree.toStringTree(recog=parser))
    visitor = EvalVisitor()
    visitor.visit(tree)
 
if __name__ == '__main__':
    main(sys.argv)


# Run the Main.py file with the following command:
# python .\Main.py .\example.expr 
#
# RUn gui program with the following command:
# antlr4-parse .\Expr.g4 prog -gui
# Generated from .\Expr.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx:ExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assign.
    def visitAssign(self, ctx:ExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blank.
    def visitBlank(self, ctx:ExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#number.
    def visitNumber(self, ctx:ExprParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#minNumber.
    def visitMinNumber(self, ctx:ExprParser.MinNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#variable.
    def visitVariable(self, ctx:ExprParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSub.
    def visitAddSub(self, ctx:ExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDivPow.
    def visitMulDivPow(self, ctx:ExprParser.MulDivPowContext):
        return self.visitChildren(ctx)



del ExprParser
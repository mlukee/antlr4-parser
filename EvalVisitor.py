
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.memory = {} 
        
    def visitProg(self, ctx: ExprParser.ProgContext):
        return super().visitProg(ctx)
    
    def visitPrintExpr(self, ctx: ExprParser.PrintExprContext):
        value = self.visit(ctx.expr())
        print(value)
        return value
    
    def visitAssign(self, ctx: ExprParser.AssignContext):
        value = self.visit(ctx.expr())
        self.memory[ctx.VARIABLE().getText()] = value
        return value
    
    def visitBlank(self, ctx: ExprParser.BlankContext):
        return super().visitBlank(ctx)
    
    def visitNumber(self, ctx: ExprParser.NumberContext):
        return float(ctx.FLOAT().getText())
    
    def visitMinNumber(self, ctx: ExprParser.MinNumberContext):
        return -float(ctx.FLOAT().getText())
    
    def visitParens(self, ctx: ExprParser.ParensContext):
        return self.visit(ctx.expr())
    
    def visitVariable(self, ctx: ExprParser.VariableContext):
        var = ctx.VARIABLE().getText()
        value = self.memory.get(var)
        if value is None:
            raise NameError(var)
        return value
    
    def visitAddSub(self, ctx: ExprParser.AddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.ADD:
            return left + right
        return left - right
    
    def visitMulDivPow(self, ctx: ExprParser.MulDivPowContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == ExprParser.MUL:
            return left * right
        if ctx.op.type == ExprParser.DIV:
            return left / right
        return left ** right
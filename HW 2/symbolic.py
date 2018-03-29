# Ömer Mesud TOKER
# 21302479
# CS 315 - 2
# HW 2

def main():
	x = Var("x")
	y = Var("y")
	z = Var("z")
	e = 3 - (x - 2 / y) / z;

	print evaluate(x, x=3)
	print evaluate(e, {"x":3, "y":4, "z":2})
	print evaluate(e, x=3, y=-1, z=4)
	print

	print e.string() 
	print e.desc()
	print

	print x.string() 
	print x.desc()
	print

	#start of test for substraction division 
	print (x-3).string() 
	print (x-3).desc()
	print

	print (3-x).string() 
	print (3-x).desc()
	print

	print (y/(x-1)).string()
	print (y/(x-1)).desc()
	print

	print ((x-1)/y).string()
	print ((x-1)/y).desc()
	print

	print (x/y-3).string()
	print (x/y-3).desc()
	print

	print (x-y-3).string()
	print (x-y-3).desc()
	print

	print ((x-y)-3).string()
	print ((x-y)-3).desc()
	print

	print (x-(y-3)).string()
	print (x-(y-3)).desc()
	print

	print (((x)-y)/(3-x)).string()
	print (((x)-y)/(3-x)).desc()
	print

	print ((4 - 3 / x) / 3 - 5).string()
	print ((4 - 3 / x) / 3 - 5).desc()
	print
	#end of test for substraction and division

	#Testing derivative
	print derivative(2*x*x+3*x+5, x).string()
	print evaluate(derivative(2*x*x+3*x+5, x),x=4,y=5)
	print

	print derivative(2*x*x*x-3*x*x-5*x+5, x).string()
	print evaluate(derivative(2*x*x*x-3*x*x-5*x+5, x),x=4,y=5)
	print

	print derivative(x*x/y,x).string()
	print evaluate(derivative(x*x/y,x),x=25,y=16)
	print

	print derivative((x*x-2*x)/(x-1),x).string()
	print evaluate(derivative((x*x-2*x)/(x-1),x),x=25,y=16)
	print
	 
import operator
  
def evaluate(expr, mapValues={}, **namedValues):
    combined = dict(mapValues)
    combined.update(namedValues)
    return expr.eval(combined)

#common derivative definition
def derivative(expr, var):
    return expr.derivative(var)

class Expr:
    def eval(self, values):
        raise NotImplementedError()
    def desc(self):
        raise NotImplementedError()
    def string(self):
        raise NotImplementedError()

class VarExpr(Expr):
    def __init__(self, var):
        self.var = var
    def eval(self, values):
        return values[self.var.getName()]
    def desc(self):
        return "VarExpr("+self.var.desc()+")"
    def string(self):
        return self.var.getName()
    
    #derivative definition for VarExpr class
    def derivative(self, var):
        return self.var.derivative(var)


class LiteralExpr(Expr):
    def __init__(self, val):
        self.val = val
    def eval(self, values):
        return self.val  
    def desc(self): 
        return "LiteralExpr("+str(self.val)+")"
    def string(self):
        return str(self.val)
    def derivative(self, var):
        return LiteralExpr(0)
    
def opToSign(op):
    if (op == operator.__add__):
        return "+"
    #Adding sub
    if (op == operator.__sub__):
        return "-"
    if (op == operator.__div__):
        return "/"
    #Adding divide
    if (op == operator.__mul__):
        return "*"
    raise NotImplementedError()

def opToPrecedence(op):
    #Editing precedence
    if (op == operator.__sub__ or op == operator.__add__):
        return 0
    if (op == operator.__div__ or op == operator.__mul__):
        return 1
    raise NotImplementedError()

class BinaryExpr(Expr):
    def __init__(self, op, lhs, rhs):
        self.op = op;
        self.lhs = lhs
        self.rhs = rhs
    def __add__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__add__, self, LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__add__, self, VarExpr(val))
        else:
            return BinaryExpr(operator.__add__, self, val)
    def __radd__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__add__, LiteralExpr(val), self)
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__add__, VarExpr(val), self)
        else:
            return BinaryExpr(operator.__add__, val, self)

    #Adding sub definition for BinaryExpr class
    def __sub__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__sub__, self, LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__sub__, self, VarExpr(val))
        else:
            return BinaryExpr(operator.__sub__, self, val)
        
    def __rsub__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__sub__, LiteralExpr(val), self)
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__sub__, VarExpr(val), self)
        else:
            return BinaryExpr(operator.__sub__, val, self)
        
    def __mul__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__mul__, self, LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__mul__, self, VarExpr(val))
        else:
            return BinaryExpr(operator.__mul__, self, val)
    def __rmul__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__mul__, LiteralExpr(val), self)
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__mul__, VarExpr(val), self)
        else:
            return BinaryExpr(operator.__mul__, val, self);

    #Adding div definition for BÝnaryExpr Class
    def __div__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__div__, self, LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__div__, self, VarExpr(val))
        else:
            return BinaryExpr(operator.__div__, self, val)
        
    def __rdiv__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__div__, LiteralExpr(val), self)
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__div__, VarExpr(val), self)
        else:
            return BinaryExpr(operator.__div__, val, self);

    #Adding derivative definition for BÝnaryExpr Class
    def derivative(self,var):
        if (self.op == operator.__mul__):
            return BinaryExpr(operator.__add__, BinaryExpr(operator.__mul__,self.lhs,self.rhs.derivative(var)),BinaryExpr(operator.__mul__,self.lhs.derivative(var),self.rhs))
        if (self.op == operator.__div__):
            return BinaryExpr(operator.__div__, BinaryExpr(operator.__sub__,
                                         BinaryExpr(operator.__mul__,
                                                    self.lhs.derivative(var),
                                                    self.rhs),
                                         BinaryExpr(operator.__mul__,
                                                    self.lhs,
                                                    self.rhs.derivative(var))),
                              BinaryExpr(operator.__mul__, self.rhs, self.rhs))
        return BinaryExpr(self.op,self.lhs.derivative(var),self.rhs.derivative(var))

    
    def eval(self, values):
        return self.op(self.lhs.eval(values), self.rhs.eval(values));
    def desc(self):
        return "BinaryExpr("+self.op.__name__+","+self.lhs.desc()+","+self.rhs.desc()+")"
    def string(self):
        res = "";
        if (isinstance(self.lhs, BinaryExpr) and 
            (opToPrecedence(self.lhs.op) < opToPrecedence(self.op))):
            res += "(" + self.lhs.string() + ")"
        else:
            res += self.lhs.string()
        res += opToSign(self.op)
        if (isinstance(self.rhs, BinaryExpr) and 
            (opToPrecedence(self.rhs.op) <= opToPrecedence(self.op))):
            res += "(" + self.rhs.string() + ")"
        else:
            res +=self.rhs.string()
        return res
    
class Var:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __add__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__add__, VarExpr(self), LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__add__, VarExpr(self), VarExpr(val))
        else:
            return BinaryExpr(operator.__add__, VarExpr(self), val)
    def __radd__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__add__, LiteralExpr(val), VarExpr(self))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__add__, VarExpr(val), VarExpr(self))
        else:
            return BinaryExpr(operator.__add__, val, VarExpr(self))

    #Adding sub definition for Var class
    def __sub__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__sub__, VarExpr(self), LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__sub__, VarExpr(self), VarExpr(val))
        else:
            return BinaryExpr(operator.__sub__, VarExpr(self), val)
        
    def __rsub__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__sub__, LiteralExpr(val), VarExpr(self))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__sub__, VarExpr(val), VarExpr(self))
        else:
            return BinaryExpr(operator.__sub__, val, VarExpr(self))

        
    def __mul__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__mul__, VarExpr(self), LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__mul__, VarExpr(self), VarExpr(val))
        else:
            return BinaryExpr(operator.__mul__, VarExpr(self), val)
    def __rmul__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__mul__, LiteralExpr(val), VarExpr(self))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__mul__, VarExpr(val), VarExpr(self))
        else:
            return BinaryExpr(operator.__mul__, val, VarExpr(self))

    #Adding div definition for Var class
    def __div__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__div__, VarExpr(self), LiteralExpr(val))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__div__, VarExpr(self), VarExpr(val))
        else:
            return BinaryExpr(operator.__div__, VarExpr(self), val)
        
    def __rdiv__(self, val):
        if (isinstance(val, int)):
            return BinaryExpr(operator.__div__, LiteralExpr(val), VarExpr(self))
        elif (isinstance(val, Var)):
            return BinaryExpr(operator.__div__, VarExpr(val), VarExpr(self))
        else:
            return BinaryExpr(operator.__div__, val, VarExpr(self))

    #Adding derivative definition for Var class
    def derivative(self, var):
        if (self.name == var.name):
            return LiteralExpr(1)
        else:
            return LiteralExpr(0)
        
    def eval(self, values):
        return values[self.name]
    def desc(self):
        return "Var("+self.name+")"   
    def string(self):
        return self.name
    
if __name__ == '__main__':
    main()

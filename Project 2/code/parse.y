// Define the tokens

%token STAR
%token PDCOLOR
%token SPACE
%token ASSIGN
%token PLUS
%token MINUS
%token MUL
%token DIV
%token COMMA
%token AND
%token OR
%token LT
%token GT
%token LTE
%token GTE
%token NOT
%token POW
%token LPARAM
%token RPARAM
%token LBRACE
%token RBRACE
%token LBRACKET
%token RBRACKET
%token DIGIT
%token LETTER
%token NEWLINE
%token NONSTAR
%token NONSTARNONDIV
%token NONNEWLINE
%token UNDERSCORE
%token STRING
%token BOOL
%token PRECOLOR
%token ID
%token INT
%token FLOAT
%token NEWOBJECT
%token FOR
%token WHILE
%token BREAK
%token CONTINUE
%token FUNCTION
%token IF
%token ELSE
%token ELSEIF
%token RETURN
%token ENDSTMT
%token EQUAL
%token NOTEQUAL


// Define the union that can hold different values for the tokens
 
%union 
{
  char * string;
  int integer;
}

// Define the token value types

%type <string> ID
// define associativity of operations

%left PLUS MINUS // the order defines precedence, 
%left STAR DIV // so * and / has higher precedence than + and -

%{ 
  #include <iostream> 
  #include <string>
  #include <set>
  using namespace std;
  // forward declarations
  extern int yylineno;
  void yyerror(string);
  int yylex(void);
  int errors;
  set<string> var_sym;
  set<string> func_sym;
%}

%%

program :
	func_list

func_list:
	func_def func_list |

stmt_list:
	statement stmt_list |

statement:
    expr ENDSTMT |
	expr error {yyerror("expected ';'");} |
	for_stmt |
	while_stmt |
	newObject_def |
	if_stmt

expr:
	func_call |
	return_stmt |
	assignment |
	array_def

return_stmt:
	RETURN |
	RETURN art_expr

array:
	ID LBRACKET art_expr RBRACKET {if(var_sym.count(string($1))==0) yyerror("array " + string($1) + " is not defined");}|
	ID LBRACKET error RBRACKET {yyerror("a valid arithmetic expression expected between '[' and ']'");}

blocklist:
	LBRACE arg_list RBRACE |
	LBRACE arg_list error ENDSTMT {yyerror("expected '}'");}

array_def:
	ID LBRACKET art_expr RBRACKET ASSIGN blocklist {var_sym.insert(string($1));} |
	ID LBRACKET art_expr RBRACKET ASSIGN rhs {var_sym.insert(string($1));} |
	ID LBRACKET error RBRACKET ASSIGN rhs {yyerror("a valid arithmetic expression expected between '[' and ']'");}

newObject_def:
	NEWOBJECT ID LPARAM param_list RPARAM LBRACE stmt_list RBRACE {func_sym.insert(string($2));}

func_def:
	FUNCTION ID LPARAM param_list RPARAM LBRACE stmt_list RBRACE {func_sym.insert(string($2));}

func_call:
	ID LPARAM arg_list RPARAM {if(func_sym.count(string($1))==0) yyerror("function " + string($1) + " is not defined");}

param_list:
	param param_list_tail |

param_list_tail:
	COMMA param param_list_tail |

param:
	ID {var_sym.insert(string($1));} |
	ID ASSIGN rhs {var_sym.insert(string($1));}

assignment:
	ID ASSIGN rhs {var_sym.insert(string($1));} |
	ID PLUS PLUS {if(var_sym.count($1)==0) yyerror("variable " + string($1) + " is not defined");}|
	ID MINUS MINUS {if(var_sym.count($1)==0) yyerror("variable " + string($1) + " is not defined");}

rhs:
	art_expr |
	conditional

arg_list:
	arg arg_list_tail |
		

arg_list_tail:
	COMMA arg arg_list_tail |

arg:
	rhs

art_expr:
	art_expr add term |
	term

term:
	term mul factor |
	factor

factor:
	operand |
	LPARAM art_expr RPARAM

add:
   PLUS |
	MINUS

mul:
	STAR |
	DIV

operand:
	PRECOLOR |
	integer |
	float |
	array |
	variable |
	func_call

float:
	FLOAT |
	MINUS FLOAT |
	PLUS FLOAT

integer:
	INT |
	MINUS INT |
	PLUS INT

boolean:
	BOOL |
	NOT BOOL

bool_op:
	AND |
	OR |
	LT |
	GT |
	LTE |
	GTE |
	EQUAL |
	NOTEQUAL

variable:
	ID {if(var_sym.count($1)==0) yyerror("variable " + string($1) + " is not defined");}

for_stmt:
	FOR LPARAM assignment ENDSTMT loop_cond ENDSTMT assignment RPARAM LBRACE stmt_list RBRACE

loop_cond:
	conditional |
	func_call |
	variable |
	error {yyerror("conditional expression expected");}

while_stmt:
	WHILE LPARAM loop_cond RPARAM LBRACE stmt_list RBRACE

conditional:
	boolean |
	boolean bool_op conditional |
	boolean bool_op art_expr |
	art_expr bool_op conditional |
	art_expr bool_op art_expr |
	LPARAM conditional RPARAM


if_stmt:
	IF LPARAM loop_cond RPARAM LBRACE stmt_list RBRACE else_stmt

else_stmt:
	ELSE LBRACE stmt_list RBRACE |



%%

// report errors
extern int yylineno;
void yyerror(string s) 
{
	errors++;
	cout << "error at line " << yylineno << ": " << s << endl;
}
int main()
{
	errors=0;
	func_sym.insert("Oval");
	func_sym.insert("Stroke");
	func_sym.insert("Rectangle");
	func_sym.insert("Line");
	func_sym.insert("draw");
	func_sym.insert("Size");
	func_sym.insert("Color");
	func_sym.insert("Location");
	func_sym.insert("fillColor");
	func_sym.insert("fillState");
	func_sym.insert("drawString");
	func_sym.insert("drawShapeNTimes");
	var_sym.insert("HEIGHT");
	var_sym.insert("WIDTH");
	yyparse();
	
	if(errors>0) 
		cout << "Parsing completed with " << errors << " errors" <<endl;
	else 
		cout << "Parsing completed successfully" <<endl;
		
	return 0;
}


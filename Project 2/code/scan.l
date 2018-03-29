%{
#include<iostream>
#include "y.tab.h"
using namespace std;
int yyparse();
%}
%option yylineno

NEWLINE \n
SPACE [ \t]+
ASSIGN =
PLUS \+
MINUS -
MUL \*
DIV \/
COMMA ,
QUESTION \?
LT <
GT >
LTE <=
GTE >=
NOT !
EQUAL ==
NOTEQUAL !=
POW \^
LPARAM \(
RPARAM \)
LBRACE \{
RBRACE \}
LBRACKET \[
RBRACKET \]
DIGIT [0-9]
LETTER [a-zA-Z]
NONSTAR [^\*]
NONSTARNONDIV [^\*/]
NONNEWLINE [^\n]
UNDERSCORE _
AND &&
OR \|\|
STRING \"([^\\\"]|\\\\|\\\"|\\t|\\n)*\"
BOOL true|false
PRECOLOR BLACK|WHITE|GREEN|RED|YELLOW|ORANGE|BLUE
ID ({LETTER}|{UNDERSCORE})({LETTER}|{DIGIT}|{UNDERSCORE})*
INT {DIGIT}+
FLOAT {DIGIT}*("."{DIGIT}|{DIGIT}"."){DIGIT}*
NEWOBJECT newObject
FOR for
WHILE while
BREAK break
CONTINUE continue
FUNCTION function
IF if
ELSE else
ELSEIF "else if"
RETURN return
ENDSTMT ;
COMMENT {DIV}{DIV}{NONNEWLINE}*{NEWLINE}|{DIV}\*({NONSTAR}|\*+{NONSTARNONDIV})*\*+{DIV}
%%
{NEWLINE} ;
{SPACE} ;
{COMMENT} ;
{NEWOBJECT} return NEWOBJECT;
{FUNCTION} return FUNCTION;
{IF} return IF;
{ELSE} return ELSE;
{ELSEIF} return ELSEIF;
{RETURN} return RETURN;
{FOR} return FOR;
{ENDSTMT} return ENDSTMT;
{CONTINUE} return CONTINUE;
{BREAK} return BREAK;
{WHILE} return WHILE;
{COMMA} return COMMA;
{ASSIGN} return ASSIGN;
{AND} return AND;
{OR} return OR;
{EQUAL} return EQUAL;
{NOTEQUAL} return NOTEQUAL;
{NOT} return NOT;
{LTE} return LTE;
{GTE} return GTE;
{LT} return LT;
{GT} return GT;
{POW} return POW;
{LBRACE} return LBRACE;
{RBRACE} return RBRACE;
{PLUS} return PLUS;
{MINUS} return MINUS;
{MUL} return STAR;
{DIV} return DIV;
{LPARAM} return LPARAM;
{RPARAM} return RPARAM;
{LBRACKET} return LBRACKET;
{RBRACKET} return RBRACKET;
{PRECOLOR} return PRECOLOR;
{STRING} return STRING;
{BOOL} return BOOL;
{INT} return INT;
{FLOAT} return FLOAT;
{ID} {yylval.string=strdup(yytext);return ID;};
%%
int yywrap()
{
	return 1;
}

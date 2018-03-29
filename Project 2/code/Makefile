all: lexer parser
	g++ y.tab.c lex.yy.c -o parser

lexer: scan.l
	flex scan.l

parser: parse.y
	yacc -d parse.y


clean:
	-rm -f y.tab.h
	-rm -f parse.c
	-rm -f y.tab.c
	-rm -f lex.yy.c
	-rm -f parser

CXX    = g++
LEX    = flex
PROG   = lexer
LF     = lex.yy.c

all: $(PROG)

$(LF): $(PROG).l
	$(LEX) $(PROG).l  

$(PROG): $(LF)
	$(CXX) -o $(PROG) $(LF) -lfl

test: input
	cat input | ./$(PROG)

clean:
	-rm -f $(LF)
	-rm -f $(PROG)


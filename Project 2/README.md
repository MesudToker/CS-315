Graph Definition and Querying Language - Part II
In Part II, we ask you to develop BNF grammars for your languages (one for the graph definition language and one for the graph query language) and implement them using yacc (there will be two parsers, one for the graph definition language and one for the graph query language). The parsers will either accept a given input program (a graph definition or a graph query) as correct, or output a list of erroneous lines.

Deliverables
(20pts.) The BNF grammars (one for the graph definition language and one for the graph query language)
(20pts.) The parsers (including code + Makefile) (one for the graph definition language and one for the graph query language)
(15pts) 3 sample graph definitions and 5 sample graph queries that are correct (your parsers should produce no errors for these)
(15pts.) Sample erroneous graph definitions illustrating 5 different kind of errors (your graph definition parser should produce errors for these)
(15pts.) Sample erroneous graph queries illustrating 5 different kind of errors (your graph query parser should produce errors for these)
(10pts.) The output from your parsers for the all the sample programs
(5pts.) A report describing the challenges you have faced and how you addressed them
Logistics
Once you are done, put your deliverables under a directory named group<GroupNo>_proj2 and make an archive from that directory. It is important that your code should compile without any issues using the make command. Once complete, it should output executables called 'definition_parser' and 'query_parser', which can be used to parse your sample inputs (graph definitions and graph queries). For example, the following Unix commands could be used:

  mkdir group<GroupNo>_proj2    
  cd group<GroupNo>_proj2
      mkdir code      # contains Makefile, lex, yacc, and C code
      mkdir samples   # contains the program samples
      (edit and test your files)
      ...
  cd ..
  tar -cvzf group<GroupNo>_proj2.tar.gz group<GroupNo>_proj2
Then e-mail this newly generated file (named group<GroupNo>_proj2.tar.gz) to your TA.

Reports in formats other than .pdf and .txt are not accepted.
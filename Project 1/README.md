Design a Graph Definition and Querying Language
You are asked to design a graph definition and querying language. There should be two parts to your language:

The graph definition language: This language would be used to define a graph, that is to specify the vertices and edges of the graph.
The graph querying language: This language is used to define regular path queries on the graph.
There are specific requirements for each part. These are listed below:

(45pts) The graph definition language should support:
(5pts) Defining directed graphs
(5pts) Defining undirected graphs
(10pts) Defining vertex properties
A vertex property is some data value associated with a vertex.
It should be possible to attach multiple properties to a vertex.
A property should be a (name, value) pair. For instance, if a vertex represents a student, then a vertex property could be (“id”, 19945656). Remember that there could be multiple such properties, such as: (“id”, 19945656), (“name”, “Ali Veli”), (“age”, 20).
(10pts) Defining edge properties
It should be possible to attach multiple properties to an edge.
(15pts) A dynamic type system for the property values (property names should be strings)
Support strings, integers, and floats as primitive types. For instance, in the earlier example, the “id” attribute was using an integer value, whereas the “name” attribute was using a “string” value.
Support lists, sets, and maps as collection types. For instance, it should be possible to have a property like: (“grades”, {“CS315”: 85, “CS101”: 90, “CS666”: 15}). This would be an example of a property, whose value is a map from strings to integers. Arbitrary nesting should be possible as well. For instance, we can have (“grades”, {“CS315”: [85, 80], “CS101”: [90, 98], “CS666”: [15, 3]}). This is an example where the value type is a map from a string to a list of integers.
(55pts) The graph querying language should support:
(30pts) Creating regular path queries. A regular path query is a regular expression specifying a path. A path is a series of edges. Importantly, we are not asking you to evaluate path queries. We are asking you to create a language to express them. A path query should be able to specify:
(10pts) Concatenation, alternation, and repetition.
(10pts) Filters as Boolean expressions, which are composed of predicates defined over edge properties as well as incident vertex properties. For instance, one may want to find all paths of length three (a path of three edges), where the start vertex of the first edge has a vertex property name=“CS”, the second edge has an edge property code=“315”, and finally the third edge's end vertex has a vertex property kind=“rulez!”.
(10pts) Support for existence predicates as well as arithmetic expressions and functions in predicate expressions. For instance: an edge containing or not containing a property with a given name or value; or an edge that has a certain property whose value is greater than a constant threshold; or an edge that has a certain property whose value is a string that starts with “A” (this would require a string indexing function).
(15pts) Support having variables in path expressions. For instance, you may want to query all paths of length two where both edges in the path have a property called name with the same property value, but the value is not known. In this case, that value becomes a variable.
(10pts) Support modularity, that is dividing regular path queries into multiple pieces that are specified separately. This would require giving names to each piece and being able to use those names in a higher-level query.
We ask you to:

(80%) Design a language (give it a name) to meet the requirements described above.
(35%) Write a tutorial for the language you have designed. The tutorial's goal is to teach your language to someone who does not know about it.
(35%) Write a report describing how you addressed each requirement. For each requirement that has points associated with it, provide a small code segment in the language you designed, showcasing your design. If you like, you can also reference parts of your tutorial in the report.
(10%) Write 2 sample graph definitions (one directed, one undirected), and 10 queries.
(20%) Write a lexer for your language (you might write separate lexers for the definition and querying, it is up to you), using Lex.
Important Note
If there are parts you do not understand, you can come to the office hours or ask during the lecture breaks. This project has been given last semester as well. However, the results were not promising. This year, additional descriptions have been added to make certain aspects more clear.

Logistics
Once you are done, put your deliverable under a directory named group<GroupNo>_proj1 and make an archive from that directory. It is important that your code should compile without any issues using the make command. Once complete, it should output an executable called 'lexer' that can be used to lex your sample input. For example, the following Unix commands could be used:

  mkdir group<GroupNo>_proj1    
  cd group<GroupNo>_proj1
      mkdir code      # contains Makefile, lex, and C code
      mkdir samples   # contains the program samples
      mkdir documents # contains the tutorial and report
      (edit and test your files)
      ...
  cd ..
  tar -cvzf group<GroupNo>_proj1.tar.gz group<GroupNo>_proj1
Then e-mail this newly generated file (named group<GroupNo>_proj1.tar.gz) to your TA.

Reports in formats other than .pdf and .txt are not accepted.
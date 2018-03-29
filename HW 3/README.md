Homework III (Sections 1 and 2)
In the class, as part of the concurrency topic, we have studied the implementation of a search method in the context of the Needle in the Haystack problem. The signature of the method was as follows:

static <T> List<Integer> search(T needle, T[] haystack, int numThreads)

The goal was to find all indices in the array haystack that contains a needle. As part of this homework, we are asking you to implement a similar search method that returns the index of the first needle found. Importantly, you should stop all the threads as soon as a needle is found, so as to minimize the search time. The signature for this new search method would look like as follows:

static <T> int search(T needle, T[] haystack, int numThreads)

A few hints on the implementation:

- You can use a conditional variable to signal the control thread that an item is found. This conditional variable could be created by the controller thread and passed as an argument to the constructors of the searchers.

- You can stop a searcher thread from the control thread by making a function call that sets an atomic boolean variable named done maintained by the searcher to true. This same variable could be checked within the main search loop to early terminate the search.

It is recommended that you implement the homework in Java or C++.

Logistics
Put your code under a directory named lastname_name_hw3 and make an archive from that directory. For example, the following Unix commands could be used:
    mkdir lastname_name_hw3
    cd lastname_name_hw3
        ...
        (edit and test your files in this directory)
        ...
    cd ..
    tar -cvzf lastname_name_hw3.tar.gz lastname_name_hw3
Then e-mail this newly generated file (named lastname_name_hw3.tar.gz) to your TA.

Collaboration on the homework is not allowed. Reports in formats other than .txt and .pdf are not accepted.
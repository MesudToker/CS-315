//Ömer Mesud TOKER
// 21302479
// CS 315 - 2
// HW 3

import java.util.ArrayList;

public class Searcher 
{  
  public static <T> int search(T needle, T[] haystack, int numThreads)
  {  
    // List of Threads to search on the array
    ArrayList<SearchThread<T>> searchers = new ArrayList<SearchThread<T>>();
    
    // -1 means needle is not found
    int result = -1;
    
    // Each Thread is given equal items to search
    int numItemsPerThread = haystack.length / numThreads;
    
    // Result of above arithmetic may round up to an integer and some extra items could be left
    int extraItems = haystack.length - numItemsPerThread * numThreads;
    
    for (int i = 0, start = 0; i < numThreads; i++) {
      int numItems;
      
      if(i < extraItems)
        numItems = numItemsPerThread + 1;
      
      else
        numItems = numItemsPerThread;
      
      searchers.add(new SearchThread<T>(needle, haystack, start, start + numItems, false));
      start += numItems;
    }
    
    for(int i = 0; i < searchers.size(); i++) {
      searchers.get(i).run();
    }
    
    boolean flag = false;
    while(!flag) {
      for(int i = 0; i < searchers.size(); i++) {
        if(!searchers.get(i).isAlive()) {
          result = searchers.get(i).getResult();
          
          // Stop all threads
          for (int j = 0; j < searchers.size(); j++) {
            searchers.get(j).setDone(true);
            searchers.get(j).interrupt();
          }
          flag = true;
          break;
        }
      }           
    }
    return result;
  }
}

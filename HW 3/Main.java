//Ömer Mesud TOKER
// 21302479
// CS 315 - 2
// HW 3

import java.util.Random;

public class Main {
  
  public static void main(String[] args) throws InterruptedException
  {
    int numItems = 100000;
    Integer[] haystack = new Integer[numItems];
    
    Random random = new Random();
    
    // Setting elements of haystack array randomly from 1 to 10000
    for (int i = 0; i < numItems; i++) {
      haystack[i] = random.nextInt(10000) + 1;  
    }
    
    int needle = 123; 
    int numThreads = 5;
    
    int index  = Searcher.search(needle, haystack, numThreads);
    
    if(index != -1)
      System.out.println("Integer " + haystack[index] + " is first found at index " + index + "!");
    else
      System.out.println("Integer " + needle + " is not found in the haystack!");
  }
}

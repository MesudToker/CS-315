//Ömer Mesud TOKER
// 21302479
// CS 315 - 2
// HW 3

public class SearchThread<T> extends Thread 
{
  private T needle;
  private T[] haystack;
  private int start, end;
  private int result = -1;
  private boolean done;
  
  
  public SearchThread(T needle, T[] haystack, int start, int end, boolean done) {
    this.needle = needle;
    this.haystack = haystack;
    this.start = start;
    this.end = end;
    this.done = done;    
  }
  
  public void setDone(boolean done) {
    this.done = done;
  }
  
  public int getResult() {
    return result;
  }
  
  public void run() {
    for (int i = start; i < end; ++i) {
      if(!done) {
        if (haystack[i].equals(needle)) {
          result = i;
          break;
        } 
      }
      else
        break;       
    }
  }   
}

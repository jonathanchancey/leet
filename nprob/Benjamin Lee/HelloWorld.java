//*******************************************************************
// Welcome to CompileJava!
// If you experience any issues, please contact us ('More Info')  -->
// Sorry that the "Paste" feature no longer works! GitHub broke it.
//*******************************************************************

import java.lang.Math; // headers MUST be above the first class
import java.util.*;

// one class needs to have a main() method
public class HelloWorld
{
  // arguments are passed using the text field below this editor
  public static void main(String[] args)
  {
    int[] n = {1, 2, 3, 4};
    double[] p = {0.1, 0.5, 0.2, 0.2};
    
	List<Integer> numbers = new ArrayList<Integer>();
    for (int i = 0; i < 1000; i++) {
      numbers.add(getNumber(n, p));
    }
    
    System.out.println(getProbability(numbers));
    
  }
  
  public static int getNumber(int[] n, double[] probabilities) {
	double[] values = new double[probabilities.length];
	double temp = 0;
	for (int i = 0; i < probabilities.length; i++) {
		temp += probabilities[i];
		values[i] = temp;
	}
	
	double roll = Math.random();
	for (int i = 0; i < values.length; i++) {
		if (roll < values[i]) {
			return n[i];
		}
	}
    return -1;
  }
  
  public static Map<Integer, Integer> getProbability(List<Integer> n) {
    Map<Integer, Integer> result = new HashMap<Integer, Integer>();
    for (int num: n) {
      result.put(num, result.getOrDefault(num, 0) + 1);
    }
    return result;
  }
}


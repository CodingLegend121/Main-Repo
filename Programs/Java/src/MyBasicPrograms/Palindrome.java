package MyBasicPrograms;
import java.util.Scanner;
public class Palindrome {	
	public static void main(String[] args){		
		Scanner input = new Scanner(System.in);
		System.out.println("Enter a word");
		String word = input.nextLine();
		System.out.println("________________________________");
		String wordBack = new StringBuffer(word).reverse().toString();
				System.out.println(wordBack);			
				if(word.equals(wordBack)){
					System.out.println("It is a palindrome");
				}
				else{
					System.out.println("It is NOT a palindrome");
				}		
	}
}
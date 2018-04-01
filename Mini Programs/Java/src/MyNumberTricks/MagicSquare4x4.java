package MyNumberTricks;
import java.util.Scanner;
public class MagicSquare4x4 {	
	public static void main(String[] args) {	
	System.out.println("I will make a magic square...");
	Scanner num = new Scanner(System.in);
	System.out.println("Type a number between 22 - 99.");
	int magic = num.nextInt();	
	System.out.println("Your Magic Square is...");
	System.out.println("---------------------");	
	System.out.println("| "+(magic-20)+" | 1  | 12 | 7  |");
	System.out.println("---------------------");
	System.out.println("| 11 | 8  | "+(magic-21)+" | 2  |");
	System.out.println("---------------------");
	System.out.println("| 5  | 10 | 3  | "+(magic-18)+" |");
	System.out.println("---------------------");
	System.out.println("| 4  | "+(magic-19)+" | 6  | 9  |");
	System.out.println("---------------------");
	System.out.println("Write it in a piece of paper.");
	System.out.println("There are 28 possible combinations!!!");

}
}
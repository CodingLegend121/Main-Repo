package MyFirstPackage;
import java.util.Scanner;
public class MyClass1 {
public static void main(String[] args) {
		
		Scanner myFav = new Scanner(System.in);
		System.out.println("Enter your favorite number");
		int Num = myFav.nextInt();
		System.out.println("**************************");
		int i= 0;
		while(i<=Num){
			System.out.println(i);
			i++;
			}
		Scanner OddEve = new Scanner(System.in);
		System.out.println("Odd = false and Even = true");
		boolean style = OddEve.nextBoolean();
		style=false;
		if (style == true){
			
		while(i<=Num){
			i = 0;
			System.out.println(i);
			i= i +2;
		}
		}
		else{
			
			while(i<=Num){
			i = 1;
			System.out.println(i);
			i = i+2;
			}
		}
	
	
	
	}
}
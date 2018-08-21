package MyFirstPackage;

import java.util.Scanner;

public class Grades {
	
	
	public static void main(String[] args){
		
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter the Grade");
		int grade = scan.nextInt();
		System.out.println("<================>");
		int x;
		switch (grade){
		
		case 100:
			print("[A+] Outstanding");
			break;
		case 95:
			print("[A] Excellent");
			break;
		case 90:
			print("[A-] Awesome");
			break;
		case 85:
			print("[B] Great");
			break;
		case 80:
			print("[B-] Good");
			break;
		case 75:
			print("[C] Nice");
			break;
		case 70:
			print("[C-] Not Good");
			break;
		case 65:
			print("[D]Need to Improve");
			break;
		case 60:
			print("[F] Failure");
			break;
		case 55:
			print("[F-] You are Dumb");
			break;
		default:
			print("Grades not valid");
			break;
		}
	}

	public static void print(String word){
		System.out.println(word);
	}
}

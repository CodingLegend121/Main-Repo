
	package MyNumberTricks;

	import java.util.Scanner;

	public class Guess_Your_Number_Longer {
		
		public static void main(String[] args){
		
		System.out.println("Think of a number Between 1-60");
		Scanner one = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println(" 1, 3, 5, 7, 9");
		System.out.println("11,13,15,17,19");
		System.out.println("21,23,25,27,29");
		System.out.println("31,33,35,37,39");
		System.out.println("41,43,45,47,49");
		System.out.println("51,53,55,57,59");
		System.out.println("61,63,65,67,69");
		System.out.println("71,73,75,77,79");
		System.out.println("81,83,85,87,89");
		System.out.println("91,93,95,97,99");
		String card_one = one.nextLine();
		
		Scanner two = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println(" 2, 3, 6, 7,10");
		System.out.println("11,14,15,18,19");
		System.out.println("22,23,26,27,30");
		System.out.println("31,34,35,38,39");
		System.out.println("42,43,46,47,50");
		System.out.println("51,54,55,58,59");
		String card_two = two.nextLine();
		
		Scanner three = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println(" 4, 5, 6, 7,12");
		System.out.println("13,14,15,20,21");
		System.out.println("22,23,28,29,30");
		System.out.println("31,36,37,38,39");
		System.out.println("44,45,46,47,52");
		System.out.println("53,54,55,60");
		String card_three = three.nextLine();
		
		Scanner four = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println(" 8, 9,10,11,12");
		System.out.println("13,14,15,24,25");
		System.out.println("26,27,28,29,30");
		System.out.println("31,40,41,42,43");
		System.out.println("44,45,46,47,56");
		System.out.println("57,58,59,60");
		String card_four = four.nextLine();
		
		Scanner five = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println("16,17,18,19,20");
		System.out.println("21,22,23,24,25");
		System.out.println("26,27,28,29,30");
		System.out.println("31,48,49,50,51");
		System.out.println("41,43,54,55,56");
		System.out.println("57,58,59,60");
		String card_five = five.nextLine();
		
		Scanner six = new Scanner(System.in);
		System.out.println("Is it in ");
		System.out.println("32,33,34,35,36");
		System.out.println("37,38,39,40,41");
		System.out.println("42,43,44,45,46");
		System.out.println("47,48,49,50,51");
		System.out.println("52,53,54,55,56");
		System.out.println("57,58,59,60");
		String card_six = six.nextLine();
		int num=0;
		
		if (card_one.equals("yes")){
			num = num + 1;
		}
		if (card_two.equals("yes")){
			num = num + 2;
		}
		if (card_three.equals("yes")){
			num = num + 4;
		}
		if (card_four.equals("yes")){
			num = num + 8;
		}
		if (card_five.equals("yes")){
			num = num + 16;
		}
		if (card_six.equals("yes")){
			num = num + 32;
		}
		
		
		System.out.println("I guess it is " + num);
		
		}

	}


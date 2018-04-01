
import javac;
import java.util.Scanner;

public class Password {

	public static void main(String []args){



		Scanner pscan = new Scanner(System.in);
			System.out.println("Please enter your password");
			String pass = pscan.nextLine();

		if(pass.equals("dragoon") ){

			System.out.println("Accessed");

		}

		else{
			System.out.println("Password incorrect: Attempt 1");

			Scanner pscan2 = new Scanner(System.in);
			String password2 = pscan2.nextLine();

		if(password2.equals("dragoon") ){

			System.out.println("Accessed");

		}

		else{
			System.out.println("Password incorrect: Attempt 2");

			Scanner pscan3 = new Scanner(System.in);
			String password3 = pscan3.nextLine();

		if(password3.equals("dragoon") ){

			System.out.println("Accessed");

		}

		else{
			System.out.println("Password incorrect: Attempt 3");

			Scanner pscan4 = new Scanner(System.in);
			String password4 = pscan4.nextLine();

		if(password4.equals("dragoon") ){

			System.out.println("Accessed");

		}

		else{
			System.out.println("LOCKED");



		}

		}



		}
	}

}
}

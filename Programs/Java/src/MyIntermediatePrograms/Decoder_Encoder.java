package MyIntermediatePrograms;

import java.util.Scanner;

public class Decoder_Encoder {
	public static void main(String[] args){
		//Questions whether to decode or encode
		Scanner de = new Scanner(System.in);
		System.out.println("Decode or Encode (use all small letters)");
		String ed = de.nextLine();
		// If statement to figure out what the person chose 
		if (ed.equals("decode")) {// <-- Decode
			System.out.println("Decode");
		}
		else if (ed.equals("encode")) {// <-- Encode
			System.out.println("Encode");
		}
	}

}

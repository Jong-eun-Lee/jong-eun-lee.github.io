import java.io.IOException;
import java.util.Scanner;

public class BD_TheCalculator {
	public static void main(String[] args) throws IOException {

		int a, b;
		int result;
		char k;

		Scanner s = new Scanner(System.in);
		System.out.print("Variable 1 -> ");
		a = s.nextInt();
		System.out.print("+ or - or * or / or % -> ");
		k = (char) System.in.read();
		System.out.print("Variable 2 -> ");
		b = s.nextInt();

		if (k == '+') {
			result = a + b;
			System.out.println(result);
		}

		if (k == '-') {
			result = a - b;
			System.out.println(result);
		}

		if (k == '*') {
			result = a * b;
			System.out.println(result);
		}

		if (k == '/') {
			if (b != 0) {
				result = a / b;
				System.out.println(result);
			} else
				System.out.println("ZeroDivisionError");
		}

		if (k == '%') {
			if (b != 0) {
				result = a % b;
				System.out.println(result);
			} else
				System.out.println("ZeroModError");
		}
	}
}

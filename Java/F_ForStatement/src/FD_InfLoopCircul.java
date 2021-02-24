import java.io.IOException;
import java.util.Scanner;

public class FD_InfLoopCircul {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a, b;
		char ch;
		while (true) 
		{
			System.out.print("Input a: ");
			a = s.nextInt();
			System.out.print("Input b: ");
			b = s.nextInt();
			System.out.print("Choose operator: ");
			ch = (char) System.in.read();
			
			switch (ch)
			{
			case '+':
				System.out.printf("%d + %d = %d \n", a, b, a+b); break;
			case '-':
				System.out.printf("%d - %d = %d \n", a, b, a-b); break;
			case '*':
				System.out.printf("%d * %d = %d \n", a, b, a*b); break;
			case '/':
				System.out.printf("%d / %d = %d \n", a, b, a/b); break;
			case '%':
				System.out.printf("%d %% %d = %d \n", a, b, a%b); break;
			default:
				System.out.print("Wrong input. \n");
			}

		}
	}

}

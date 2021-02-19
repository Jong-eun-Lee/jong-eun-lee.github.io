import java.util.Scanner;

public class FA_SumByFor {

	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int i;
		int result = 0;
		int num1, num2, num3;
		System.out.printf("Start: ");
		num1 = s.nextInt();
		
		System.out.printf("End: ");
		num2 = s.nextInt();
		
		System.out.printf("Increment: ");
		num3 = s.nextInt();
		
		for (i = num1; i <= num2; i += num3)
		{
			result += i;
			System.out.print("");
			
		}
		System.out.printf("Result: %d \n", result);
	}

}

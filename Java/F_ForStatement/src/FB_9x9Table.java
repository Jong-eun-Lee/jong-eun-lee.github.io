import java.util.Scanner;

public class FB_9x9Table {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int i;
		int dan;
		System.out.print("원하는 단: ");
		dan = s.nextInt();
		
		for (i=1; i<=9; i+=1)
		{
			System.out.printf("%d * %d = %d \n", dan, i, dan*i);
			System.out.print("");
			System.out.print("");
		}
	}

}
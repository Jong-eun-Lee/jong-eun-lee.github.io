import java.util.Scanner;

public class GB_DoWhileVending {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int menu;
		do
		{
			System.out.printf("\nOrder please.\n");
			System.out.printf("[1] Tea | [2] Coffee | [3] No thanks | -> ");
			menu = s.nextInt();
			switch (menu)
			{
			case 1:
				System.out.println("Here's your tea."); break;
			case 2:
				System.out.println("Here's your coffee."); break;
			case 3:
				System.out.println("Is that it? OK."); break;
			default:
				System.out.println("Wrong order."); break;
			}
		} while (menu != 3);
	}

}
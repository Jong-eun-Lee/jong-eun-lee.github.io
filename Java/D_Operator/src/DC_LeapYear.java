import java.util.Scanner;

public class DC_LeapYear {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int year;
		
		System.out.print("Year: ");
		year = s.nextInt();
		// 4�� ������ �������鼭 100���� ������ �������� ������ ����
		// 400���� ������ �������� ����
		if ( ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0) )
			System.out.printf("%d���� ������ �´�. \n", year);
		else
			System.out.printf("%d���� ������ �ƴϴ�.", year);
	}

}

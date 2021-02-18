import java.util.Scanner;

public class DC_LeapYear {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int year;
		
		System.out.print("Year: ");
		year = s.nextInt();
		// 4로 나누어 떨어지면서 100으로 나누어 떨어지지 않으면 윤년
		// 400으로 나누어 떨어져도 윤년
		if ( ((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0) )
			System.out.printf("%d년은 윤년이 맞다. \n", year);
		else
			System.out.printf("%d년은 윤년이 아니다.", year);
	}

}

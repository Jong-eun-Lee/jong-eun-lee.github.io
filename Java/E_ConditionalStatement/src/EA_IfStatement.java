
import java.util.Scanner;

public class EA_IfStatement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a;
		System.out.printf("���� �Է�: ");
		a = s.nextInt();
		if (a > 0) {
			if (a > 100) {
				System.out.printf("100���� ū ���");
			} else {
				System.out.printf("100���� ���� ���");
			}
		} else if (a == 0) {
			System.out.printf("0");
		} else {
			System.out.printf("����");
		}
	}

}



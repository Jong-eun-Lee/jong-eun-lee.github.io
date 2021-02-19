
import java.util.Scanner;

public class EA_IfStatement {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a;
		System.out.printf("정수 입력: ");
		a = s.nextInt();
		if (a > 0) {
			if (a > 100) {
				System.out.printf("100보다 큰 양수");
			} else {
				System.out.printf("100보다 작은 양수");
			}
		} else if (a == 0) {
			System.out.printf("0");
		} else {
			System.out.printf("음수");
		}
	}

}



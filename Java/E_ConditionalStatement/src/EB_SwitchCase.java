import java.util.Scanner;

public class EB_SwitchCase {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a;
		
		System.out.printf("11, 22, 33 중 택일: ");
		a = s.nextInt();
		
		switch (a) {
		case 11:
			System.out.printf("Take 11.");
			break; // break문 안 쓰면 다음 코드로 넘어감.
		case 22: System.out.printf("Take 22."); break;
		case 33: System.out.printf("Take 33."); break;
		default:
			System.out.printf("다른 걸 선택했군요.");
		}
	}

}

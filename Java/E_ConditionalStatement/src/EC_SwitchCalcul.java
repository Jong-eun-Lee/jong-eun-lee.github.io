import java.util.Scanner;

public class EC_SwitchCalcul {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a, b;
		char ch;
		String[] str; //���ڿ� �迭 �غ�.
		System.out.printf("������ ���⸦ ����Ͽ� �� �ٷ� ������. : ");
		str = s.nextLine().split(" "); // ���ڿ��� �� �ٷ� �Է� �޾� �̰��� ���� �������� �и��� �迭�� ����.
		a = Integer.parseInt(str[0]); // ������ ��ȯ�Ͽ� a�� ����.
		ch = str[1].charAt(0);
		b = Integer.parseInt(str[2]);
		
		switch (ch) {
		case '+':
			System.out.printf("%d + %d = %d \n", a, b, a+b);
			break;
		case '-':
			System.out.printf("%d - %d = %d \n", a, b, a-b);
			break;
		case '*':
			System.out.printf("%d * %d = %d \n", a, b, a*b);
			break;
		case '/':
			System.out.printf("%d / %d = %d \n", a, b, a/b);
			break;
		case '%':
			System.out.printf("%d %% %d = %d \n", a, b, a%b);
			break; 
		default:
			System.out.printf("Wrong Input \n");
		}
	}

}

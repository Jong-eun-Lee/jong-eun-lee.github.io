import java.util.Scanner;

public class EC_SwitchCalcul {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int a, b;
		char ch;
		String[] str; //문자열 배열 준비.
		System.out.printf("수식을 띄어쓰기를 사용하여 한 줄로 쓰세요. : ");
		str = s.nextLine().split(" "); // 문자열을 한 줄로 입력 받아 이것을 공백 기준으로 분리해 배열에 저장.
		a = Integer.parseInt(str[0]); // 정수로 변환하여 a에 저장.
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

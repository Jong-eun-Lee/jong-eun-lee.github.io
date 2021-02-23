import java.util.Scanner;

public class FC_ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		String str;
		int count;
		int i;
		
		System.out.printf("문자열을 입력하시오. ");
		str = s.nextLine();
		
		System.out.println("");
		System.out.printf("입력된 문자열: %s \n", str);
		System.out.printf("거꾸로 출력된 문자열: ");
		
		count = str.length();
		for (i=count-1; i>=0; i--)
		{
			System.out.printf("%c", str.charAt(i));
		}
	}

}

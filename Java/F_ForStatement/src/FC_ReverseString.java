import java.util.Scanner;

public class FC_ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		String str;
		int count;
		int i;
		
		System.out.printf("���ڿ��� �Է��Ͻÿ�. ");
		str = s.nextLine();
		
		System.out.println("");
		System.out.printf("�Էµ� ���ڿ�: %s \n", str);
		System.out.printf("�Ųٷ� ��µ� ���ڿ�: ");
		
		count = str.length();
		for (i=count-1; i>=0; i--)
		{
			System.out.printf("%c", str.charAt(i));
		}
	}

}

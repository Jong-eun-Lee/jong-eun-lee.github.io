import java.util.Scanner;

public class DB_CoinChange {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int money, div500, div100, div50, div10;
		
		System.out.println("�������� ��ȯ�� ���� ���Դϱ�?");
		money = s.nextInt();
		
		div500 = money / 500; // div500�� �� 500��¥�� ���� ����
		money %= 500; // 500�� ¥������ �Ž��� �� ���� money�� ����
		
		div100 = money / 100;
		money %= 100;
		
		div50 = money / 50;
		money %= 50;
		
		div10 = money / 10;
		money %= 10;
		
		System.out.printf("500�� ���� �� %d�� \n", div500);
		System.out.printf("100�� ���� �� %d�� \n", div100);
		System.out.printf("50�� ���� �� %d�� \n", div50);
		System.out.printf("10�� ���� �� %d�� \n", div10);
		System.out.printf("�������� �� �Ž����� �ܵ� %d��", money);
	}

}

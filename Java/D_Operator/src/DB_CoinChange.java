import java.util.Scanner;

public class DB_CoinChange {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int money, div500, div100, div50, div10;
		
		System.out.println("동전으로 교환할 돈은 얼마입니까?");
		money = s.nextInt();
		
		div500 = money / 500; // div500은 총 500원짜리 동전 개수
		money %= 500; // 500원 짜리들을 거슬러 준 후의 money를 갱신
		
		div100 = money / 100;
		money %= 100;
		
		div50 = money / 50;
		money %= 50;
		
		div10 = money / 10;
		money %= 10;
		
		System.out.printf("500원 동전 총 %d개 \n", div500);
		System.out.printf("100원 동전 총 %d개 \n", div100);
		System.out.printf("50원 동전 총 %d개 \n", div50);
		System.out.printf("10원 동전 총 %d개 \n", div10);
		System.out.printf("동전으로 안 거슬러진 잔돈 %d원", money);
	}

}

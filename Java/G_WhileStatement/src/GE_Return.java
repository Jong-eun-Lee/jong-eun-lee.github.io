
public class GE_Return {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int result = 0;
		int i;
		for (i=1; i<=10; i+=1) {
			result += i;
		}
		System.out.printf("%d", result);
		if (result > 50)
			return; // return 뒤에 오는 값은 현재 메소드의 데이터 타입과 일치해야 함.
		System.out.printf("Hi"); // result 값이 50보다 크다면 출력되지 않을 것(실제로 출력 안 됨).

	}

}

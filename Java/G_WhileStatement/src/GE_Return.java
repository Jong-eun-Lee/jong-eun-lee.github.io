
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
			return; // return �ڿ� ���� ���� ���� �޼ҵ��� ������ Ÿ�԰� ��ġ�ؾ� ��.
		System.out.printf("Hi"); // result ���� 50���� ũ�ٸ� ��µ��� ���� ��(������ ��� �� ��).

	}

}

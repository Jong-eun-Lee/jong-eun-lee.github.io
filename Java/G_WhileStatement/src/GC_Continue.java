
public class GC_Continue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int result = 0;
		int i;
		
		for (i=1; i<=10; i+=1)
		{
			if (i%2==0)
				continue;
			result += i;
		}
		System.out.printf("1���� 10������ ��(¦�� ����): %d", result);
	}

}
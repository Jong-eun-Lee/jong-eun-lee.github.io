
public class GD_BreakLable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int result=0;
		int i;
		
		abcLabel: for (;;) // for (;;)�� while (true)�� ���� ���ѷ�����.
		{
			for (i=1; i<=10; i+=1)
			{
				result += i;
				if (result > 15)
				{
					System.out.printf("i���� %d, result ���� %d \n", i, result);
					result = 0;
					break abcLabel; // break �� ������ ���̺��� ��������.
				}
			}
			System.out.print("�� ������ ���δٸ� ������ �ݺ� ��."); // break lable�� ���� �� ���� ��.
		}
	}

}
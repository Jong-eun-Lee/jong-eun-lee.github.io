
public class DA_Operators {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// ��� ������: +, -, *, /, %
		// ���� ������: +=, -=, *=, /=, %=
		// ���� ������: ++ --
		// a++(��ġ ���� ������) �Ǵ� ++a �� �Ȱ��� a �� 1�� ������Ű����, ��뿡 �־ �������� �߻��� �� �ִ�.
		int a = 10, b;
		b = a++; // b=a�� ���� ���� a �� 1 ������Ŵ.
		System.out.println(b); //10
		System.out.println(a); // 11
		b = ++a; // a �� 1 ������Ų ���� b=a ����.
		System.out.println(b); // 12
		System.out.println(a); // 12
		// ���� ������: ==, !=, >, <, >=, <=
		// �� ������: &&(AND), ||(OR), !(NOT)
		System.out.println(1>2 && 3>1);
		// ��Ʈ ������: &, |, ^(XOR), ~, <<, >>(��Ʈ�� ���������� ����Ʈ)
		// ��Ʈ �����ڴ� ������ ���� ���� 2������ ��ȯ�� �� �� �ڸ��� ��Ʈ���� ���� ����
		System.out.println(10 & 6); // 1010(2)�� 0110(2)�� ��Ʈ �������ָ� 0010(2), �� 2�� ����.
		System.out.println(~5); // ��Ʈ ���� ������. 1�� ���� ��ȯ.
		System.out.println(Integer.toBinaryString(~5));
		System.out.println(11 >> 1); // 1011(2) �� ���������� �� ĭ ����Ʈ�Ͽ� 0101(2), �� �� 5�� ����.

	}

}

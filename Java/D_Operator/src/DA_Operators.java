
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
		int c = -10;
		c ++;
		System.out.print(c);
		-- c;
		System.out.print(c);
	}

}

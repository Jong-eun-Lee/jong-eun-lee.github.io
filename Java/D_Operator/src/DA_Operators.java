
public class DA_Operators {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 산술 연산자: +, -, *, /, %
		// 대입 연산자: +=, -=, *=, /=, %=
		// 증감 연산자: ++ --
		// a++(후치 증가 연산자) 또는 ++a 는 똑같이 a 값 1을 증가시키지만, 사용에 있어서 차이점이 발생할 수 있다.
		int a = 10, b;
		b = a++; // b=a를 해준 다음 a 값 1 증가시킴.
		System.out.println(b); //10
		System.out.println(a); // 11
		b = ++a; // a 값 1 증가시킨 것을 b=a 해줌.
		System.out.println(b); // 12
		System.out.println(a); // 12
		int c = -10;
		c ++;
		System.out.print(c);
		-- c;
		System.out.print(c);
	}

}

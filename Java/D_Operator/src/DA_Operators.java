
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
		// 관계 연산자: ==, !=, >, <, >=, <=
		// 논리 연산자: &&(AND), ||(OR), !(NOT)
		System.out.println(1>2 && 3>1);
		// 비트 연산자: &, |, ^(XOR), ~, <<, >>(비트를 오른쪽으로 시프트)
		// 비트 연산자는 정수나 문자 등을 2진수로 변환한 후 각 자리의 비트끼리 연산 수행
		System.out.println(10 & 6); // 1010(2)와 0110(2)를 비트 논리곱해주면 0010(2), 즉 2가 나옴.
		System.out.println(~5); // 비트 부정 연산자. 1의 보수 반환.
		System.out.println(Integer.toBinaryString(~5));
		System.out.println(11 >> 1); // 1011(2) 를 오른쪽으로 한 칸 시프트하여 0101(2), 즉 값 5가 나옴.

	}

}

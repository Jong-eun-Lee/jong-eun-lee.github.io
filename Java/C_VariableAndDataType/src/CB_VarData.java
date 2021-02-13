
public class CB_VarData {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Variable and Data type
		int a; // 정수형 변수 선언. 4byte.
		float b; // 실수형. 4byte.
		double c; // 실수형. 8byte.
		int d, e; double f;
		int x = 100;
		float y;
		y = 200.54f; // float에 값 대입 시 f를 붙여야.
		double z = (int) 11.345; // int로 변환됨.
		System.out.println(z);
		System.out.println(10.0/3);
		// Java의 기본 정수형은 int(4바이트).
		// 기본 실수형은 double(8바이트). (float는 4바이트)
		char g = 'a';
		char h = (char) (g + 1); // h를 출력하면 b가 나올 것이다.
		char i = (char) 75;
		System.out.println(g);
		System.out.println(h);
		System.out.println(i);
	}

}
 
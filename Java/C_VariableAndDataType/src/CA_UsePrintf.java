
public class CA_UsePrintf {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.printf("%d / %d = %1.3f \n", 10, 20, 0.5);
		System.out.printf("%-5d %05d %5d \n", 123, 123, 123);
		System.out.printf("%x %o", 511, 9); // hexadecimal & octal
		System.out.printf("%c %s %s \n", 'a', "abc", "z"); // char and string
		System.out.printf("\t123\b321\\\'\"\r000");
		
		// 변수
		int a; // 정수형 변수 선언. 4byte.
		float b; // 실수형. 4byte.
		double c; // 실수형. 8byte.
		int d, e; double f;
		int x = 100;
		float y;
		y = 200.54f; // float에 값 대입 시 f를 붙여야.
		float z = (int) 11.345f; // int로 변환됨.
		System.out.println(z);
		System.out.println("3") = 4;
	}

}
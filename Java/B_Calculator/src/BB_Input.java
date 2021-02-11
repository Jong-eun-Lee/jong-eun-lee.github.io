import java.util.Scanner;
public class BB_Input{

public static void main(String[] args) {
	// TODO Auto-generated method stub
	int a, b;
	int result;

	Scanner s = new Scanner(System.in);
	a = s.nextInt();
	b = s.nextInt();

	result = a + b;
	System.out.println(a + "+" + b + "=" + result);

	result = a - b;
	System.out.println(a + "-" + b + "=" + result);

	result = a * b;
	System.out.println(a + "*" + b + "=" + result);

	result = a / b;
	System.out.println(a + "/" + b + "=" + result);
	}

}

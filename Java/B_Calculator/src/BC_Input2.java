import java.util.Scanner;
public class BC_Input2{

public static void main(String[] args) {
	// TODO Auto-generated method stub
	int a, b;
	int result;

	Scanner s = new Scanner(System.in);
	System.out.print("Variable 1 => ");
	a = s.nextInt();
	System.out.print("Variable 2 => ");
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

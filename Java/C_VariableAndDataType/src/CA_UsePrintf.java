
public class CA_UsePrintf {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.printf("%d / %d = %1.3f \n", 10, 20, 0.5);
		System.out.printf("%-5d %05d %5d \n", 123, 123, 123);
		System.out.printf("%x %o", 511, 9); // hexadecimal & octal
		System.out.printf("%c %s %s \n", 'a', "abc", "z"); // char and string
		System.out.printf("\t123\b321\\\'\"\r000");
	}

}
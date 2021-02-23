public class FB_9x9Table {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i, j;
		
		for (i=1; i<=9; i++)
		{
			for (j=2; j<=9; j++)
			{
			System.out.printf("%d * %d = %2d | ", j, i, j*i);
			}
			System.out.println("");
		}
	}

}
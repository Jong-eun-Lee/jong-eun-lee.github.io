
public class GD_BreakLable {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int result=0;
		int i;
		
		abcLabel: for (;;) // for (;;)는 while (true)와 같이 무한루프를.
		{
			for (i=1; i<=10; i+=1)
			{
				result += i;
				if (result > 15)
				{
					System.out.printf("i값은 %d, result 값은 %d \n", i, result);
					result = 0;
					break abcLabel; // break 시 지정한 레이블을 빠져나감.
				}
			}
			System.out.print("이 문구가 보인다면 여전히 반복 중."); // break lable을 통해 안 보일 것.
		}
	}

}
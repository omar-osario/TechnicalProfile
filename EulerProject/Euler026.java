import java.util.*;

class Euler026
{
	public static void main(String[] args)
	{
		long startTime = System.currentTimeMillis() ;
		
		//double x = 0.0 ;
		
		for ( int x = 7 ; x < 100 ; x+=2 )
		{
			double dummy = x ;
			System.out.println("X :" + dummy +" \t Fraction:" +  1.0/dummy);
		}
	



		double execTime = (System.currentTimeMillis() - startTime) ;
		System.out.print("Total execution time is :");
		System.out.print(execTime/1000);
		System.out.println(" sec/s");
	//	Scanner in = new Scanner(System.in);
	//	in.nextLine();
		
	}
}



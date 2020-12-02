
public class ComputeGrade {
	
	private static int pointsPerProblem = 20;
	
	public static int gradeP1()
	{
		int grade = 0;
		
		int[] a = {3, 2, 3};
		int[] b = {2,2,1,1,1,2,2};
	    int[] c = {2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

		int test1 = P1MajorityElement.majorityElement(a);
		int test2 = P1MajorityElement.majorityElement(b);
		int test3 = P1MajorityElement.majorityElement(c);
		
	    if (test1 == 3 && test2 == 2 && test3 == 1)
	        grade += pointsPerProblem;
		
		
		return grade;
	}
	
	
	public static int gradeP2()
	{
		int grade = 0;
		
		int[] a = {2,2,1};
		int[] b = {4,1,2,1,2};
		int[] c = {8, 9, 9, 8, 1, 0, 1, 3, 2, 3, 2};
		int test1 = P2SingleNumber.singleNumber(a);
		int test2 = P2SingleNumber.singleNumber(b);
		int test3 = P2SingleNumber.singleNumber(c);
		
	    if (test1 == 1 && test2 == 4 && test3 == 0)
	        grade += pointsPerProblem;
		
		
		return grade;
	}
	
	
	public static int gradeP3()
	{
		int grade = 0;
		
		int test1 = P3ClimbStairs.climbStairs(2);
		int test2 = P3ClimbStairs.climbStairs(3);
		int test3 = P3ClimbStairs.climbStairs(13);
		
	    if (test1 == 2 && test2 == 3 && test3 == 377)
	        grade += pointsPerProblem;
		
		
		return grade;
	}
	
	
	public static int gradeP4()
	{
		int grade = 0;
		
		int[] a = {1,2,3,1};
		int[] b = {2,7,9,3,1};		
		int[] c = {1,200,3,3,400,1};
		int test1 = P4HouseRobber.rob(a);
		int test2 = P4HouseRobber.rob(b);
		int test3 = P4HouseRobber.rob(c);
		
	    if (test1 == 4 && test2 == 12 && test3 == 600)
	        grade += pointsPerProblem;
		
		
		return grade;
	}
	
	public static int gradeP5()
	{
		int grade = 0;
		
		int[] a = {7,1,5,3,6,4};
		int[] b = {7,6,4,3,1};		
		int[] c = {7, 1, 5, 3, 6, 4, 3, 10, 10, 8};
		
		int test1 = P5BestTimeToBuySell.maxProfit(a);
		int test2 = P5BestTimeToBuySell.maxProfit(b);
		int test3 = P5BestTimeToBuySell.maxProfit(c);
		
	    if (test1 == 5 && test2 == 0 && test3 == 9)
	        grade += pointsPerProblem;
		
		
		return grade;
	}
	
	public static void main(String... args)
	{
		
		int grade = 0;
		
		grade += gradeP1();
		grade += gradeP2();
		grade += gradeP3();
		grade += gradeP4();
		grade += gradeP5();
		
		System.out.println("Your grade is: " + grade);
	}
}

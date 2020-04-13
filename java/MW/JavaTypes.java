public class JavaTypes {
	public static void main(String[] args) {
		// Create a variable with an int value
		int a = 5;
		a = 7;
		
		/*
		System.out.print("a is ");
		System.out.println(a);
		*/

		System.out.println("a is " + a);

		// This would generate an error:
		//a = 4.0;

		// Possible, but bad practice
		// Should initialize all variables
		/*int b;
		b = 10;
		*/

		double d = 5.0;
		System.out.println("d is " + d);

		float f = 6.0f;
		System.out.println("f is " + f);

		/* range of int is:
		-2,147,483,648
		to
		2,147,483,647
		*/
		//int g = 4000000000;
		long h = 4000000000l;

		char i = 'i';
		System.out.println("i is " + i);

		String j = "This is a string";
		System.out.println("j is " + j);

		System.out.printf("i is %c\nj is %s\n", i, j);
		System.out.printf("%.2f\n", d);
	}
}

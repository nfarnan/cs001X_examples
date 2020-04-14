public class JavaTypes {
	public static void main(String[] args) {
		// This is a Java comment

		/* This is also a Java comment
		Keeps going
		Until 
		*/

		// Bad practice, always provide an inital value
		//int a;
		//a = 5;

		int a = 5;
		a = 7;

		System.out.println("a is " + a);

		// This will generate an error
		//a = 4.0;

		double b = 4.0;

		System.out.print("b is ");
		System.out.println(b);

		// This will error
		//float c = 5.4
		// This is fine
		float c = 5.4f;
		System.out.print("c is ");
		System.out.println(c);

		// This will error
		/* Valid range for int -2,147,483,648
		   to
		   2,147,483,647
		*/
		//int d = 4000000000;
		long d = 4000000000l;
		System.out.println("d is " + d);

		char e = 'e';
		String f = "this is a string";
		
		System.out.printf("e: %c\nf is %s\n", e, f);

		System.out.printf("%.5f\n", b);
	}
}

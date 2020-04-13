public class Functions {
	public static void main(String[] args) {
		sayHello();
		System.out.println(returnHello());
		System.out.println(adder(5, 7));
		rec(5);
	}

	public static void sayHello() {
		System.out.println("Hello!");
	}

	public static String returnHello() {
		return "Hello!";
	}

	public static int adder(int a, int b) {
		return a + b;
	}

	public static void rec(int i) {
		if (i == 0) {
			System.out.println(0);
		}
		else if (i > 0) {
			rec(i - 1);
			System.out.println(i);			
		}
	}
}

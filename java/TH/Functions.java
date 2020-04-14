public class Functions {
	public static void main(String[] args) {
		sayHello();
		System.out.println(returnHello());
		System.out.println(adder(5, 17));
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
}

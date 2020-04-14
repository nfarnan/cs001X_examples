public class Structures {
	public static void main(String[] args) {
		String a_string = "This is a String";

		int cur = 0;
		int total = 0;
		while (cur < a_string.length()) {
			if (a_string.charAt(cur) == 's') {
				total += 1;
			}
			else if (a_string.charAt(cur) == 'S') {
				total++;
			}
			else {
				// Nothing to do
			}

			cur++;
		}

		System.out.printf("%d s's found\n", total);

		// Basic for loop different in Java...
		for (int i = 0; i < 10; i++) {
			System.out.println(i);
		}

		for (int i = 5; i <= 20; i += 5) {
			System.out.println(i);
		}
	}
}

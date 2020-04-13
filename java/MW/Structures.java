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
				// Nothing to do...
			}

			cur++;
		}

		System.out.printf("%d s's!\n", total);

		// For loop syntax is different...
		for (int i = 5; i <= 10; i += 2) {
			System.out.println(i);
		}
	}
}

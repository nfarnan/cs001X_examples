public class Arrays {
	public static void main(String[] args) {
		int[] an_array = new int[10];
		for (int i = 0; i < an_array.length; i++) {
			an_array[i] = i;
		}

		for (int j : an_array) {
			System.out.println(j);
		}
	}
}

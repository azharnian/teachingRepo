public class Main {

	public static void main(String[] args) {
		System.out.println("Hello, world!");
		if (args.length > 0){
			// for (int index = 0; index < args.length; index++){

			// 	System.out.println( index + " " + args[index] );

			// }

			for (String arg : args) {
				System.out.println(arg);
			}
		}
	}

}
package com.program;

public class Main {

    public static void main(String[] args){

        System.out.println("I'm Anas Azhar");
        System.out.printf("I'm %d years old and %.2f.\n", 27, 170.5f);

        if (args.length > 0){
            System.out.println("Args value : ");
//            for (int index = args.length - 1; index >= 0; --index){
//                System.out.print(args[index] + " ");
//            }
//            for (int index = 0; index < args.length; ++index){
//                System.out.print(args[index] + " ");
//            }
            for (String arg : args){
                System.out.print(arg + " ");
            }
            System.out.println();
        }

        int number; // deklarasi
        number = 40 ; // assignment
        int numberAgain = 100;
        System.out.println(number+" "+numberAgain);
        // INTEGER, SHORT, LONG, BYTE
        // FLOAT, DOUBLE
        // BOOL, CHAR

        System.out.println(Integer.BYTES); // 4 BYTES -> 4*8 BIT SIGN NUMBER +- 2^31 -1
        System.out.println(Integer.MAX_VALUE+1);
        System.out.println(Short.BYTES);
        System.out.println(Short.MAX_VALUE);
        System.out.println(Long.BYTES);
        System.out.println(Long.MAX_VALUE);
        System.out.println(Byte.BYTES);
        System.out.println(Byte.MAX_VALUE);


    }

}

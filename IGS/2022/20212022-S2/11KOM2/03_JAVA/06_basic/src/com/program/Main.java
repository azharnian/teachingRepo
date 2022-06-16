package com.program;

public class Main {

    public static void main(String[] args){

        System.out.println("I'm Anas Azhar");
        System.out.printf("I'm %d years old, and %.2f.\n", 27, 170.5f);

        if (args.length > 0){
            System.out.println("Args value are :");

            for (int index = args.length-1; index >= 0; --index){
                System.out.print(args[index]+ " ");
            }

        } else {
            System.out.println("No Arguments Here!");
        }

        int number; //deklarasi
        number = 40; //assignment
        int numberAgain = 100;
        System.out.println(numberAgain + " " + number);
        // INTEGER, SHORT, LONG, BYTE
        // FLOAT, DOUBLE
        // CHAR, BOOL

        System.out.println(Integer.BYTES); // 4 BYTES = 32 BIT : +- 2 ^ 31 - 1
        System.out.println(Integer.MAX_VALUE+1);

    }

}

package com.program;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	    float a, b, result;
        char operator; // String operator, 'a', "a"

        Scanner userInput = new Scanner(System.in);

        System.out.print("Value A : ");
        a = userInput.nextFloat();
        System.out.print("Operator : ");
        operator = userInput.next().charAt(0);
        System.out.print("Value B : ");
        b = userInput.nextFloat();


        switch (operator){
            case '+':
                result = a+b;
                break;
            case '-':
                result = a-b;
                break;
            case '*':
                result = a*b;
                break;
            case '/':
                result = a/b;
                break;
            default:
                result = 0;
                System.out.println("Sorry, undefined operator!");
        }

        if (result > 0) System.out.printf("Result = %.2f\n", result);


    }
}

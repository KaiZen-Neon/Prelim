import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter value of x: ");
        double x = input.nextDouble();

        System.out.print("Enter value of y: ");
        double y = input.nextDouble();

        double result = 0.0;

        System.out.println("\nVariable values:");
        System.out.println("x = " + x);
        System.out.println("y = " + y);
        System.out.println("result = " + result);

        System.out.println("\nArithmetic Operation:");

        result = x + y;
        System.out.println("Addition: x + y = " + result);

        result = x - y;
        System.out.println("Subtraction: x - y = " + result);

        result = x * y;
        System.out.println("Multiplication: x * y = " + result);

        result = x / y;
        System.out.println("Division: x / y = " + result);

        result = x % y;
        System.out.println("Modulus: x % y = " + result);

        result = ++x;
        System.out.println("Increment: x++ = " + result);

        result = x - 2;
        System.out.println("Decrement: x-- = " + result);

        input.close();
    }
}



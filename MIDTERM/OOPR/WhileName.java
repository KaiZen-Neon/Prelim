import java.util.Scanner;

public class WhileName {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = input.nextLine();

        int i = 1;

        while (i <= 5) {
            System.out.println(name);
            i++;
        }
    }
}
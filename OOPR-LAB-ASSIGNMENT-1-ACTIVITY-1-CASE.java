import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String choice;

        do {
            System.out.print("Enter your Java Score: ");
            double javaScore = input.nextDouble();

            System.out.print("Enter your C Score: ");
            double cScore = input.nextDouble();

            System.out.print("Enter your Database Handling score: ");
            double databaseScore = input.nextDouble();

            double average = (javaScore + cScore + databaseScore) / 3;
            String grade;

            if (average >= 90 && average <= 100) {
                grade = "A";
            } else if (average >= 80) {
                grade = "B";
            } else if (average >= 75) {
                grade = "C";
            } else {
                grade = "F";
            }

            System.out.println("Output:");
            System.out.println(grade);

            System.out.printf("Explanation:%nThe average of the student is %.3f, so the student's grade is %s.%n",
                    average, grade);

            input.nextLine();
            System.out.print("Do you want to continue : YES / NO: ");
            choice = input.nextLine();

        } while (choice.equalsIgnoreCase("YES"));

        System.out.println("Program terminated.");

        input.close();
    }
}

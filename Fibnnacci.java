public class Fibnnacci {
    static int fib(int n) {
        if (n <= 1)
            return n;   // Base case
        return fib(n - 1) + fib(n - 2); // Recursive case
    }

    static void fibr(int n) {
        int a = 0, b = 1, c;

        System.out.print("Fibonacci series up to " + n + " terms:\n");
        if (n > 0) System.out.print(a + " ");
        if (n > 1) System.out.print(b + " ");

        for (int i = 2; i < n; i++) {
            c = a + b;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
    }

    public static void main(String[] args) {
        int n = 10; // Example
        System.out.println("Fibonacci series up to " + n + " terms:");
        for (int i = 0; i < n; i++) {
            System.out.print(fib(i) + " ");
        }
    }
}

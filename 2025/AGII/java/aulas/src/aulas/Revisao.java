package aulas;

public class Revisao {
    public static void main(String[] args) {
    Revisao teste = new Revisao();
    int[] a = {1, 2, 3};
    int[] b = {1, 2 ,3};
    int n = 3;
    int result = teste.recursao(a, b, n);
    System.out.println(result);

    }
    public int recursao(int[] a, int[] b, int n) {
        if(n == 0) {return 0;}

        return a[n - 1] * b[n -1] + recursao(a, b, n - 1);
    }
}

package aulas.recursao;

public class Fibonacci {
    public int sequenciaFibonacci(int num) {
        if(num <= 1) {return num;}

        return sequenciaFibonacci(num - 1) + sequenciaFibonacci(num - 2);
    }

    public void imprimirFibonacci(int num) {
        for(int i = 0; i < num; i++) {
            System.out.print(sequenciaFibonacci(i) + " ");
        }
        int result = sequenciaFibonacci(num);
        System.out.println("= " + result);
    }
}

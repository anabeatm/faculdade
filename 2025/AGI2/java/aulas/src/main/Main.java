package main;
import java.util.Scanner;

public class Main {
    // Converta uma temperatura de Celsius para Fahrenheit.
    public static double conversaoTemperatura(double celsius) {
        double temperatura = (celsius * 9 / 5) + 32;
        return temperatura;
    }

    // Escreva um programa/método que receba três números e calcule a média aritmética deles.
    public static double mediaAritmetica(double valor1, double valor2, double valor3) {
        double media = (valor1 + valor2 + valor3) / 3;
        return media;
    }

    // Calcule o número fatorial de um número.
    public static int fatorial(int valor) {
        int fatorial = valor;
        while (valor > 1) {
            fatorial = fatorial * (valor - 1);
            valor--;
        }
        return fatorial;
    }

    // Inverta a ordem dos dígitos de um número
    public static int invertendoOrdem (int[] numeros) {
        int invertido = 0;
        for (int i = numeros.length - 1; i >= 0; i--) {
            invertido = invertido * 10 + numeros[i];
        }
        return invertido;
    }

    public static void main(String[] args) {
        // System.out.println(conversaoTemperatura(25));
        // System.out.println(mediaAritmetica(4, 6, 8));
        // System.out.println(fatorial(5));
        Scanner scanner = new Scanner(System.in);

        System.out.print("Quantos números você deseja inserir? ");
        int tamanho = scanner.nextInt();

        int[] numeros = new int[tamanho];
        for (int i = 0; i < tamanho; i++) {
            System.out.print("Insira o número " + (i + 1) + ": ");
            numeros[i] = scanner.nextInt();
        }

        scanner.close();

        System.out.println(invertendoOrdem(numeros));
    }


}

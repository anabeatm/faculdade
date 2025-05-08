package exercicios;

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

    // Verifique se uma palavra é um palíndromo.
    public static boolean palindromo(String palavra) {
        int esquerda = 0;
        int direita = palavra.length() - 1;

        while(esquerda < direita) {
            if(palavra.charAt(esquerda) != palavra.charAt(direita)) {
                return false;
            }
            esquerda++;
            direita--;
        }
        return true;

    }

    // Calcule a soma dos dígitos de um número.
    public static int soma(String digitos) {
        int soma = 0;
        for(int i = 0; i < digitos.length(); i++) {
            soma += Character.getNumericValue(digitos.charAt(i));
        }
        return soma;
    }

    // Ordene três números em ordem crescente.
    public static int[] ordemCrescente(int[] vetorNumerico) {
        for(int i = 0; i < vetorNumerico.length - 1; i++) {
            int iMenor = i;
            for(int j = i + 1; j < vetorNumerico.length; j++) {
                if(vetorNumerico[j] < vetorNumerico[iMenor]) {
                    iMenor = j;
                }
            }
            int auxiliar = vetorNumerico[i];
            vetorNumerico[i] = vetorNumerico[iMenor];
            vetorNumerico[iMenor] = auxiliar;
        }
        return vetorNumerico;
        
    }

    // Conte o número de vogais em uma string sem utilizar a função length.
    public static void contantoVogais(String frase) {
        int tamanhoFrase = 0;

        for(char vogal : frase.toCharArray()) {
            tamanhoFrase += 1;
        }

        // Converte a string para minúsculas e transforma em um array de caracteres
        char[] vogais = frase.toLowerCase().toCharArray();
        int count = 0;  // Inicializa o contador de vogais
        for(int i = 0; i < tamanhoFrase; i++) { // Percorre cada caractere do array
            char v = vogais[i]; // Obtém o caractere atual
            if(v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u') {
                // Verifica se o caractere é uma vogal (a, e, i, o, u)
                count++;
            }
        }
       System.out.println("Há " + count + " vogais.");
    }

//    Converta um número decimal para binário.
    public static String convertendoBinario(int decimal) {
        if(decimal == 0) {
            return "0";
        }

        StringBuilder binario = new StringBuilder();

        while(decimal > 0) {
            int resto = decimal % 2;
            binario.insert(0, resto);
            decimal /= 2;
        }
        return binario.toString();
    }

//          SAÍDA
public static void main(String[] args) {
    double[] vetor = {3.3, 76.4, 12.2, 9.8, 23.5, 54.1};

    for (int i = 0; i < vetor.length; i++) {
        System.out.print(vetor[i] + " \n");
    }
    ordenandoVetor(vetor);
    System.out.println("----------ORDENADO------------");
    for (int i = 0; i < vetor.length; i++) {
        System.out.print(vetor[i] + " \n");
    }
}

    public static void ordenandoVetor(double[] vetor) {
        for (int i = 0; i < vetor.length; i++) {
            double chave = vetor[i];
            int j = i - 1;

            while (j >= 0 && vetor[j] > chave) {
                vetor[j + 1] = vetor[j];
                j -= 1;
            }
            vetor[j + 1] = chave;
        }
    }
}


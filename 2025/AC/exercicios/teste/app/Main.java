package teste.app;

import teste.model.Teste;

public class Main {
    public static void main(String[] args) {
       int[] vetor = {13, 65, 34, 98};
       String msgMaior = "O maior número é: ";

        Teste iniciando = new Teste();
        int maiorNumero = iniciando.descobrindoMaiorNum(vetor);
        System.out.println(msgMaior + maiorNumero);

        System.out.println(iniciando.selectionSort(vetor));
    }
}

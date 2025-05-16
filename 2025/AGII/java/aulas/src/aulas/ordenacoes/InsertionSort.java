package aulas.ordenacoes;
// LÓGICA:
// Semelhante ao processo de organizar cartas na mão. Imagine que você tem um baralho de cartas desordenadas
// e deseja organizá-las. Você começa com uma carta na mão (a primeira da lista) e, à medida que pega as próximas
// cartas, as coloca na posição correta em relação às cartas já ordenadas.
public class InsertionSort {
    private int[] vetor;

    public void setVetor(int[] vetor) {
        this.vetor = vetor;
    }

    public int[] getVetor() {
        return vetor;
    }

    public InsertionSort(){}

    public InsertionSort(int[] vetor) {
        this.setVetor(vetor);
    }

    private void ordenandoVetor() {
        // enquanto i for menor que o tamanho do vetor
        for (int i = 0; i < vetor.length; i++) {
            int carta = vetor[i]; // cria uma variável que recebe o valor do vetor em i
            int j = i - 1; // e cria uma variável que recebe o valor de i - 1

            while(j >= 0 && vetor[j] > carta) { // enquanto j for maior ou igual a 0 e...
                // vetor em j for maior que a variável de vetor em i
                vetor[j + 1] = vetor[j]; // o próximo valor (j + 1) recebe o valor de vetor em j
                j -= 1; // aí diminui o j em 1
            }
            vetor[j + 1] = carta; // fora do while, o vetor em j + 1 recebe o valor da variável de vetor em i
        }
    }

    public void printandoVetor() {
        ordenandoVetor();

        for (int i = 0; i < vetor.length ; i++) {
            System.out.println(vetor[i]);
        }
    }
}

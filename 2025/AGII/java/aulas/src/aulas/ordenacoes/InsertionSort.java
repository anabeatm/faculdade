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
        for (int i = 0; i < vetor.length; i++) {
            int carta = vetor[i];
            int j = i - 1;

            while(j >= 0 && vetor[j] > carta) {
                vetor[j + 1] = vetor[j];
                j -= 1;
            }
            vetor[j + 1] = carta;
        }
    }

    public void printandoVetor() {
        ordenandoVetor();

        for (int i = 0; i < vetor.length ; i++) {
            System.out.println(vetor[i]);
        }
    }
}

package aulas.ordenacoes;
// LÓGICA:
// Percorre repetidamente a lista, comparando elementos adjacentes e trocando-os se estiverem na ordem errada.
// Esse processo é repetido até que a lista esteja ordenada.
public class BubbleSort {
    private int[] vetor;

    public void setVetor(int[] vetor) {
        this.vetor = vetor;
    }

    public int[] getVetor() {
        return vetor;
    }

    public BubbleSort(){}

    public BubbleSort(int[] vetor) {
        this.setVetor(vetor);
    }

    private void ordernandoVetor() {
//        Ciclo
        for (int i = 0; i < vetor.length - 1; i++) {
//            Ordenação
            for (int j = 0; j < vetor.length - 1 ; j++) {
                // Se vetor na posição j for maior que o próximo (j + 1)
                if(vetor[j] > vetor[j + 1]) {
                    // Swap
                    int aux = vetor[j];
                    vetor[j] = vetor[j + 1];
                    vetor[j + 1] = aux;
                }
            }
        }
    }

    public void printandoVetor() {
        ordernandoVetor();
        for (int i = 0; i < vetor.length; i++) {
            System.out.printf(vetor[i] + "\n");
        }
    }
}


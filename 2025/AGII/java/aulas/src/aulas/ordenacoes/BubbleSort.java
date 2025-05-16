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
//      enquanto i for menor que o tamanho do vetor - 1
        for (int i = 0; i < vetor.length - 1; i++) {
//            e enquanto j também for menor que o tamanho do vetor - 1
            for (int j = 0; j < vetor.length - 1 ; j++) {
                // e se o vetor na posição j for maior que o próximo valor (j + 1)
                if(vetor[j] > vetor[j + 1]) {
                    // cria uma variável auxiliar onde...
                    int aux = vetor[j]; // ...aux recebe o valor do vetor na posição j
                    vetor[j] = vetor[j + 1]; // vetor em j recebe o valor de j + 1
                    vetor[j + 1] = aux; // e por último, vetor em j + 1 recebe a variável auxiliar
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


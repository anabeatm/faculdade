package aulas.ordenacoes;
// LÓGICA:
// Dividir o array em duas partes: a parte ordenada (à esquerda) e a parte não ordenada (à direita).
// A cada iteração, o menor elemento da parte não ordenada é selecionado e
// trocado com o primeiro elemento da parte não ordenada, movendo-o para a parte ordenada.
// Esse processo continua até que toda a lista esteja ordenada.
public class SelectionSort {
    private int[] vetor;

    public void setVetor(int[] vetor) {
        this.vetor = vetor;
    }

    public int[] getVetor() {
        return vetor;
    }

    public SelectionSort(){}

    public SelectionSort(int[] vetor) {
        this.setVetor(vetor);
    }

    private void ordenandoVetor() {
        for (int i = 0; i < vetor.length - 1; i++) {
            int iMenor = i;
            for (int j = i + 1; j < vetor.length; j++) {
                if(vetor[j] < vetor[iMenor]) {
                    iMenor = j;
                }
            }

            int temp = vetor[iMenor];
            vetor[iMenor] = vetor[i];
            vetor[i] = temp;
        }
    }

    public void printandoVetor() {
        ordenandoVetor();

        for (int i = 0; i < vetor.length; i++) {
            System.out.println(vetor[i]);
        }
    }
}


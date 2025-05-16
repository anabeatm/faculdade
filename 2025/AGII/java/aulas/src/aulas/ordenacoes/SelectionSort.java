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
        // Enquanto i for menor que o tamanho do vetor - 1
        for (int i = 0; i < vetor.length - 1; i++) {
            int iMenor = i; // inicia uma variável iMenor com o valor sendo o índice i
            for (int j = i + 1; j < vetor.length; j++) { // enquanto j for o próximo número (i + 1)
                // e j for menor que o tamanho do vetor
                if(vetor[j] < vetor[iMenor]) { // ent, se vetor em j for menor que vetor em iMenor
                    iMenor = j; // iMenor se torna o valor j
                }
            }
            // aí fora do segundo for
            int temp = vetor[iMenor]; // cria uma variável auxiliar/temporária, onde receberá valor em iMenor
            vetor[iMenor] = vetor[i]; // o valor em iMenor se torna o valor em i
            vetor[i] = temp; // e por último, valor em i se torna o valor em temp
        }
    }

    public void printandoVetor() {
        ordenandoVetor();

        for (int i = 0; i < vetor.length; i++) {
            System.out.println(vetor[i]);
        }
    }
}


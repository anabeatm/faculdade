package aulas.ordenacoes;

public class MergeSortOutroJeito {
    int[] vetorOriginal;

    public void setVetorOriginal(int[] vetorOriginal) {
        this.vetorOriginal = vetorOriginal;
    }

    public MergeSortOutroJeito(int[] vetorOriginal) {
        this.setVetorOriginal(vetorOriginal);
    }

    public void mergeSort(int[] vetorOriginal) {
            int tamanhoVetor = vetorOriginal.length;

            if(tamanhoVetor < 2) {return;}

            int meioIndex = tamanhoVetor / 2;

            int[] vetorDaEsquerda = new int[meioIndex];
            int[] vetorDaDireita = new int[tamanhoVetor - meioIndex];

            for(int i = 0; i < meioIndex; i++) {
                vetorDaEsquerda[i] = vetorOriginal[i];
            }

            for(int i = meioIndex; i < tamanhoVetor; i++) {
                vetorDaDireita[i - meioIndex] = vetorOriginal[i];
            }
    
            mergeSort(vetorDaEsquerda);
            mergeSort(vetorDaDireita);

            merge(vetorOriginal, vetorDaEsquerda, vetorDaDireita);
    }

    private void merge(int[] vetorOriginal, int[] vetorDaEsquerda,int[] vetorDaDireita) {
        int tamanhoVetorEsq = vetorDaEsquerda.length;
        int tamanhoVetorDir = vetorDaDireita.length;

        int indexEsq = 0, indexDir = 0, indexOrig = 0;

        while(indexEsq < tamanhoVetorEsq && indexDir < tamanhoVetorDir) {
            if(vetorDaEsquerda[indexEsq] <= vetorDaDireita[indexDir]) {
                vetorOriginal[indexOrig] = vetorDaEsquerda[indexEsq];
                indexEsq++;
            } else {
                vetorOriginal[indexOrig] = vetorDaDireita[indexDir];
                indexDir++;
            }
            indexOrig++;
        }

        while(indexEsq < tamanhoVetorEsq) {
            vetorOriginal[indexOrig] = vetorDaEsquerda[indexEsq];
            indexEsq++;
            indexOrig++;
        }
        while(indexDir < tamanhoVetorDir) {
            vetorOriginal[indexOrig] = vetorDaDireita[indexDir];
            indexDir++;
            indexOrig++;
        }
    }
    public void imprimir() {
        for(int i = 0; i < vetorOriginal.length; i++) {
            System.out.print(vetorOriginal[i] + " ");
        }
    }
}
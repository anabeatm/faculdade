package aulas.ordenacoes;
// LÓGICA:
// O algoritmo atua dividindo o vetor em sub-vetores cada vez menores até que cada um contenha apenas um elemento
// (o que significa que estão ordenados), e então intercala esses sub-vetores de maneira ordenada
// para formar o vetor final.
public class MergeSort {
    private int[] vetor;
    private int[] temp;

    public void setVetor(int[] vetor) {
        this.vetor = vetor;
    }

    public int[] getVetor() {
        return vetor;
    }

    public void setTemp(int[] temp) {
        this.temp = temp;
    }

    public int[] getTemp() {
        return temp;
    }

    public MergeSort(){}

    public MergeSort(int[] vetor) {
        this.setVetor(vetor);
        this.temp = new int[vetor.length];
    }

    public void ordenar() {
        mergeSort(0, vetor.length - 1);
    }

    private void mergeSort(int inicio, int fim) {
        if(inicio < fim) {
            int meio = (inicio + fim) / 2;
            mergeSort(inicio, meio);
            mergeSort(meio + 1, fim);
            intercalar(inicio, meio, fim);
        }
    }

    private void intercalar(int inicio, int meio, int fim) {
        for (int i = inicio; i <= fim ; i++) {
            temp[i] = vetor[i];
        }

        int esquerda = inicio;
        int direita = meio + 1;

        for (int i = inicio; i <= fim ; i++) {
            if(esquerda > meio){
                vetor[i] = temp[direita++];

            } else if (direita > fim) {
                vetor[i] = temp[esquerda++];

            } else if (temp[esquerda] < temp[direita]) {
                vetor[i] = temp[esquerda++];

            } else {vetor[i] = temp[direita++];}
        }
    }

    public void imprimir() {
        ordenar();
        for (int i = 0; i < vetor.length; i++) {
            System.out.println(vetor[i]);
        }
    }
}

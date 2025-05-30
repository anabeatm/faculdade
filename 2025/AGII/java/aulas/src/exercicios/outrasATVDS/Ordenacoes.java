package exercicios.outrasATVDS;
import java.util.Arrays;

public class Ordenacoes {
    int troca = 0;
    public static void main(String[] args) {
//        int[] vetor = {7, 3, 9, 2, 6};
//        Ordenacoes bubble = new Ordenacoes();
//        bubble.bubbleSort(vetor);
//        System.out.println("--> " + Arrays.toString(vetor));

//        int[] vetor = {29, 10, 14, 37, 13};
//        Ordenacoes selection = new Ordenacoes();
//        selection.selectionSort(vetor);
//        System.out.println("--> " + Arrays.toString(vetor));
//        System.out.println("Quantidade de trocas: " + selection.troca);

//        int[] vetor = {8, 4, 1, 5, 9, 2};
//        Ordenacoes insertion = new Ordenacoes();
//        insertion.insertionSort(vetor);

        int[] vetor = {38, 27, 43, 3, 9, 82, 10};
        Ordenacoes merge = new Ordenacoes();
        merge.mergeSort(vetor, 0, vetor.length - 1);
        System.out.println("--> " + Arrays.toString(vetor));
    }

    private void bubbleSort(int[] array) {
        for(int i = 0; i < array.length - 1; i++) {
            for(int j = 0; j < array.length - 1; j++) {
                if(array[j] > array[j + 1]) {
                    int aux = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = aux;
                }
            }
            System.out.println("Passagem " + (i + 1) + ": " + Arrays.toString(array));
        }
    }

    private void selectionSort(int[] array) {
        for(int i = 0; i < array.length - 1; i++) {
            int iMenor = i;
            for(int j = i + 1; j < array.length; j++) {
                if(array[iMenor] > array[j]) {
                    iMenor = j;
                }
            }
            int temp = array[i];
            array[i] = array[iMenor];
            array[iMenor] = temp;
            troca++;
        }
    }

    private void insertionSort(int[] array) {
        for(int i = 1; i < array.length; i++) { // errei aqui
            int key = array[i];
            int j = i - 1; // errei aqui
            while(j >= 0 && array[j] > key) {
                array[j + 1] = array[j]; // errei aqui
                j--;
            }
            array[j + 1] = key; // errei aqui
            System.out.println("Inserção " + i + ": " + Arrays.toString(array));
        }
    }

    private void mergeSort(int[] array, int inicio, int fim){
        if(inicio < fim) {
            int meio = (inicio + fim) / 2;
            System.out.println(Arrays.toString(array));
            System.out.println("-------------------------------------------------------");

            mergeSort(array, inicio, meio);
            mergeSort(array,meio + 1, fim);
            merge(array, inicio, meio, fim);

            System.out.println(Arrays.toString(array));
            System.out.println("-------------------------------------------------------");
        }
    }
    private void merge(int[] array, int inicio, int meio, int fim){
        int[] vetorTemp = new int[fim - inicio + 1];

        int esquerda = inicio;
        int direita = meio + 1;
        int index = 0;

        while(esquerda <= meio && direita <= fim){
            if(array[esquerda] <= array[direita]) {
                vetorTemp[index++] = array[esquerda++];
            } else {
                vetorTemp[index++] = array[direita++];
            }
        }
        while(esquerda <= meio) {
            vetorTemp[index++] = array[esquerda++];
        }
        while (direita <= fim) {
            vetorTemp[index++] = array[direita++];
        }

        for(int i = 0; i < vetorTemp.length; i++) {
            array[inicio + i] = vetorTemp[i];
        }
    }
}

package aulas;

import aulas.ordenacoes.BubbleSort;
import aulas.ordenacoes.InsertionSort;
import aulas.ordenacoes.MergeSort;
import aulas.ordenacoes.SelectionSort;

public class Main {
    public static void main(String[] args) {
        System.out.println("--BUBBLE SORT--");
        int[] bubbleArray = {5, 1, 4, 2, 8};
        BubbleSort bubble = new BubbleSort(bubbleArray);
        bubble.printandoVetor();

        System.out.println("--SELECTION SORT--");
        int[] selectionArray = {29, 10, 14, 37, 13};
        SelectionSort selection = new SelectionSort(selectionArray);
        selection.printandoVetor();

        System.out.println("--INSERTION SORT--");
        int[] insertionArray = {6, 98, 12, 9, 24};
        InsertionSort insertion = new InsertionSort(insertionArray);
        insertion.printandoVetor();

        System.out.println("--MERGE SORT--");
        int[] mergeSortArray = {65, 98, 12, 5, 23, 76, 19, 87, 1, 1009};
        MergeSort merge = new MergeSort(mergeSortArray);
        merge.imprimir();
    }
}

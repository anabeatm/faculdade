package aulas;

import aulas.ordenacoes.BubbleSort;
import aulas.ordenacoes.InsertionSort;
import aulas.ordenacoes.MergeSort;
import aulas.ordenacoes.SelectionSort;
import aulas.ordenacoes.MergeSortOutroJeito;
import aulas.recursao.Fibonacci;
import aulas.recursao.BuscaBinaria;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
//        System.out.println("--BUBBLE SORT--");
//        int[] bubbleArray = {5, 1, 4, 2, 8};
//        BubbleSort bubble = new BubbleSort(bubbleArray);
//        bubble.printandoVetor();
//
//        System.out.println("--SELECTION SORT--");
//        int[] selectionArray = {29, 10, 14, 37, 13};
//        SelectionSort selection = new SelectionSort(selectionArray);
//        selection.printandoVetor();
//
//        System.out.println("--INSERTION SORT--");
//        int[] insertionArray = {6, 98, 12, 9, 24};
//        InsertionSort insertion = new InsertionSort(insertionArray);
//        insertion.printandoVetor();
//
//        System.out.println("--MERGE SORT--");
//       int[] mergeSortArray = {65, 98, 12, 5, 23, 76, 19, 87, 1, 1009};
//        MergeSort merge = new MergeSort(mergeSortArray);
//        merge.imprimir();

//        System.out.println("Array anterior:");
//        for(int i = 0; i < mergeSortArray.length; i++) {
//            System.out.print(mergeSortArray[i] + " ");
//        }
//        MergeSortOutroJeito merge2 = new MergeSortOutroJeito(mergeSortArray);
//        merge2.mergeSort(mergeSortArray);
//        System.out.println("\nArray depois:");
//        merge2.imprimir();
//        Fibonacci fibonacci = new Fibonacci();
//        fibonacci.imprimirFibonacci(8);

        BuscaBinaria busca = new BuscaBinaria();
        int[] array = {29, 10, 14, 37, 13};
        busca.ordenandoVetor(array);
        System.out.println(Arrays.toString(array));
        int result = busca.busca(array, 29, 0, array.length);
    }
}

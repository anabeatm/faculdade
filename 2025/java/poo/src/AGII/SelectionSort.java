package AGII;
import java.util.Scanner;

public class SelectionSort {
    public static String[] selectionSort(String[] array) {
        int tamanho = array.length;
        for(int i = 0; i < tamanho - 1; i++) {
            int iMenor = i;


            for(int c = i + 1; c < tamanho; c++) {
                if(array[c].compareTo(array[iMenor]) < 0) {
                    iMenor = c;
                }
            }
            if(iMenor != i) {
                String aux = array[iMenor];
                array[iMenor] = array[i];
                array[i] = aux;
            }
        }
        return array;
    }



    public static void main(String[] args) {
        String[] array = {"joão", "mariana", "ana"};
         String[] ordenou = selectionSort(array);
         for(int i = 0; i < array.length; i++) {
             System.out.println(ordenou[i]);
         }
    }

}




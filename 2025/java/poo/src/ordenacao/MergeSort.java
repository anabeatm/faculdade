package ordenacao;

public class MergeSort {
    public static void main(String[] args) {
        int[] vetor = {6, 32, 9, 10, 3};

        boolean find = false;
        int start = 0;
        int end = vetor.length - 1;

        int contadorWhile = 0;
        int contadorFor = 0;

        int valorQueQuero = 32;

        int middle = 0;

        while (start <= end) {
            middle = (start + end) / 2;
            contadorWhile++;

            if (valorQueQuero == vetor[middle]) {
                find = true;
                break;
            } else {
                if (valorQueQuero > vetor[middle]) {
                    start = middle + 1;
                } else {
                    end = middle - 1;
                }
                contadorWhile++;
            }
        }

        for (int c = 0; c < vetor.length; c++) {
            contadorFor++;
            if (valorQueQuero == vetor[c]) {
                find = true;
                break;
            }
        }

        if (find) {
            System.out.printf("Valor %s encontrado no índice %s", valorQueQuero, middle);
        }
    }


}

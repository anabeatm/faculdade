package aulas.recursao;

public class BuscaBinaria {
    public void ordenandoVetor(int[] num) {
        for (int i = 0; i < num.length - 1; i++) {
            int iMenor = i;
            for (int j = i + 1; j < num.length; j++) {
                if(num[iMenor] > num[j]) {
                    iMenor = j;
                }
            }
            int temp = num[iMenor];
            num[iMenor] = num[i];
            num[i] = temp;
        }
    }

    public int busca(int[] num, int elementoBusca, int inicio, int fim) {
        if(inicio > fim) {
            return -1;
        }
        int meio = (inicio + fim) / 2;

        if(num[meio] == elementoBusca) {
            System.out.println("Elemento encontrado no índice: " + meio);
            return meio;
        }

        if(elementoBusca < num[meio]) {
            return busca(num, elementoBusca, inicio, meio - 1);
        } else {
            return busca(num, elementoBusca, meio + 1, fim);
        }
    }
}

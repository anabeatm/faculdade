package teste.model;

public class Teste {   
    public int descobrindoMaiorNum(int[] vetor) {
        int tamanho = vetor.length;
        int maiorNumero = vetor[0];

        for(int i = 0; i < tamanho; i++) {
            if(maiorNumero < vetor[i]) {
                maiorNumero = vetor[i];
            } 
        }
        return maiorNumero;
    }

    public String selectionSort(int[] vetor) {
        int tamanho = vetor.length;
        for(int i = 0; i < tamanho; i++) {
            
            int indiceMin = i;

            for(int j = i + 1; j < tamanho; j++) {
                if(vetor[j] < vetor[indiceMin]) {
                    indiceMin = j;
                }
            }

            int temp = vetor[indiceMin];
            vetor[indiceMin] = vetor[i];
            vetor[i] = temp;
        }
        return java.util.Arrays.toString(vetor);
    }
}
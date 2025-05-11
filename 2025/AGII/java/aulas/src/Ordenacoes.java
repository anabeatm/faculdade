public class Ordenacoes {
    public static void main(String[] args) throws Exception {
        int vetor[] = {9, 4, 3, 6, 1, 10};
        System.out.println("BUBBLE SORT");
        bubbleSort(vetor);
        print(vetor);

        int vetor2[] = {9, 4, 3, 6, 1, 10};
        System.out.println("INSERTION SORT");
        insertionSort(vetor2);
        print(vetor2);
    }

    // BUBBLE SORT
    public static void bubbleSort (int numeros[]) {
        int length = numeros.length; // Obtém o tamanho do array
        int count = 0; // Contador para monitorar o número de comparações

        // Loop externo: controla o número de passagens pelo array
        for(int i = 0; i < length - 1; i++) {
            Boolean swap = false; // Flag para verificar se houve trocas nesta passagem

            for(int j = 0; j < length - 1 - i; j++) {  // Loop interno: faz as comparações entre elementos adjacentes
                // length - 1 - i: a cada passagem, o maior elemento já está na posição correta,
                // então não precisamos comparar com os últimos elementos já ordenados
                count++; // Incrementa o contador de comparações

                if(numeros[j] > numeros[j + 1]) {  // Compara o elemento atual com o próximo
                    // Realiza a troca dos elementos (swap)
                    int aux = numeros[j]; // Armazena o valor atual temporariamente
                    numeros[j] = numeros[j + 1]; // Move o valor menor para a posição atual
                    numeros[j + 1] = aux; // Move o valor maior para a próxima posição
                    swap = true; // Indica que houve pelo menos uma troca
                }
            }
            // Se não houve trocas nesta passagem, o array está ordenado
            if(!swap) break;
            // Otimização: encerra o algoritmo prematuramente se já estiver ordenado
        }
        // Imprime o número total de comparações realizadas
        System.out.println("Contador: " + count);
    }

    public static void print(int vetor[]) {
        for (int i = 0; i < vetor.length; i++) {
            System.out.print(vetor[i] + " \n");
        }
    }

    // INSERTION SORT
    public static void insertionSort(int numeros[]) {
        // Loop começa do segundo elemento (i = 1), pois o primeiro já está "ordenado" por definição
        for(int i = 1; i < numeros.length; i++) {
            int key = numeros[i]; // Armazena o valor atual que será inserido na posição correta
            int j = i - 1; // Inicia um índice 'j' para comparar com os elementos anteriores

            // Enquanto 'j' não ultrapassar o início do array AND o elemento na posição 'j' for maior que 'key'
            while(j >= 0 && numeros[j] > key) {
                numeros[j + 1] = numeros[j]; // Move o elemento maior uma posição para frente
                j -= 1; // Decrementa 'j' para comparar com o próximo elemento anterior
            }
            // Insere 'key' na posição correta (onde o elemento anterior é menor ou igual)
            numeros[j + 1] = key;
        }
    }
}

package ordenacao;

public class BubbleSort {
	public static void main(String[] args) {
		int vetor[] = {0,1,2,3,4,5};
		ordenar(vetor);
		imprimir(vetor);
	
	}
	
	public static void imprimir(int vetor[]) {
		for (int x = 0; x < vetor.length; x++) {
			System.out.print(vetor[x]+" ");
		}
	}

	public static void ordenar(int numeros[]) {
		int tamanho = numeros.length;
		int contador = 0;
		for (int x = 0; x < tamanho - 1; x++) {
			Boolean  trocou = false;
			for (int y = 0; y < tamanho - 1 - x; y++) {
				contador++;
				if (numeros[y] > numeros[y + 1]) {
					int aux = numeros[y];
					numeros[y] = numeros[y + 1];
					numeros[y + 1] = aux;
					trocou = true;
				}				
			}
			//se trocou for igual a false
			if(!trocou) break;
		}
		System.out.println("Contador: "+ contador);
	}
}

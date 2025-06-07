// LISTA ENCADEADA/LINKED LIST
// NÃO HÁ LIMITAÇÃO DE ELEMENTOS
public class linkedList{
  No head;
  
  public void adicionarInicio(int valor) {
    No novoElemento = new No(valor);
    if(head == null) {head = novoElemento;}
    else {
      novoElemento.proximoValor = head;
      head = novoElemento;
    }

    public void adicionarFim(int valor) {
      if(head == null) {adicionarInicio(int valor);} 
      else {
        No novoElemento = new No(valor);
        No aux = head;
        while(aux.proximoValor != null) {
          aux = aux.proximoValor;
        }
        aux.proximoValor = novoElemento;
    }

    public void adicionarMeio(int valor, int valorReferencia) {}


    public void imprimir() {
      No aux = head;
      while(aux != null) {
        System.out.print(aux.valor + " -> ");
        aux = aux.proximoValor;
      }
    }
    System.out.print("null");
    System.out.println();
  }
  
  private class No {
    int valor;
    No proximoValor;

    public No(int valor) {
      this.valor = valor;
      this.proximoValor = null;
    }
  }
  
  public static void main(String[] args) {
    linkedList lista = new linkedList();
    lista.adicionarInicio(10);
    lista.adicionarInicio(5);
    lista.imprimir();
  }
  
}

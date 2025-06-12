
package app;

import model.Animal;
import model.Ave;
import model.Mamifero;

public class Main {
  public static void main(String[] args) {
    Ave queroQuero = new Ave(1, .100, "Quero quero", .50, "reto", "branco", true);

    queroQuero.emitirSom(); // polimorfismo --> capacidade de objetos de diferentes classes responder a mesma mensagem (chamada a um método) de maneira diferente, dependendo da sua classe

    Animal queroQuero = new Ave(1, .100, "Quero quero", .50, "reto", "branco", true);
    queroQuero.emitirSom();
    // saída: pia

    List<Animal> listaAnimal = new ArrayList<Animal>(20);
    listaAnimal.add(queroQuero);

    Mamifero vaca = new Mamifero(10, 150, "Vaca", true, true);
    vaca.emitirSom();

    listaAnimal.add(vaca);
    
  }
}

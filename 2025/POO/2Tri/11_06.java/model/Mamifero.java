package model;

public class Mamifero extend Animal {
  private boolean temPelo;
  private String rabo;
  private String som;

  public Mamifero (int idade, double peso, String nomePopular, boolean temPelo, String rabo, String som) {
    this.idade = idade;
    this.peso = peso;
    this.nomePopular = nomePopular;
    this.temPelo = temPelo;
    this.rabo = rabo;
    this.som = som;
  }

 // @Override
   /// public void emitirSom() {
     // System.out.println("")
   // }
}

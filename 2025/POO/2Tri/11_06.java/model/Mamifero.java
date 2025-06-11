package model;

public class Mamifero extend Animal {
  private boolean isTemPelo;
  private boolean rabo;
  private String som;

  public Mamifero (int idade, double peso, String nomePopular, boolean isTemPelo, boolean rabo, String som) {
    super(idade, peso, nomePopular);
    this.isTemPelo = isTemPelo;
    this.rabo = rabo;
    this.som = som;
  }

 // @Override
   /// public void emitirSom() {
     // System.out.println("")
   // }
}

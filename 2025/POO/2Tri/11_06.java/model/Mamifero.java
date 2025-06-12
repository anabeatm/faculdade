package model;

public class Mamifero extend Animal {
  private boolean isTemPelo;
  private boolean rabo;
  private String som;

  public Mamifero (int idade, double peso, String nomePopular, boolean isTemPelo, boolean rabo, String som) {
    super(idade, peso, nomePopular);
    this.som = som;
  }

  public boolean isTemPelo() {
    return isTemPelo;
  }

  public void setIsTemPelo(boolean isTemPelo) {
    this.isTemPelo = isTemPelo;
  }

  public boolean rabo() {
    return rabo;
  }

public void setRabo(boolean rabo) {
  this.rabo = rabo;
}

  @Override
  public String toString() {
    return "Nome: " + nomePopular + " Rabo: " + rabo
  }

 // @Override
   /// public void emitirSom() {
     // System.out.println("")
   // }

  @Override
    public void locomocao() {
      System.out.println("anda");
    }
}

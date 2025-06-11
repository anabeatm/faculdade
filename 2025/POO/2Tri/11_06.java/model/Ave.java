package model;

public class Ave extend Animal {
  private double envergadura;
  private String formatoBico;
  private String corOvo;
  private boolean voa;
  
  public Ave(int idade, double peso, String nomePopular, double envergadura, String formatoBico, String corOvo, boolean voa) {
    super(idade, peso, nomePopular); // --> comando para chamar construtores de classes superiores
    this.evergadura = envergadura;
    this.formatoBico = formatoBico;
    this.corOvo = corOvo;
    this.voa = voa;
  } // necessário existir um construtor padrão na classe mãe ou NENHUM construtor; sem um construtor padrão é possível utilizar o super

  @Override
    public void emitirSom() {
      System.out.println("pia");
    }
}

// HERANÇA --> é um conceito fundamental que permite que uma classe (classe derivada) herde atributos e métodos de outra classe (classe base)
package model;

public class Animal {
  protected int idade;
  protected double peso;
  protected String nomePopular;

  public Animal (int idade, double peso, String nomePopular) {
    this.idade = idade;
    this.peso = peso;
    this.nomePopular = nomePopular;
  }

  public void emitirSom() {
    System.out.println("som não definido")
  }
}

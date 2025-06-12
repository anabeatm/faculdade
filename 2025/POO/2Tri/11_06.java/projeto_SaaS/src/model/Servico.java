package model;

public abstract class Servico {
    protected String nome;
    protected double custoBaseHora;
    protected boolean status;
    protected String ambiente;

    public Servico(String nome, double custoBaseHora, boolean status, String ambiente) {
        this.nome = nome;
        this.custoBaseHora = custoBaseHora;
        this.status = status;
        this.ambiente = ambiente;
    }

    public void setNome (String nome) {
        this.nome = nome;
    }
    public void setStatus (double custoBaseHora) {
        this.custoBaseHora = custoBaseHora;
    }
    public void setAmbiente (String ambiente) {
        this.ambiente = ambiente;
    }

    public String getNome () {return this.nome;}
    public double getCustoBaseHora() {return this.custoBaseHora;}
    public String getAmbiente() {return this.ambiente;}


    public abstract double calcularCusto (int horas);

    public abstract String gerarRelatorio(int horas);

    public void ativar() {
        this.status = true;
    }
    public void desativar() {
        this.status = false;
    }
    public boolean isAtivo() {
        return this.status;
    }

}

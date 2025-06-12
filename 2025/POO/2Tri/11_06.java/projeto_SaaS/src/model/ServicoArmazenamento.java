package model;

public class ServicoArmazenamento extends Servico{
    protected int capacidadeGB;
    protected String redundancia;

    public ServicoArmazenamento(String nome, double custoBaseHora, boolean status, String ambiente, int capacidadeGB,
                                String redundancia) {
        super(nome, custoBaseHora, status, ambiente);
        this.capacidadeGB = capacidadeGB;
        this.redundancia = redundancia;
    }

    @Override
    public double calcularCusto (int horas) {
        return custoBaseHora * horas;
    }

    @Override
    public String gerarRelatorio(int horas) {
        double custoTotal = calcularCusto(horas);
        String relatorio = String.format("""
                Nome do Serviço: %s
                Custo fixo: %s
                Status: %s
                Ambiente: %s
                Capacidade em GB: %s
                Custo total: R$%s
                """, nome, custoBaseHora, status, ambiente, capacidadeGB, custoTotal);
        return relatorio;
    }
}

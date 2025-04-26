public class Cliente {
    private String nomeCliente;
    private String cpf;

    public void setNomeCliente(String nome) {
        this.nomeCliente = nome;
    }

    public String getNomeCliente() {
        return this.nomeCliente;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public Cliente() {
        this.nomeCliente = "";
        this.cpf = "";
    }
}

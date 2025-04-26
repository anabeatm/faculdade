// qualificadores de acesso:
// -> default, protected, private e public



public class Conta {
    private double saldo;
    private Cliente cliente;

    public Conta() {
        this.saldo = 0.;
    }




    public void depositar(double valor) {

    }

    public void sacar(double valor) {

    }

    public void setClientethis(Cliente nomeCliente) {
        this.cliente = nomeCliente;
    }

    public double getSaldo() {
        return this.saldo;
    }
}

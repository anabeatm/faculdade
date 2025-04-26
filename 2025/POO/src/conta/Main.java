public class Main {
    public static void main(String[] args) {
        Conta conta = new Conta();
        Cliente cliente = new Cliente();

        cliente.setNomeCliente("Bonde das Maravilhas");
        conta.setClientethis(cliente);
        System.out.print(conta.getSaldo());
    }
}
public class Carro {
    // qualificadores de acesso
    //  (visibilidade/quem pode acessar):
    //          default, private, public e protected
    String modelo;
    public Integer velocidadeMaxima = 0;
    Integer velocidadeMomento = 0;
    Integer posicao = 0;

    void acelerar() {
        if(velocidadeMomento < velocidadeMaxima) {
            velocidadeMomento += 5;
        }
    }
    void frear() {
        if(velocidadeMomento > velocidadeMaxima) {
            velocidadeMomento -= 5;
        }
    }
    Integer status() {
        return velocidadeMomento;
    }
    void trocarPosicao(Carro outroCarro) {
        int posicaoOutroCarro = outroCarro.posicao;
        outroCarro.posicao = posicao;
        posicao = posicaoOutroCarro;
    }
}

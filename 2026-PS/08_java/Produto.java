public class Produto {

    private int codigo;
    private String nome;
    private double preco;

    public Produto(int codigo, String nome, double preco) {
        this.codigo = codigo;
        this.nome = nome;
        this.preco = preco;
    }

    public double getPreco(){
        return preco;
    }
    public String getNome(){
        return nome;
    }
    public int getCodigo(){
        return codigo;
    }

    public void setPreco(double preco){
        this.preco = preco;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setCodigo(int codigo){
        this.codigo = codigo;
    }


    public void alterarPreco(double preco, double desconto) {
        this.preco = preco - (preco * desconto / 100);
    }
    @Override
    public String toString() {
    return codigo + " - " + nome + " - R$ " + preco;
}
}
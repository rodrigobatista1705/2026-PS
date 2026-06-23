public class cardSB{
    public static void exibirProduto(String nome){
        System.out.println("Produto: " + nome);
    }

    public static void exibirProduto(String nome, double preco){
        System.out.println("Produto: "+nome + "\nPreço: " + preco);
    }
    public static void main(String[] args) {
        exibirProduto("Refrigerante");
        exibirProduto("Pizza",39.90);
        exibirProduto("Hambúrguer",22.50);
    }
}


import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        ArrayList<Produto> produtos = new ArrayList<Produto>();



        while (true) {

            System.out.println("\n=== SISTEMA DE PRODUTOS ===");
            System.out.println("1 - Cadastrar");
            System.out.println("2 - Listar");
            System.out.println("3 - Alterar preco");
            System.out.println("4 - Remover");
            System.out.println("5 - Sair");
            System.out.print("Opcao: ");

            String opcao = teclado.nextLine().trim();
            teclado.nextLine();

            if (opcao.equals("5")){
                System.out.println("Sistema encerrado.");
                break;
            }else if (opcao.equals("1")) {
                cadastrar(produtos, teclado);

            } else if (opcao.equals("2")) {
                listar(produtos);

            } else if (opcao.equals("3")) {
                AltPreco(produtos, teclado);

            } else if (opcao.equals("4")) {
                remove(produtos, teclado);
            }
                
        }
    }

    public void cadastrar(ArrayList<Produto> produtos, Scanner teclado){
        System.out.print("Codigo: ");
        int codigo = teclado.nextInt();
        teclado.nextLine();

        System.out.print("Nome: ");
        String nome = teclado.nextLine();

        System.out.print("Preco: ");
        double preco = teclado.nextDouble();

        Produto p = new Produto(codigo, nome, preco);
        produtos.add(p);
    }


    public void listar(ArrayList<Produto> produtos){
        if (produtos.size()== 0 ){
            System.out.println("Nenhuma produto cadastrado");
        }else{
            System.out.println("\n --- Quantidade em estoque: " + produtos.size() + " ---");
            for(int i=0; i<produtos.size(); i++){
                Produto prd = produtos.get(i);
                System.out.println(produtos);
            }
        }
    }

    public void AltPreco(ArrayList<Produto> produtos, Scanner teclado){
        System.out.print("Produto para Alterar o preco: ");
        int codigo = teclado.nextInt();
        Produto p = buscarPorCodigo(produtos, codigo);
        if (p== null){
            System.out.println("Nenhum Produto encontrado com esse codigo: " + codigo +".");
            return;
        }
        System.out.print("Novo Preco de "+ p.getNome() + ": ");
        double novoPreco = teclado.nextDouble();
        p.setPreco(novoPreco);
        System.out.println("Preco atualizado: "+ p);
    }


    static Produto buscarPorCodigo(ArrayList<Produto> produtos, int codigo){
        for (int i = 0; i< produtos.size(); i++){
            Produto p = produtos.get(i);
            if(p.getcodigo() == codigo){
                return p;
            }
        }
        return null;
    }


    static void remove (ArrayList<Produto> produtos, Scanner teclado){
        System.out.print("Codigo do produto a remover: ");
        int codigo = teclado.nextInt();
        Produto p = buscarPorCodigo(produtos, codigo);
        if (p == null){
            System.out.println("Nenhum produto com esse codigo encontrado " + codigo +".");
            return;
        }
        System.out.println("Tem certeza que quer remover " + p.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")){
            produtos.remove(p);
            System.out.println("Produto removido.");
        }else {
            System.out.println("Remocao cancelada");
        }
    }
}
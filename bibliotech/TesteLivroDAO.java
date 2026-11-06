public class TesteLivroDAO {

    public static void main(String[] args) {

    LivroDAO dao = new LivroDAO();

    boolean resultado = dao.adicionarLivro("Pequeno Principe", "Antoine de Saint-Exupery", 1943);

    boolean resultado2 = dao.adicionarLivro("The X-Men", "Stan Lee e Jack Kirby", 1963);

    boolean resultado3 = dao.adicionarLivro("Amazing Fantasy", "Stan Lee e Steve Ditko", 1962);

    //boolean resultado4 = dao.atualizarLivro(22, "Espetacular Homem-Aranha - Edição Especial", "Stan Lee e Steve Ditko", 1962);
    //boolean atualizou = dao.atualizarLivro( 999999, "Livro Inexistente", "Autor Desconhecido",  2026);

    //boolean excluiu = dao.excluirLivro(999999);

    //System.out.println("Atualização: " + atualizou);

    //System.out.println("Exclusão: " + excluiu);
     
    //boolean resultado = dao.excluirLivro(21);
      
        System.out.println("Livro adicionado: " + resultado);
        System.out.println("Livro adicionado: " + resultado2);
        System.out.println("Livro adicionado: " + resultado3);
        //System.out.println("Livro atualizado: " + resultado4);
        //System.out.println("Livro excluido: " + resultado);

}
}
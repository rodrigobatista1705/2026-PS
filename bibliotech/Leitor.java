/*
 * Disciplina : 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : Leitor.java
 * Autor      : Rodrigo Lima dos Santos Batista
 * Descricao  : Leior e um tipo de usuario: herda nome, matricula e entrar().
 */
public class Leitor extends Usuario{

    //So o que a caixa Leitor acrescenta. nOme e matricula ja vem de Usuario.
    private int limiteEmprestimos;
    private int livrosEmMaos; // nao estava na caixa o docdigo pediu

    public Leitor(String nome, String matricula, int limiteEmprestimos){
        super(nome, matricula); // primeiro a parte de Usuario, depois a de leitor 
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }

    public int getLimiteEmprestimos(){
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos(){
        return livrosEmMaos;
    }

    //Operacao da caixa: podePegarEmprestado()
    public boolean podePegarEMprestado(){
        return livrosEmMaos< limiteEmprestimos;
    }

    // Os dois metodos que o emprestimo vai usar na Aula 38
    public void pegouLivro(){
        this.livrosEmMaos = this.livrosEmMaos +1;
    }

    public void devolveuLivro(){
        this.livrosEmMaos = this.livrosEmMaos -1;
    }

    public String toString(){
        return "Leitor "+ getNome()+ " ("+ getMatricula()+") - "+ livrosEmMaos + " de "+ limiteEmprestimos + " livros";
    }
}

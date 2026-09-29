/*
 * Disciplina : 2026-PS
 * Projeto    : bibliotech
 * Arquivo    : bibliotecario.java
 * Autor      : Rodrigo Lima dos Santos Batista
 * Descricao  : Biblioteca eh um tipo de usuario, com a matricula funcional.
 */
public class Bibliotecario extends Usuario{

    private String matriculaFuncional;

    public Bibliotecario(String nome, String matricula, String matriculaFuncional) {
        super(nome, matricula);
        this.matriculaFuncional = matriculaFuncional;
    }

    public String getMatriculaFuncional() {
        return matriculaFuncional;
    }

    public boolean consultarMatriculaFuncional() {
        return true;
    }

    public String toString() {
        return "Bibliotecario(a) " + getNome() + " (" + getMatricula() + ", funcional " + matriculaFuncional + ")";
    }
}
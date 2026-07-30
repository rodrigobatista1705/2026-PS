public class aluno {
    private int matricula;
    private String nome;
    private String curso;

    public aluno(int matricula, String nome,String curso){
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }
    public int getMatricula(){
        return matricula;
    }

    public String getNome(){
        return nome;
    }

    public String getCurso(){
        return curso;
    }

    public void setMatricula(int matricula){
        if (matricula > 0){
            this.matricula=matricula;
        }
    }
    
    public void setNome(String nome){
        if (nome != null && !nome.isBlank()){
            this.nome=nome;
        }
    }

    public void setCurso(String curso){
        if (nome != null && !nome.isBlank()){
            this.curso=curso;
        }
    }

    public void trancar(){
        if (this.curso != null && !this.curso.isBlank()){
            this.curso = null;
        }
    }

    public void reativar(String curso){
        if (curso != null && !curso.isBlank()){
            this.curso = curso;
        }
    }

    public void alterarCurso(String curso){
        if (curso != null && !curso.isBlank()){
            this.curso = curso;
        }
    }
}
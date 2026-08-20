/*
 * Diciplina:   2026-PS
 * Estudante:   Rorigo Lima dos Santos Batista 
 * Data     :   2026.08.13
 * Projeto  :   aula32-projeto-secretaria
 * Arquivo  :   Aluno.java
 */

public class Aluno{
    //Atributos: campos impressos
    //Private = somente o codigo desta classe mexe neles. De forra nao e possivel
    private String nome;
    private String matricula;
    private String curso;

    public Aluno(String nome, String matricula, String curso){
        //this = ESTA ficha aui (o self do java)
        // this.nome eh o atributo da ficha; nome, sozinho, e o parametro que acabou de chegar. Sem  'this', os dois seriam o parametro
        this.nome = nome;
        this.matricula = matricula;
        this.curso = curso;
    }

    //getters: as janelas leitura
    public String getNome(){
        return nome;
    }
    public String getMatricula(){
        return matricula;
    }
    public String getCurso(){
        return curso;
    }

    //Setters: aa unica porta de entrada para mudar um dado da ficha
    // Sem "setters, ninguem altera - nem por engano"
    public void setNome(String nome){
        this.nome = nome;    
    }

    public void setCurso(String curso){
        this.curso = curso;    
    }
}
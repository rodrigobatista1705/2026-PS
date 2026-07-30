public class Main {
    public static void main(String[] args){
        aluno aluno1 = new aluno(123, "rodrigo", "informatica");
        System.out.println("Matricula: " + aluno1.getMatricula());
        System.out.println("Nome: " + aluno1.getNome());
        System.out.println("Curso: " + aluno1.getCurso());
        aluno1.trancar();
        System.out.println("Curso depois de trancar: " + aluno1.getCurso());
        aluno1.reativar("informatica");
        System.out.println("Curso depois de reativar: " + aluno1.getCurso());
        
    }
}

/*
 * Diciplina:   2026-PS
 * Estudante:   Rorigo Lima dos Santos Batista 
 * Data     :   2026.08.13
 * Projeto  :   aula32-projeto-secretaria
 * Arquivo  :   Main.java
 */

// ArrayList = a lista que cresce (o gaveteiro)
import java.util.ArrayList;
import java.util.Scanner;

/*  
    * Balcao da secretaria: onde o programa vai rodar
    * Mostra o menu, le a escolha e chama o metodo que resolve
*/

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        // O Gaveteiro: o <Aluno> diz que so entra ficha de alunp aqui 
        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        // while (true) = repete infinitamente. A unica saida e o break opcao "0"
        while (true){
            System.out.println("===================================");
            System.out.println("    SECRETARIA DO RODRIGO");
            System.out.println("===================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");
            String opcao = teclado.nextLine().trim(); // trim: tira espaco das pontas

            // Texto se compara com .equal, nunca com "==" em Java
            if (opcao.equals("0")){
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            }else if(opcao.equals("1")){
                Cadastrar(lista, teclado);
            }else if (opcao.equals("2")){
                Listar(lista);
            }else if (opcao.equals("3")){
                buscar(lista, teclado);
            }else if (opcao.equals("4")){
                Atualizar(lista,teclado);
            }else if (opcao.equals("5")){
                remover(lista,teclado);
            }else{
                System.out.println("Opcao invalida! Use 0, 1, 2, 3, 4 ou 5.");
            }
        }

    }
    // Le os dados, carimba a ficha e guarda 
    static void Cadastrar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        // Verifica se ja existe um aluno com essa matricula
        Aluno existente = buscarPorMatricula(lista, matricula);
        if(existente !=null){
            System.out.println("Ja existe uma ficha com a matricula " + matricula + "!");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        System.out.print("E-mail: ");
        String email = teclado.nextLine().trim();
    
        Aluno novo = new Aluno(nome, matricula, curso, email);
        lista.add(novo);
        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    
    //percorre o gaveteiro e imprime as fichas que tiver nele
    static void Listar(ArrayList<Aluno> lista){
        if (lista.size()== 0 ){
            System.out.println("Nenhuma ficha existente");
        }else{
            System.out.println("\n--- FICHAS NO GAVETEIRO: " + lista.size() + " ---");
            for(int i=0; i<lista.size(); i++){
                Aluno ficha = lista.get(i);
                System.out.println(ficha.getMatricula() + " | " + ficha.getNome() + " | " + ficha.getCurso() + " | " + ficha.getEmail() + "\n");
            }
        }
    }
    
    // Serve para achar uma ficha pela sua matricula, e avisa quando nao existir uma
    static Aluno buscarPorMatricula(ArrayList<Aluno> lista, String matricula){
        for (int i = 0; i< lista.size(); i++){
            Aluno a = lista.get(i);
            if(a.getMatricula().equals(matricula)){
                return a;
            }
        }
        return null;
    }

    //
    static void buscar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Matricula procurada: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);

        if (a == null){
            System.out.println("Nenhuma ficha com a matricula " + matricula + " econtrada");
            return;
        }else {
            System.out.println("Resultado: " + a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso() + " | " + a.getEmail());
        }
    }
    static void Atualizar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Matricula da ficha a atualizar: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a== null){
            System.out.println("Nenhuma ficha com a matricula" + matricula +".");
            return;
        }
        System.out.print("Novo curso de "+ a.getNome() + ": ");
        String novoCurso = teclado.nextLine().trim();
        a.setCurso(novoCurso);
        System.out.println("Ficha atualizada: "+ a.getMatricula() + " | " + a.getNome() + " | " + a.getCurso() + " | " + a.getEmail());
    }
    static void remover (ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Matricula a ficha a remover: ");
        String matricula = teclado.nextLine().trim();
        Aluno a = buscarPorMatricula(lista, matricula);
        if (a == null){
            System.out.println("Nenhuma ficha com a matricula" + matricula +".");
            return;
        }
        System.out.println("Tem certeza que quer remover " + a.getNome() + "? (s/n): ");
        String resposta = teclado.nextLine().trim();
        if (resposta.equals("s")){
            lista.remove(a);
            System.out.println("Ficha removida.");
        }else {
            System.out.println("Remocao cancelada");
        }
    }
}


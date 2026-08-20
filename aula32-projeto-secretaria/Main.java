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
            }else{
                System.out.println("Opcao invalida! Use 0, 1 ou 2.");
            }
        }

        // Pergunta
        // Resposta: (a) Nao- cada new criou uma ficha independente 
    }

    static void Cadastrar(ArrayList<Aluno> lista, Scanner teclado){
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();
    
        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);
        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    static void Listar(ArrayList<Aluno> lista){
        if (lista.size()== 0 ){
            System.out.println("Nenhuma ficha existente");
        }else{
            for(int i=0; i<lista.size(); i++){
                Aluno ficha = lista.get(i);
                System.out.println("--- FICHAS NO GAVETEIRO: " + (i+1) + " ---");
                System.out.println(ficha.getMatricula() + " | " + ficha.getNome() + " | " + ficha.getCurso());
            }
        }
    }
}
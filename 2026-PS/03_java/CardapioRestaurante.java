import java.util.Scanner;
public class CardapioRestaurante{
    public static void main(String[] args){
        
        Scanner entrada = new Scanner(System.in);


        System.out.println("==========================================");
        System.out.println("     PASTEL URBANO");
        System.out.println("==========================================\n");
        System.out.println("1 - Que Pastel É Este ....... R$ 18,00");
        System.out.println("2 - Ainda Há Queijo ......... R$ 35,00");
        System.out.println("3 - Faroeste com Vinagrete .. R$ 13,00");
        System.out.println("4 - Geração Coca-Cola ....... R$ 16,00");
        System.out.println("5 - Pastéis e Massinhas ..... R$ 17,00\n");
        System.out.println("     CARDÁPIO INICIAL\n");
        System.out.println("6 - Primeiros Churros ....... R$ 15,00");
        System.out.println("7 - A Sua Banoffee .......... R$ 11,00");
        System.out.println("8 - Ganasha ................. R$ 10,00");
        System.out.println("9 - Geladeira-pência  ....... R$ 12,00\n");
        System.out.println("==========================================");
    
        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        if (opcao == 1) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+ qtd +" Que Pastel É Este.");
            System.out.println("Você vai gastar R$"+ qtd*18);
            
        
        } else if (opcao == 2) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu " +qtd+ " Ainda Há Queijo.");
            System.out.println("Você vai gastar R$"+ qtd*35);
            
        
        } else if (opcao == 3) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu " +qtd+ " Faroeste com Vinagrete.");
            System.out.println("Você vai gastar R$"+ qtd*13);
            
 
        } else if (opcao == 4) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu " +qtd+ " Geração Coca-Cola.");
            System.out.println("Você vai gastar R$"+ qtd*16);
            
        
        }else if (opcao == 5) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+qtd+ " Pastéis e Massinhas.");
            System.out.println("Você vai gastar R$"+ qtd*17);
            

        }else if (opcao == 6) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+qtd+ " Primeiros Churros.");
            System.out.println("Você vai gastar R$"+ qtd*15);
            

        }else if (opcao == 7) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+qtd+ " A Sua Banoffee.");
            System.out.println("Você vai gastar R$"+ qtd*11);
            

        }else if (opcao == 8) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+qtd+ " Ganasha.");
            System.out.println("Você vai gastar R$"+ qtd*10);
            

        }else if (opcao == 9) {
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
            System.out.println("Você pediu "+qtd+ " Geladeira-pência.");
            System.out.println("Você vai gastar R$"+ qtd*12);
            

        } else {
            System.out.println("Opção inválida.");
        }
        System.out.println("Volte Sempre 👋");
        entrada.close();
    }
}
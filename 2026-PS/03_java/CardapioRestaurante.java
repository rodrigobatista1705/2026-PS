import java.util.Scanner;
public class CardapioRestaurante{
    public static void main(String[] args){
        
        Scanner entrada = new Scanner(System.in);
        int opcao = 1;
        int preco = 0;
        int qtd_1 = 0, qtd_2 = 0, qtd_3 = 0, qtd_4 = 0, qtd_5 = 0, qtd_6 = 0, qtd_7 = 0, qtd_8 = 0, qtd_9 = 0;
        while(opcao !=0){
            System.out.println("==========================================");
            System.out.println("            PASTEL URBANO                   ");
            System.out.println("==========================================\n");
            System.out.println("1 - Que Pastel É Este ....... R$ 18,00");
            System.out.println("2 - Ainda Há Queijo ......... R$ 35,00");
            System.out.println("3 - Faroeste com Vinagrete .. R$ 13,00");
            System.out.println("4 - Geração Coca-Cola ....... R$ 16,00");
            System.out.println("5 - Pastéis e Massinhas ..... R$ 17,00\n");
            System.out.println("==========================================");
            System.out.println("            CARDÁPIO INICIAL\n              ");
            System.out.println("6 - Primeiros Churros ....... R$ 15,00");
            System.out.println("7 - A Sua Banoffee .......... R$ 11,00");
            System.out.println("8 - Ganasha ................. R$ 10,00");
            System.out.println("9 - Geladeira-pência  ....... R$ 12,00\n");
            System.out.println("==========================================");
        
            System.out.print("Escolha uma opção (0 para sair): ");
            opcao = entrada.nextInt();
            if (opcao ==0 ) break;
            System.out.print("Quantos deseja: ");
            int qtd = entrada.nextInt();
    

            switch (opcao) {
                case 1:
                    preco += qtd*18;
                    qtd_1+= qtd;
                    break;

                case 2 :
                    preco += qtd*35;
                    qtd_2+= qtd;
                    break;

                case 3:
                    preco += qtd*13;
                    qtd_3+= qtd;
                    break;
    
                case 4: 
                    preco += qtd*16;
                    qtd_4+= qtd;
                    break;
            
                case 5: 
                    preco += qtd*17;
                    qtd_5+= qtd;
                    break;

                case 6: 
                    preco += qtd*15;
                    qtd_6+= qtd;
                    break;

                case 7: 
                    preco += qtd*11;
                    qtd_7+= qtd;
                    break;

                case 8: 
                    preco += qtd*10;
                    qtd_8+= qtd;
                    break;

                case 9: 
                    preco += qtd*12;
                    qtd_9+= qtd;
                    break;
                default: System.out.println("Opção inválida!");
            }
        }
            System.out.println("==========================================");
            System.out.println("            RESUMO DO PEDIDO              ");
            System.out.println("==========================================");
            if(qtd_1>0)
                System.out.println(qtd_1+" Que Pastel É Este ....... R$ 18,00");
            if(qtd_2>0)
                System.out.println(qtd_2+" Ainda Há Queijo ......... R$ 35,00");
            if(qtd_3>0)
                System.out.println(qtd_3+" Faroeste com Vinagrete .. R$ 13,00");
            if(qtd_4>0)
                System.out.println(qtd_4+" Geração Coca-Cola ....... R$ 16,00");
            if(qtd_5>0)
                System.out.println(qtd_5+" Pastéis e Massinhas ..... R$ 17,00");
            if(qtd_6>0)
                System.out.println(qtd_6+" Primeiros Churros ....... R$ 15,00");
            if(qtd_7>0)
                System.out.println(qtd_7+" A Sua Banoffee .......... R$ 11,00");
            if(qtd_8>0)
                System.out.println(qtd_8+" Ganasha ................. R$ 10,00");
            if(qtd_9>0)
                System.out.println(qtd_9+" Geladeira-pência  ....... R$ 12,00");
            
            System.out.println("TOTAL: R$ "+preco+"\n");

            System.out.println("Forma de pagamento:\n");

            System.out.println("1 - Dinheiro\n2 - Cartão\n3 - PIX\n");
            
            System.out.println("Escolha: "); int esc = entrada.nextInt();
            
            System.out.println("\nPagamento realizado com sucesso!");
            
            int numero = (int)(Math.random() * 300); 
            System.out.println("Pedido Nº: " + numero+"\n");
            
            System.out.println("Aguarde a chamada do seu pedido.");
            entrada.close();
    }
}

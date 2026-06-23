public class Frete{
    public static void calcularFrete(double peso){
        if (peso<=1.0){
            System.out.println(10.0);
        }else if(peso<=5){
            System.out.println(20.0);
        }else if(peso>5){
            System.out.println(35.0);
        }
    }
    public static void main(String[] args) {
        calcularFrete(0.5);
        calcularFrete(3);
        calcularFrete(8);
    }
}
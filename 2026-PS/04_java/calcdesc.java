public class calcdesc {
   public calcdesc() {
   }

   public static double calcularDesconto(double valor, double percentual) {
      double vP = valor * (percentual / (double)100.0F);
      return valor - vP;
   }

   public static void main(String[] var0) {
      double result = calcularDesconto((double)100.0, (double)10.0);
      double result1 = calcularDesconto((double)250.0, (double)20.0);
      double result2 = calcularDesconto((double)500.0, (double)15.0);
      System.out.println(result);
      System.out.println(result1);
      System.out.println(result2);
   }
}

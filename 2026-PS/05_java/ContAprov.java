public class ContAprov {
    public static int contarAprovados(double[] notas) {
        int contador = 0;
        
        for (int i = 0; i < notas.length; i++){
            if (notas[i] >= 6.0) {
                contador++;
            }
        }
        return contador;
    }
    public static void main(String[] args){
        double[] notas = {7.0, 4.0, 9.0, 6.0};
        double[] notas1 = {2.0, 3.0, 5.0};
        double[] notas2 = {10.0, 8.0, 6.0};
        int aprovados = contarAprovados(notas);
        int aprovados1 = contarAprovados(notas1);
        int aprovados2 = contarAprovados(notas2);
        System.out.println(aprovados);
        System.out.println(aprovados1);
        System.out.println(aprovados2);
    }
}
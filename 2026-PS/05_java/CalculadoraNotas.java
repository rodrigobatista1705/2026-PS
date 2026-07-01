public class  CalculadoraNotas{
    public static double calcularMedia(double[] notas) {
        double soma = 0;
        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }
        return soma / notas.length;
    }
    public static void main(String[] args) {
        double[] notas = {7.0, 8.0, 9.0};
        double media = calcularMedia(notas);
        double[] notas1 = {6.0, 6.0, 6.0, 6.0};
        double media1 = calcularMedia(notas1);
        double[] notas2 = {5.0, 10.0,};
        double media2 = calcularMedia(notas2);
        System.out.println(media);
        System.out.println(media1);
        System.out.println(media2);
    }
}
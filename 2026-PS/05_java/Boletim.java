public class Boletim {

    // 1. Calcular média de notas
    public static double calcularMedia(double[] notas) {
        double soma = 0;
        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }
        return soma / notas.length;
    }

    // 2. Contar aprovados
    public static int contarAprovados(double[] notas) {
        int contador = 0;
        for (int i = 0; i < notas.length; i++) {
            if (notas[i] >= 6.0) {
                contador++;
            }
        }
        return contador;
    }

    // 7. Exibir boletim (usa calcularMedia e contarAprovados)
    public static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        String situacao = (media >= 6.0) ? "APROVADA" : "EM RECUPERACAO";

        System.out.println("=== BOLETIM DA TURMA ===");
        System.out.println("Média: " + media);
        System.out.println("Total de aprovados: " + aprovados);
        System.out.println("Situação final: " + situacao);
    }

    public static void main(String[] args) {

        double[] notasTurma = {7.0, 5.0, 9.0, 6.0};
        exibirBoletim(notasTurma);

        double[] notasTurma2 = {4.0, 3.0, 5.0};
        exibirBoletim(notasTurma2);
    }
}

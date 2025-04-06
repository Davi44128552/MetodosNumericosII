package MetodosNumericosII.unidade1.java;
import java.util.Scanner;

public class Main {

    public static void main(String[] args){

        // Criando scanner para entradas
        Scanner scanner = new Scanner(System.in);

        /* A interface grafica ainda esta bem ruim
         * Sendo assim, vamos dar ao usuario a opcao de testar os metodos pelo terminal
         * Ou entao usar a interface grafica
         */

        // Dando ao usuario a opcao de escolher terminal ou GUI
        int opcao = 3;

        while (opcao != 1 && opcao != 2){

            System.out.println("========== Calculadora de Derivadas ==========");
            System.out.println("Você gostaria de usar terminal ou nossa interface gráfica?");
            System.out.println("[ 1 ] Terminal \n[ 2 ] GUI");
            opcao = scanner.nextInt();

            if (opcao != 1 && opcao != 2){
                System.out.println("ERRO! Valor inválido!");
            }

        }

        if (opcao == 1){

            // Caso tenha sido escolhido o terminal
            // Declarando derivacao
            Derivacao derivada;

            boolean loop = true;
            while (loop){

                // Declarando variaveis que vao ser usadas
                int opcao2, opcao3;
                double x, deltaX;
                double resultado = -1;
                String funcao;

                System.out.println("========== TERMINAL ==========");
                System.out.println("O que você gostaria de fazer?");
                System.out.println("[ 1 ] Derivada Primeira " + 
                "\n[ 2 ] Derivada Segunda" +
                "\n[ Any ] Encerrar");

                opcao2 = scanner.nextInt();

                if (opcao2 == 1 || opcao2 == 2){

                    // Entrada do usuario
                    System.out.print("Digite x: ");
                    x = scanner.nextDouble();
                    scanner.nextLine();

                    System.out.print("Digite Delta x: ");
                    deltaX = scanner.nextDouble();
                    scanner.nextLine();

                    System.out.print("Digite a função: ");
                    funcao = scanner.nextLine();

                    // Instanciando derivacao
                    derivada = new Derivacao(x, deltaX, funcao);

                    // Escolhendo o metodo para calculo de derivada
                    System.out.println("Qual dos métodos você escolhe?");
                    System.out.println("[ 1 ] Forward \n[ 2 ] Backward \n[ 3 ] Central");
                    opcao3 = scanner.nextInt();

                    // Perguntando ao usuario qual tipo de derivada deseja calcular
                        // Derivada primeira
                    if (opcao2 == 1){
                        resultado = derivada.calcularDerivacao(0.0000000001, opcao3);
                    }

                    else if (opcao2 == 2){
                       resultado = derivada.calcularDerivacao(0.0000000001, 3 + opcao3);
                    }

                    System.out.println("Resultado: " + resultado);

                }

                else{
                    loop = false;
                }

            }

        }

        else{
            new GUI();
        }

        // Fechando o scanner
        scanner.close();

    }
    
}

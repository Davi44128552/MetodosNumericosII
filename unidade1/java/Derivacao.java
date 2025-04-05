package MetodosNumericosII.unidade1.java;

// Classe para realizar as operacoes de derivacao
public class Derivacao {

    // Definindo os atributos da classe
    private double x; 
    private double deltaX;
    private String funcao;

    // Construtor
    Derivacao(double x, double deltaX, String funcao){
        this.setX(x);
        this.setDeltaX(deltaX);
        this.setFuncao(funcao);
    }

    // Getters
    public double getX(){
        return x;
    }

    public double getDeltaX(){
        return deltaX;
    }

    public String getFuncao(){
        return funcao;
    }

    // Setters
    public void setX(double x){
        this.x = x;
    }

    public void setDeltaX(double deltaX){
        this.deltaX = deltaX;
    }

    public void setFuncao(String funcao){
        this.funcao = funcao;
    }

    // Criando os metodos para o calculo da derivada
        // Derivada primeira
    public double derivadaPrimeira(int tipo){

        // Declarando numerador e denominador
        // Deixo inicialmente null para nao dar erro de compilacao
        // Ja que um dos metodos sera escolhido, entao o numerador e o denominador sempre mudarao
        Double numerador = null;
        Double denominador = null;

        // Se for escolhido o tipo 1, entao sera calculado a derivada pelo metodo forward
        if (tipo == 1){
            numerador = ExecutarPython.converter_funcao(funcao, x + deltaX) 
            - ExecutarPython.converter_funcao(funcao, x);

            denominador = deltaX;
        }

        // Se for escolhido o tipo 2, entao sera calculado a derivada pelo metodo backward
        else if (tipo == 2){
            numerador = ExecutarPython.converter_funcao(funcao, x) 
            - ExecutarPython.converter_funcao(funcao, x - deltaX);

            denominador = deltaX;
        }

        // Se for escolhido o tipo 3, entao sera escolhido o metodo central
        else if (tipo == 3){
            numerador = ExecutarPython.converter_funcao(funcao, x + deltaX) 
            - ExecutarPython.converter_funcao(funcao, x - deltaX);

            denominador = 2 * deltaX;
        }

        // Calculando a reta secante
        double secante = numerador / denominador;
        return secante;

    }

        // Derivada segunda
    public Double derivadaSegunda(int tipo){

        // Declarando numerador e denominador
        Double numerador = null;
        Double denominador = null;

        // Se for escolhido o tipo 1, entao sera calculado a derivada pelo metodo forward
        if (tipo == 4){
            numerador = 
            ExecutarPython.converter_funcao(funcao, x + 2 * deltaX) 
            - 2 * ExecutarPython.converter_funcao(funcao, x + deltaX)
            + ExecutarPython.converter_funcao(funcao, x);

            denominador = deltaX * deltaX;
        }

        // Se for escolhido o tipo 2, entao sera calculado a derivada pelo metodo backward
        else if (tipo == 5){
            numerador = 
            ExecutarPython.converter_funcao(funcao, x)
            - 2 * ExecutarPython.converter_funcao(funcao, x - deltaX)
            + ExecutarPython.converter_funcao(funcao, x - 2 * deltaX);

            denominador = deltaX * deltaX;
        }

        // Se for escolhido o tipo 6, entao sera escolhido o metodo central
        else if (tipo == 6){
            numerador = ExecutarPython.converter_funcao(funcao, x + deltaX)
            - 2 * ExecutarPython.converter_funcao(funcao, x)
            + ExecutarPython.converter_funcao(funcao, x - deltaX);

            denominador = deltaX * deltaX;
        }

        // Calculando a reta secante
        double secante = numerador / denominador;
        return secante;

    }

    // Funcao para realizar a dedrivacao -> Aproximando o valor de deltaX para 0
    public double calcularDerivacao(double precisao, int tipo){

        // Criando as variaveis necessarias para a realizacao do calculo
        double resultadoAnterior = Float.POSITIVE_INFINITY;
        boolean loop = true;
        double secante = 0;

        // Loop para realizar diversos calculos aproximando deltaX de 0 ate chegar a uma diferenca minuscula
        while (loop){

            // Escolhendo a derivadacao
            if (tipo < 4){
                secante = derivadaPrimeira(tipo);
            }

            else{
                secante = derivadaSegunda(tipo);
            }

            // Se chegamos a um valor que seja menor que a precisao, entao chegamos a um valor favoravel
            if (Math.abs(resultadoAnterior - secante) < precisao){
                loop = false;
            }

            // Caso contrario, diminuimos deltaX
            this.setDeltaX(deltaX / 10);
            resultadoAnterior = secante;

        }

        // Quando chegamos a um resultado farovavel (proximo da derivada real) retornamos
        return secante;

    }
    
}

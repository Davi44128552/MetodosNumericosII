package MetodosNumericosII.unidade1.java;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class ExecutarPython {

    // Funcao para realizar a conversao
    public static Double converter_funcao(String funcaoString, double x){

        Double resultadoDouble = null;
        String caminhoPython = "unidade1\\java\\Converter_funcao.py";

        try{

            // Realizando a chamada da função python com os argumentos para a conversao
            ProcessBuilder pb = new ProcessBuilder(
                
                "python3",
                caminhoPython,
                funcaoString,
                String.valueOf(x)
            );

            // Realizando o processo para obter a conversao da funcao para double
            Process processo = pb.start();
            BufferedReader reader = new BufferedReader(new InputStreamReader(processo.getInputStream()));

            // Lendo o resultado imprimido pela funcao em python
            String resultado = reader.readLine();

            // Realizando a conversao do valor em string para double
            resultadoDouble = Double.parseDouble(resultado);

        }

        catch (IOException e){
            e.printStackTrace();
        }

        return resultadoDouble;
        
    }   

    
}

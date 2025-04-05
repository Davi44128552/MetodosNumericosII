package MetodosNumericosII.unidade1.java;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI extends JFrame implements ActionListener{

    // Elementos essenciais da GUI
        // ComboBox
    JComboBox<String> comboBox;

        // TextField
    JTextField campo_texto;
    JTextField campo_textoX;
    JTextField campo_textoDeltaX;

        // Label
    JLabel labelIntro;
    JLabel labelX;
    JLabel labelDeltaX;
    JLabel labelFuncao;
    JLabel labelResultado;

        // Panel
    JPanel painelIntro;
    JPanel painelCentro;
    JPanel painelBaixo;

    // Declarando um objeto para ser a funcao
    Derivacao derivada;

    GUI(){

        // Setando algumas configuracoes iniciais
        this.setTitle("Calculadora de Derivadas");
        this.setSize(500, 500);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new BorderLayout());

        // Configurando os paineis
        painelIntro = new JPanel();
        painelIntro.setLayout(new GridLayout(2, 1));

        painelCentro = new JPanel();
        painelCentro.setLayout(new GridLayout(4, 2));

        painelBaixo = new JPanel();
        painelBaixo.setLayout(new GridLayout(2, 1));

        // Criando uma combobox para selecionar o tipo de derivada
        String[] opcoes = 
        {
        "Derivada Padrão Forward",
        "Derivada Padrão Backward",
        "Derivada Padrão Central",
        "Derivada Segunda Forward",
        "Derivada Segunda Backward",
        "Derivada Segunda Central"
        };
        comboBox = new JComboBox<>(opcoes);

        // Adicionando as labels
        labelIntro = new JLabel("CALCULADORA DE DERIVADAS");
        
        labelX = new JLabel("x");

        labelDeltaX = new JLabel("Δx");

        labelFuncao = new JLabel("Função");

        labelResultado = new JLabel("");

        // Adicionando o botão de confirmar
        JButton confirmar = new JButton("Confirmar");
        confirmar.setFocusable(false);
        confirmar.addActionListener(this);

        // Adicionando o textbox para o usuario colocar a funcao
        campo_texto = new JTextField();
        campo_textoX = new JTextField();
        campo_textoDeltaX = new JTextField();

        // Adicionando os componentes aos paineis
        painelIntro.add(labelIntro);
        painelIntro.add(labelResultado);

        painelBaixo.add(comboBox);
        painelBaixo.add(confirmar);

        painelCentro.add(labelFuncao);
        painelCentro.add(campo_texto);
        painelCentro.add(labelX);
        painelCentro.add(campo_textoX);
        painelCentro.add(labelDeltaX);
        painelCentro.add(campo_textoDeltaX);

        // Mapeamento
        this.add(painelIntro, BorderLayout.NORTH);
        this.add(painelCentro, BorderLayout.CENTER);
        this.add(painelBaixo, BorderLayout.SOUTH);
        this.setVisible(true);

    }

    // Funcao do botao
    @Override
    public void actionPerformed(ActionEvent e){
        try {
            // Corrigindo: usar getText() em vez de getSelectedText()
            double xDouble = Double.parseDouble(campo_textoX.getText());
            double deltaXDouble = Double.parseDouble(campo_textoDeltaX.getText());
            double resultado = 0;

            // Instanciando o objeto derivada
            derivada = new Derivacao(xDouble, deltaXDouble, campo_texto.getText());

            if (comboBox.getSelectedItem() == "Derivada Padrão Forward"){
                resultado = derivada.calcularDerivacao(0.000001, 1);
            }
            else if (comboBox.getSelectedItem() == "Derivada Padrão Backward"){
                resultado = derivada.calcularDerivacao(0.000001, 2);
            }
            else if (comboBox.getSelectedItem() == "Derivada Padrão Central"){
                resultado = derivada.calcularDerivacao(0.000001, 3);
            }
            else if (comboBox.getSelectedItem() == "Derivada Segunda Forward"){
                resultado = derivada.calcularDerivacao(0.000001, 4);
            }
            else if (comboBox.getSelectedItem() == "Derivada Segunda Backward"){
                resultado = derivada.calcularDerivacao(0.000001, 5);
            }
            else if (comboBox.getSelectedItem() == "Derivada Segunda Central"){
                resultado = derivada.calcularDerivacao(0.000001, 6);
            }

            labelResultado.setText(String.valueOf(resultado));
        } 
        catch (NumberFormatException ex) {
            labelResultado.setText("Erro: Valores inválidos");
        }
    }
    
}

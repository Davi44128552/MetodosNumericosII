package MetodosNumericosII.unidade1.java;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI extends JFrame implements ActionListener{

    // Elementos essenciais da GUI
    JComboBox<String> comboBox;

    GUI(){

        // Setando algumas configuracoes iniciais
        this.setTitle("Calculadora de Derivadas");
        this.setSize(500, 500);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new BorderLayout());

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

        // Adicionando o botão de confirmar
        JButton confirmar = new JButton("Confirmar");
        confirmar.addActionListener(this);

        this.add(confirmar, BorderLayout.NORTH);
        this.add(comboBox, BorderLayout.SOUTH);
        this.setVisible(true);

    }

    // Funcao do botao
    @Override
    public void actionPerformed(ActionEvent e){

        if (comboBox.getSelectedItem() == "Derivada Padrão Forward"){
            
        }

        if (comboBox.getSelectedItem() == "Derivada Padrão Backward"){
            
        }

        if (comboBox.getSelectedItem() == "Derivada Padrão Central"){
            
        }

        if (comboBox.getSelectedItem() == "Derivada Segunda Forward"){
            
        }

        if (comboBox.getSelectedItem() == "Derivada Segunda Backward"){
            
        }

        if (comboBox.getSelectedItem() == "Derivada Segunda Central"){
            
        }

    }
    
}

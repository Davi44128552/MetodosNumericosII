# Importando bibliotecas
import sys

# Importando bibliotecas dos metodos
import unidade2.newton_cotes as nc

# Definindo a função main
def main(argv):
    tipo = argv[1]
    x_inicial = argv[2]
    x_final = argv[3]
    erro = argv[4]

    print(nc.integral_final(x_inicio = x_inicial, x_fim = x_final, erro = erro))

if __name__ == "__main__":
    main(sys.argv)
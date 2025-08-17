from container import Attributes
from interface import Screen

screen = Screen()
screen.mainloop()

def loadInterface():
    if not screen.selected_file:
        print("Nenhum arquivo foi selecionado.")
        return

    attrs = Attributes(screen.selected_file)
    print(f"Caminho do arquivo: {screen.selected_file}")

    while True:
        print("=" * 30)
        try:
            menu = int(input("[1] - Mostrar Arquivo CSV\n" "[2] - Listar Coluna\n" "[3] - Calcular estatísticas\n" "[4] - Filtrar\n" "[5] - Encerrar\nSua opção: "))
            print("=" * 30)
            if menu < 1 or menu > 5:
                print("Opção inválida, tente novamente")
            elif menu == 5:
                break
            else:
                if menu == 1:
                    attrs.readingCSV()
                elif menu == 2:
                    attrs.listColumn()
                elif menu == 3:
                    attrs.calc()
                elif menu == 4:
                    attrs.filter()
        except ValueError as e:
            print(f"Valor inválido, tente novamente ({e})")


def loadData():
    loadInterface()


loadData()

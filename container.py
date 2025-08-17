import pandas as pd
import numpy
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_integer_dtype
from tabulate import tabulate

class Attributes:
    def __init__(self, file_path):
        self.delimiter = input("Digite o delimitador do seu arquivo CSV: ")
        while True:
            try:
                self.result = pd.read_csv(file_path, delimiter=self.delimiter, index_col=False)
                break
            except FileNotFoundError as e:
                print(f"Arquivo não encontrado, tente novamente. ({e})")
    def readingCSV(self):
        print(tabulate(self.result, headers="keys"))

    def listColumn(self):
        while True:
            column = input("Digite o título da coluna que deseja visualizar: ")
            if column in self.result.columns:
                print(tabulate(self.result[[column]], headers=column))
                break
            else:
                print("Coluna não econtrada, tente novamente")

    def calc(self):
        while True:
            column = input("Digite o nome da coluna numérica: ")
            if column in self.result.columns:
                if is_numeric_dtype(self.result[column]):
                    print(f"A coluna {column} é numérica")
                    try:
                        after = int(input("[1] - Média, [2] - Mediana, [3] - Moda, [4] - Máximo, [5] - Mínimo, [6] - Desvio Padrão\nSua opção:"))
                        if after < 1 or after > 6:
                            print("Opção inválida tente novamente.")
                        if after == 1:
                            soma = self.result[column].sum()
                            numero_de_linhas = self.result[column].count()
                            media = soma / numero_de_linhas
                            print(f"Média da coluna {column}: {media:.2f}")
                        elif after == 2:
                            valor_central = numpy.median(self.result[column])
                            print(f"A mediana da coluna {column} é: {valor_central}")
                        elif after == 3:
                            moda = self.result[column].mode()
                            print(f"A moda da coluna {column} é: {list(moda)}")
                        elif after == 4:
                            print(f"O valor máximo da coluna {column} é: {max(self.result[column])}")
                        elif after == 5:
                            print(f"O valor mínimo da coluna {column} é: {min(self.result[column])}")
                        elif after == 6:
                            print(f"O desvio padrão é: {self.result[column].std():.2f}")
                        break
                    except ValueError as e:
                        print(f"Valor inválido, tente novamente. ({e})")
                else:
                    print("A coluna selecionada não é numérica, tente novamente.")
            else:
                print("Coluna não encontrada, tente novamente.")

    def filter(self):
        while True:
            column = input("Mostrar linhas que a coluna: ")
            if column in self.result.columns:
                try:
                    condition = int(input("[1] - Seja maior que, [2] - Seja menor que, [3] - Seja igual, [4] - Seja par, [5] - Seja ímpar\nSua opção: "))
                    if is_numeric_dtype(self.result[column]):
                        if condition < 1 or condition > 6:
                            print("Opção inválida, tente novamente.")
                        if condition == 1:
                            printData = float(input(f"Mostrar linhas que a coluna {column} seja maior que: "))
                            linhas = self.result[self.result[column] > printData]
                            self.show_lines(linhas)
                        elif condition == 2:
                            printData = float(input(f"Mostrar linhas que a coluna {column} seja menor que: "))
                            linhas = self.result[self.result[column] < printData]
                            self.show_lines(linhas)
                        elif condition == 3:
                            printData = float(input(f"Mostrar linhas que a coluna {column} seja igual a: "))
                            linhas = self.result[self.result[column] == printData]
                            self.show_lines(linhas)
                        elif condition == 4:
                            if not is_integer_dtype(self.result[column]):
                                print("Precisa ser uma coluna de valores inteiros.")
                            else:
                                linhas = self.result[self.result[column] % 2 == 0]
                                self.show_lines(linhas)
                        elif condition == 5:
                            if not is_integer_dtype(self.result[column]):
                                print("Precisa ser uma coluna de valores inteiros.")
                            else:
                                linhas = self.result[self.result[column] % 2 != 0]
                                self.show_lines(linhas)
                        break
                    else:
                        print("A coluna selecionada não é numérica, tente novamente.")
                except ValueError as e:
                    print(f"Valor inválido, tente novamente. ({e})")
            else:
                print("Coluna não encontrada, tente novamente.")

    def show_lines(self, linhas):
        print(tabulate(linhas, headers='keys', showindex=False))

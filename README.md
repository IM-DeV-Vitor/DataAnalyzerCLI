# CSV Analyzer

Programa em Python para leitura, análise e filtragem de arquivos CSV de forma interativa.  
Permite visualizar colunas, calcular estatísticas numéricas e filtrar dados conforme condições específicas.

---

## Funcionalidades

1. **Leitura de CSV**
   - Suporta arquivos CSV com diferentes delimitadores (`,` ou `;`).
   - Exibe o conteúdo completo do arquivo em formato de tabela.

2. **Visualização de colunas**
   - Permite exibir apenas uma coluna específica.

3. **Cálculo de estatísticas**
   - Média
   - Mediana
   - Moda (pode retornar mais de um valor)
   - Valor máximo
   - Valor mínimo
   - Desvio padrão

4. **Filtragem de dados**
   - Linhas com valores maiores ou menores que um número
   - Linhas com valores iguais a um número
   - Linhas com valores pares ou ímpares (somente colunas inteiras)

---

## Requisitos

- Python 3.x  
- Bibliotecas:
  - pandas
  - numpy
  - tabulate

Instale as dependências com:

``` bash
pip install pandas numpy tabulate
``` 

## Como usar

1. Execute o script no terminal.
2. Selecione o arquivo no Pop-Up que aparecer na tela (pode demorar um pequeno tempo).
3. Informe o delimitador do arquivo CSV (por exemplo, `,` ou `;`).
4. Escolha a operação desejada:
   - Visualizar o CSV completo.
   - Listar os valores de uma coluna específica.
   - Calcular estatísticas de uma coluna numérica:
     - Média
     - Mediana
     - Moda
     - Máximo
     - Mínimo
     - Desvio padrão
   - Filtrar linhas com base em condições:
     - Valores maiores que um número
     - Valores menores que um número
     - Valores iguais a um número
     - Valores pares (somente colunas inteiras)
     - Valores ímpares (somente colunas inteiras)
5. Siga as instruções no terminal para inserir números ou escolher opções.
6. Os resultados serão exibidos em formato de tabela diretamente no terminal.

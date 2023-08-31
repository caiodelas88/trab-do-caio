#Caio Hildebrand, Bruno Silveira , 
"""
Avaliação em grupo 01
Para Obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolvera irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados reterentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o codigo da operação (U para união, ' para interseção, D para diferença e c produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo das linhas que podem existir em um arquivo de testes para o programa que voce ira desenvolver:Neste exemplo temos 4 operações uma união (U), uma interseção (), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá ser execurada sobre os conjuntos (3,5,67,7) e (1,2,3,4), cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação. No caso da uniao a linha de saída deverá conter a informação e a formatação mostrada a seguir:
União: conjunto 1 (3,5, 67,7), conjunto 2 ¿1, 2, 3, 4). Resultado: (3,5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saida para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saida acima. Observe as letras maiúsculas e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saida, formatadas e pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado voce deve criar, no mínimo, três arquivos de entrada contendo um número diferente de operações, operações com dados diferentes, e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes devem estar disponiveis tanto no ambiente repl.it quanto no ambiente Github.
"""
def read_input_file(conjunto):
    with open(conjunto, 'r') as file:
        lines = file.readlines()
    
    operations = int(lines[0].strip())
    data = []

    for i in range(1, len(lines), 3):
        operation = lines[i].strip()
        set1 = set(map(int, lines[i + 1].strip().split(',')))
        set2 = set(map(int, lines[i + 2].strip().split(',')))
        data.append((operation, set1, set2))

    return operations, data

def perform_operations(operations, data):
    results = []

    for operation, set1, set2 in data:
        if operation == 'U':
            result = set1.union(set2)
            operation_name = 'União'
        elif operation == 'I':
            result = set1.intersection(set2)
            operation_name = 'Interseção'
        elif operation == 'D':
            result = set1.difference(set2)
            operation_name = 'Diferença'
        elif operation == 'C':
            result = {(x, y) for x in set1 for y in set2}
            operation_name = 'Produto Cartesiano'
        
        results.append((operation_name, set1, set2, result))

    return results

def format_and_print_results(results):
    for operation_name, set1, set2, result in results:
        formatted_set1 = ', '.join(map(str, set1))
        formatted_set2 = ', '.join(map(str, set2))
        formatted_result = ', '.join(map(str, result))
        print(f"{operation_name}: conjunto 1 ({formatted_set1}), conjunto 2 ({formatted_set2}). Resultado: ({formatted_result})")

if __name__ == "__main__":
    input_filename = "conjunto.txt"
    operations, data = read_input_file(input_filename)
    results = perform_operations(operations, data)
    format_and_print_results(results)

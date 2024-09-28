alunos = []
notas = {}
frequencias = {}

def adicionar_aluno():
    nome = str(input("Nome do aluno a ser adicionado: "))

    if len(nome) <= 3 or len(nome) > 50: # Verifica se o número de caracteres está de acordo com o necessário
        print("Número de caracteres inválido.")

    else: # Adiciona se estiver tudo de acordo
        alunos.append(nome)
        notas[nome] = [] # Através do dicionário notas, adiciona um array vazio para cada aluno novo criado
        frequencias[nome] = [] # # Através do dicionário frequencia, adiciona um array vazio para cada aluno novo criado

def editar_aluno():
    nome = input(str("Digite o nome do aluno a ser editado: "))

    if nome in alunos: # Se o nome existir em alunos, o mesmo poderá ser editado
        novo_nome = str(input("Digite um novo nome: "))
        busca = alunos.index(nome)
        alunos[busca] = novo_nome
        notas[novo_nome] = notas.pop(nome)
        print(f"Nome atualizado para {novo_nome}")

    else: # Caso contrário, o aluno não poderá ser editado
        print("O aluno não existe no sistema")

def remover_aluno():
    nome = str(input("Digite o nome do aluno a ser removido: "))

    if nome in alunos:
        alunos.remove(nome) # Podererá remover o nome do aluno de dentro da tupla
        notas.pop(nome) # Por ser um dicionário, será usado o pop para remover o aluno

    else:
        print("O aluno não existe no sistema")

def adicionar_notas():
    nome = str(input("Digite o nome do aluno que irá receber a nota: "))
    opcoes = int(input("Quantas notas deseja adicionar ao aluno? (Máximo 4): "))

    count = 1 # Limitador entre 1 e 4

    if opcoes < 0 or opcoes > 4: # O usuário não poderá escolher um valor que não esteja definido pela aplicação
        print("A quantidade de notas está errada.")

    else:
        if nome in alunos:

            while count <= opcoes:
                nota = float(input(f"Digite a {count} nota do aluno: "))
                if(nota < 0 or nota > 10): # Erro ao ter uma nota não pré definida
                    print("A nota colocada é inválida")
                else:
                    notas[nome].append(nota) # Através do dicionário notas, irá adicionar cada nota ao aluno correspondente
                    print(f"A {count} Nota: {nota} foi adicionada para {nome}")
                    count+=1

        else:
            print("O aluno não existe no sistema")

def adicionar_frequencia():
    nome = str(input("Digite o nome do aluno a ser adicionado a frequencia: "))

    if nome in alunos:
        frequencia = int(input("Digite a frequencia do aluno (em %): "))
        if 0 <= frequencia <= 100:
            frequencias[nome].append(frequencia)
            print(f"A frequência {frequencia}% foi adicionada para {nome}")
        else:
            print("Frequência inválida. Deve ser entre 0 e 100%.")
    else:
        print("O aluno não existe no sistema")


def calcular_situacao(nome, carga_horaria): 
    if nome in alunos:
        if notas[nome]:
            media_notas = sum(notas[nome]) / len(notas[nome]) 
            if frequencias[nome]:  # Verifica se há frequências registradas
                frequencia_total = sum(frequencias[nome]) / len(frequencias[nome])
                aulas_assistidas = (frequencia_total / 100) * carga_horaria
                porcentagem_freq = (aulas_assistidas / carga_horaria) * 100

                if porcentagem_freq < 75:
                    return "Reprovado por falta"
                elif media_notas >= 7:
                    return "Aprovado"
                else:
                    return "Reprovado por nota"
            else:
                return "Frequência não registrada"  # Se não há frequência registrada
    else:
        print("O aluno não existe no sistema")

def imprimir_relatorio_geral():
    print("\nRelatório Geral dos Alunos:")
    carga_horaria = int(input("Digite a carga horária da disciplina: "))
    for aluno in alunos:
        if notas[aluno]:
            media_notas = sum(notas[aluno]) / len(notas[aluno])
            frequencia_media = sum(frequencias[aluno]) / len(frequencias[aluno])
            situacao = calcular_situacao(aluno, carga_horaria)
            print(f"{aluno} - nota: {media_notas:.1f} / frequência: {frequencia_media:.1f}% aulas - ({situacao})")


def imprimir_relatorio_filtrado():
    situacao_filtro = input("Informe a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
    carga_horaria = int(input("Digite a carga horária da disciplina: "))
    
    print(f"\nRelatório de Alunos - Situação: {situacao_filtro}")
    for aluno in alunos:
        situacao = calcular_situacao(aluno, carga_horaria)
        # Assegura que estamos comparando corretamente
        if situacao == situacao_filtro:
            media_notas = sum(notas[aluno]) / len(notas[aluno]) if notas[aluno] else 0
            frequencia_media = sum(frequencias[aluno]) / len(frequencias[aluno]) if frequencias[aluno] else 0
            print(f"{aluno} - nota: {media_notas:.1f} / frequência: {frequencia_media:.1f}% aulas - ({situacao})")



def main():
    while True:
        opcoes = int(input('''
    O que deseja fazer?\n
    1 - Adicionar Aluno
    2 - Editar Aluno
    3 - Remover Aluno
    4 - Adicionar notas
    5 - Adicionar Frequência
    6 - Imprimir Relatório Geral
    7 - Imprimir Relatório Filtrado
    0 - Sair\n
    Digite o valor desejado: '''))
        
        match opcoes:
            case 1:
                adicionar_aluno()
            case 2:
                editar_aluno()
            case 3:
                remover_aluno()
            case 4:
                adicionar_notas()
            case 5:
                adicionar_frequencia()
            case 6:
                imprimir_relatorio_geral()
            case 7:
                imprimir_relatorio_filtrado()
            case 0:
                return False


main()
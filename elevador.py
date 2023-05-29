from distance import distance

graph = [
    [1], # 0
    [2, 5], # 1
    [1, 3, 6], # 2
    [2, 4, 7], # 3
    [3], # 4
    [8], # 5
    [9], # 6
    [10], # 7
    [11], # 8
    [12], # 9
    [13], # 10
    [14], # 11
    [15], # 12
    [16], # 13
    [17], # 14
    [18], # 15
    [19], # 16
    [20], # 17
    [21], # 18
    [22], # 19
    [23], # 20
    [24], # 21
    [25], # 22
    [26], # 23
    [27], # 24
    [28], # 25
    [30], # 26
    [31], # 27
    [32], # 28
    [30], # 29
    [29, 31, 26], # 30
    [30, 32, 27], # 31
    [31, 33, 28], # 32
    [32], # 33
]

vertices_legais = [0, 1, 2, 3, 4, 29, 30, 31, 32, 33]

# Cria uma matriz com 34 linhas e 40 colunas
instantes = [[None for x in range(40)] for y in range(34)]

instantes[1] = [] # Vértice 1 vai ter o elevador A (1) no instante 0
instantes[2] = [] # Vértice 2 vai ter o elevador B (2) no instante 0
instantes[3] = [] # Vértice 3 vai ter o elevador C (3) no instante 0

# Array para armazenar as movimentações de cada elevador
elevador_A = {
    "id": 1,
    "position": 1, # Armazena a posição atual
    "steps": [] # Armazenas as movimentações que serão feitas
}

elevador_B = {
    "id": 2,
    "position": 2,
    "steps": []
}

elevador_C = {
    "id": 3,
    "position": 3,
    "steps": []
}

elevadores = [
    elevador_A,
    elevador_B,
    elevador_C
]




def main():
    elevador_paths = []
    # corredor_partida = int(input("Digite o corredor de partida: "))
    # andar_partida = int(input("Digite o andar de partida: "))
    # andar_destino = int(input("Digite o andar de destino: "))
   
    vertice_partida_A = 2 # TODO: Usar o corredor e andar de partida para achar o vértice e decidir qual elevador será usado
    vertice_destino_A = 12 # TODO: Usar o corredor de partida e andar de destino para achar o vértice

    vertice_partida_B = 3
    vertice_destino_B = 32

    # Move o elevador para o vértice de partida
    elevador_steps = [elevador_A["steps"][-1]] if len(elevador_A["steps"]) > 0 else [elevador_A["position"]]
    acha_caminho(elevador_A, vertice_partida_A, elevador_steps, elevador_paths)
    elevador_A["steps"] =  min(elevador_paths, key=len).copy()
    elevador_paths = []


    # Move o elevador para o vértice de destino
    elevador_steps = [elevador_A["steps"][-1]] if len(elevador_A["steps"]) > 0 else [elevador_A["position"]]
    acha_caminho(elevador_A, vertice_destino_A, elevador_steps, elevador_paths)
    # Pega o menor caminho do array de caminhos (array de menor tamanho) e coloca no array de movimentações do elevador
    elevador_A["steps"] =  min(elevador_paths, key=len).copy()
    elevador_paths = []

    # print("Elevador A: ", elevador_A)
    # print("Caminhos possíveis do elevador A: ", elevador_paths)

    # Move o elevador para o vértice de partida
    elevador_steps = [elevador_B["steps"][-1]] if len(elevador_B["steps"]) > 0 else [elevador_B["position"]]
    acha_caminho(elevador_B, vertice_partida_B, elevador_steps, elevador_paths)
    elevador_B["steps"] =  min(elevador_paths, key=len).copy()
    elevador_paths = []

    # Move o elevador para o vértice de destino
    elevador_steps = [elevador_B["steps"][-1]] if len(elevador_B["steps"]) > 0 else [elevador_B["position"]]
    acha_caminho(elevador_B, vertice_destino_B, elevador_steps, elevador_paths)
    elevador_B["steps"] =  min(elevador_paths, key=len).copy()
    elevador_paths = []


    print("Elevador A: ", elevador_A)
    print("Elevador B: ", elevador_B)

    for i in range(max(len(elevador_A["steps"]), len(elevador_B["steps"]))):
        # print("Elevador A:", elevador_A["position"])
        # print("Elevador B:", elevador_B["position"])
        move_elevadores()
    
    print("Elevador A:", elevador_A["position"])
    print("Elevador B:", elevador_B["position"])


def move_elevadores():
    
    for elevador in elevadores:
        # Move apenas uma posição por instante
        if len(elevador["steps"]) > 0:
            destino = elevador["steps"][0]
            elevador["position"] = destino
            elevador["steps"].pop(0)
            instantes[destino].pop(0)


def acha_caminho(elevador, destino, elevador_steps, elevador_paths):
    # Se o elevador já está no destino (ultima posição do steps), para a recursão e adiciona o caminho
    atual = elevador_steps[-1]
    # print("Atual: ", atual, graph[atual], len(elevador_steps) - 1)
    if atual == destino:
        # Adiciona uma cópia do array de movimentações do elevador
        elevador_paths.append(elevador_steps.copy())
        # print('ACHEI CARALHO', elevador_steps)
        return
    
    for position in graph[atual]: # Pego as posições que o elevador pode ir
        # print("Position: ", position)
        current_step = len(elevador_steps) # Pego o índice do próximo instante
        if position not in elevador_steps: # Se a posição não está no array de movimentações do elevador
            # if instantes[position][current_step] == None: # Se a posição não está sendo usada no instante atual
            #     instantes[position][current_step] = elevador["id"] # Adiciona o elevador na posição do instante atual
            #     elevador_steps.append(position) # Adiciona a posição no array de movimentações do elevador
            #     acha_caminho(position, destino, elevador_steps, elevador_paths) # Chama a função recursivamente

            #     # Desfaz a movimentação do elevador
            #     instantes[position][current_step] = None
            #     elevador_steps.pop()
            #     continue
            
            # N seria a distancia do elevador até um ponto de guarda (a cada 10 andares)
            # Se a posição não está sendo usada nos próximos N instantes, eu movimento o elevador
            N = 0
            vertex = None
            if atual not in vertices_legais:
                distances = [distance(graph, position, vertices_legais[i]) for i in range(len(vertices_legais))]
                N = min(distances)
                # Get the index of the minimum distance
                index = distances.index(N)
                # Get the vertex of the minimum distance
                vertex = vertices_legais[index]
            
            # Pega a primeira posição do arrray de instante[current_step:current_step + N] que aparece um valor diferente de None
            
            try:
                index_of_first_not_none = instantes[position][current_step:current_step + N].index(next(filter(None, instantes[position][current_step:current_step + N]), None))
            except Exception as e:
                index_of_first_not_none = None
            if  index_of_first_not_none == None:
                # Ninguem irá usar, mas será que tem alguem usando?
                # Se tem alguem usando, eu movimento ele para a posição de guarda mais próxima
                for elevador in elevadores:
                    if len(elevador["steps"]) == 0:
                        if elevador["position"] == position:
                            # Se o elevador está parado na posição, eu movimento ele para a posição de guarda mais próxima
                            acha_caminho(elevador, vertex, elevador_steps, elevador_paths)
                            continue
                        
                # Se não tem ninguem usando, eu movimento o elevador
                instantes[position][current_step] = elevador["id"]
                elevador_steps.append(position)

                acha_caminho(position, destino, elevador_steps, elevador_paths)

                instantes[position][current_step] = None
                elevador_steps.pop()

                continue

            # elif instantes[position][current_step] == None and instantes[position][current_step + N] == None:
            #     instantes[position][current_step] = elevador
            #     elevador_steps.append(position)
            #     move_elevador(position, destino, elevador_steps)
            else:
                """
                Se a posição está sendo utilizada ou será utilizada nos próximos N instantes
                Verifico se os elevadores que estão no caminho estão se movendo para uma posição de guarda
                Se sim, eu espero o elevador chegar na posição de guarda e depois eu me movimento
                Se não, eu me movimento para a posição de guarda mais próxima
                No caso do elevador no caminho estar parado, eu movimento o elevador para a posição de guarda mais próxima
                """
                [None, None, None, 1 ]
                # Aguardo
            
                instantes[position][current_step] = elevador["id"]
                elevador_steps.append(position)
                acha_caminho(position, destino, elevador_steps, elevador_paths)

                instantes[atual][current_step] = None
                elevador_steps.pop()

                # Move para a posição de guarda mais próxima
                if vertex != None:
                    acha_caminho(elevador, vertex, elevador_steps, elevador_paths)
    
                

    # Se o elevador não pode ir para nenhuma posição, remove a última posição do array de movimentações

    return

main()
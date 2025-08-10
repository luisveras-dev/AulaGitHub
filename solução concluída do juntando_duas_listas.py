def juntar_duas_listas(lista1, lista2):
    """
    Função que recebe duas listas e retorna uma terceira lista
    que seja a concatenação das duas.
    """
    lista_concatenada = []
    
    # Adiciona todos os elementos da primeira lista
    for elemento in lista1:
        lista_concatenada.append(elemento)
    
    # Adiciona todos os elementos da segunda lista
    for elemento in lista2:
        lista_concatenada.append(elemento)
    
    return lista_concatenada

# Teste da função
if __name__ == "__main__":
    natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
    tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]
    
    resultado = juntar_duas_listas(natureza, tecnologia)
    print(f"Lista de natureza: {natureza}")
    print(f"Lista de tecnologia: {tecnologia}")
    print(f"Listas concatenadas: {resultado}")
   
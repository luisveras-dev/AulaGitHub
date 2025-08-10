def extrair_nomes_objetos(lista_objetos):
    """
    Função que recebe uma lista de objetos (onde cada objeto tem um atributo 'nome')
    e retorna uma nova lista contendo apenas os nomes de cada objeto.
    """
    nomes = []
    for objeto in lista_objetos:
        if hasattr(objeto, 'nome'):
            nomes.append(objeto.nome)
        elif isinstance(objeto, dict) and 'nome' in objeto:
            nomes.append(objeto['nome'])
    
    return nomes

# Classe exemplo para teste
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

# Teste da função
if __name__ == "__main__":
    # Teste com objetos
    pessoas = [
        Pessoa("Ana"),
        Pessoa("Bruno"),
        Pessoa("Carlos"),
        Pessoa("Diana")
    ]
    
    # Teste com dicionários
    pessoas_dict = [
        {"nome": "Eduardo"},
        {"nome": "Fernanda"},
        {"nome": "Gabriel"}
    ]
    
    resultado_objetos = extrair_nomes_objetos(pessoas)
    resultado_dicts = extrair_nomes_objetos(pessoas_dict)
    
    print(f"Nomes extraídos de objetos: {resultado_objetos}")
    print(f"Nomes extraídos de dicionários: {resultado_dicts}")
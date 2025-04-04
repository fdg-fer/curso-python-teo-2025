

def juros_compostos(aporte: int, taxa: float, anos: int) -> float:
    
    """Calcula o montante com base em juros compostos.
    
    Parâmetros:
    aporte inteiro: valor inicial aplicado
    taxa : taxa de juros (ex: 0.05 para 5%)
    anos inteiro: número de anos
    Retorna:
    float: valor final após aplicação dos juros compostos
    
    """
    return aporte * (1 + taxa) ** anos


juros_compostos(taxa=0.013, anos=5, aporte=1000)
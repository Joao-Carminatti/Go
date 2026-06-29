"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME_PER_LAYER = 2

def preparation_time_in_minutes(number_of_layers):

    """Calcula o tempo total gasto na preparação das camadas da lasanha.

    :param number_of_layers: int - A quantidade de camadas que a lasanha terá.
    :return: int - Tempo total gasto na preparação (em minutos).

    Esta função multiplica a quantidade de camadas pelo tempo padrão 
    gasto para preparar cada uma delas.
    """
    
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def bake_time_remaining(elapsed_bake_time):

    """Calcula o tempo restante que a lasanha deve ficar no forno.

    :param elapsed_bake_time: int - O tempo que a lasanha já passou no forno.
    :return: int - Minutos restantes para o cozimento completo.

    Esta função pega o tempo total esperado de cozimento e subtrai o tempo 
    que a lasanha já passou no forno, retornando os minutos que faltam.
    """
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calcula o tempo total total decorrido (preparo + cozimento) até agora.

    :param number_of_layers: int - A quantidade de camadas da lasanha.
    :param elapsed_bake_time: int - Os minutos que a lasanha já está no forno.
    :return: int - O total de minutos gastos no processo até o momento.

    Esta função soma o resultado do tempo de preparo das camadas com 
    o tempo de cozimento atual que já se passou no forno.
    """
    
    tempo_preparo = preparation_time_in_minutes(number_of_layers)

    tempo_forno = elapsed_bake_time

    return tempo_preparo + tempo_forno

    
    
    



from typing import List

billete_5 = 5
billete_10 = 10
billete_20 = 20
billete_50 = 50
billete_100 = 100
billete_200 = 200
billete_500 = 500

platos = {}

def init_platos() -> None:
    """
    Inicializa los platos

    returns None
    """
    for index in range(0,10):
        platos[str(index)] = (index + 1) * 10

def display_platos() -> None:
    """
    Muestra todos los platos en pantalla

    returns None
    """
    [ print(f'{nombre}: {precio} euros') for nombre, precio in platos.items() ]

def calc_total(platos_seleccionados: List[str]) -> float:
    """
    Calcula el total de los platos seleccionados

    platos_seleccionados : List[str]
        Todos los platos seleccionados

    returns float
    """
    total = 0

    for plato in platos_seleccionados:
        if not plato in platos:
            print(f'No existe el producto "{plato}".')
            continue

        total += platos[plato]

    return total

def main() -> None:
    """
    El flujo principal de ejecución del script

    returns None
    """
    init_platos()

    cliente_platos = []

    while True:
        # Muestra por pantalla todos los platos
        display_platos()

        # Pregunta que plato quiere, tiene que existir
        while True:
            plato_seleccionado = input('¿Qué plato desea? ').strip()

            if plato_seleccionado in platos:
                cliente_platos.append(plato_seleccionado)
                break

            print('El plato solicitado no existe, vuelva a intentarlo por favor')

        # Pregunta si quiere seguir pidiendo
        continue_order = input('¿Quiere seguir pidiendo? (1:Si / 0:No) ')

        # Si ha marcado algo que no sea un 1, se paraliza la ejecución
        if not continue_order.strip() == '1': break

    total = calc_total(cliente_platos)
    print(f'Su pedido costará un total de {total} euros.')

if __name__ == "__main__":
    main()
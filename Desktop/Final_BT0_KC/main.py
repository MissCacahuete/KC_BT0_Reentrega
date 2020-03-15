from datetime import datetime as dt
from repository.cryptos_repository import is_cyptos_populated, insert_cryptos
from repository.movements_repository import insert_movement
from domain.movement import Movement
from tkinter_façade.main import Tkinter
from repository.base_repository import init_database
from api import convert_coins, get_coins


def convert_currency(quantity, from_currency, to_currency):
    if from_currency != to_currency:
        conversion = convert_coins(quantity, from_currency, to_currency)
        now = dt.now()
        movement = Movement(None, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), from_currency, quantity,
                            to_currency, conversion.calculate_amount())
        insert_movement(movement)
        return True
    else:
        return False  


def main():
    init_database()
    if is_cyptos_populated():
        cryptonedas = get_coins()
        insert_cryptos(cryptonedas)
    app = Tkinter()
    app.start()


if __name__ == "__main__":
    main()

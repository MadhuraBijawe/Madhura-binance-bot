import sys
from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validator import Validator
from config import Config
from bot.logger import setup_logger

logger = setup_logger("Main")

def print_menu():
    print("\n--- Simplified Binance Futures Testnet Bot ---")
    print("1. Place Market Order")
    print("2. Place Limit Order")
    print("3. Place Stop-Limit Order")
    print("4. Exit")
    print("----------------------------------------------")

def get_common_inputs():
    try:
        symbol = Validator.validate_symbol(input("Enter Symbol (e.g., BTCUSDT): ").strip())
        side = Validator.validate_side(input("Enter Side (BUY/SELL): ").strip())
        quantity = Validator.validate_quantity(input("Enter Quantity: ").strip())
        return symbol, side, quantity
    except ValueError as e:
        logger.warning(f"Input Validation Error: {e}")
        return None, None, None

def main():
    # 1. Validate Config
    try:
        Config.validate()
    except ValueError as e:
        logger.critical(str(e))
        print(f"\nCRITICAL ERROR: {e}")
        print("Please check your .env file and ensure valid API keys are provided.")
        sys.exit(1)

    # 2. Connect to Client
    try:
        client_wrapper = BinanceTestnetClient(Config.API_KEY, Config.API_SECRET, Config.TESTNET_BASE_URL)
        client = client_wrapper.connect()
        order_manager = OrderManager(client)
    except Exception as e:
        logger.critical(f"Failed to initialize bot: {e}")
        sys.exit(1)

    # 3. Main Loop
    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == '1':
            symbol, side, quantity = get_common_inputs()
            if symbol:
                order_manager.place_market_order(symbol, side, quantity)

        elif choice == '2':
            symbol, side, quantity = get_common_inputs()
            if symbol:
                try:
                    price = Validator.validate_price(input("Enter Limit Price: ").strip())
                    order_manager.place_limit_order(symbol, side, quantity, price)
                except ValueError as e:
                    logger.warning(f"Input Validation Error: {e}")

        elif choice == '3':
            symbol, side, quantity = get_common_inputs()
            if symbol:
                try:
                    price = Validator.validate_price(input("Enter Limit Price: ").strip())
                    stop_price = Validator.validate_price(input("Enter Stop Price: ").strip())
                    order_manager.place_stop_limit_order(symbol, side, quantity, price, stop_price)
                except ValueError as e:
                    logger.warning(f"Input Validation Error: {e}")

        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

class Validator:
    """
    Validates user inputs for trading commands.
    """
    
    @staticmethod
    def validate_symbol(symbol):
        """
        Validates the trading pair symbol (e.g., BTCUSDT).
        """
        if not symbol or not isinstance(symbol, str):
            raise ValueError("Symbol must be a non-empty string.")
        if not symbol.endswith("USDT"):
            raise ValueError("Only USDT pairs are supported (e.g., BTCUSDT).")
        return symbol.upper()

    @staticmethod
    def validate_side(side):
        """
        Validates the order side (BUY or SELL).
        """
        side = side.upper()
        if side not in ['BUY', 'SELL']:
            raise ValueError("Side must be 'BUY' or 'SELL'.")
        return side

    @staticmethod
    def validate_quantity(quantity):
        """
        Validates the order quantity.
        """
        try:
            qty = float(quantity)
            if qty <= 0:
                raise ValueError("Quantity must be greater than 0.")
            return qty
        except ValueError:
            raise ValueError("Quantity must be a valid number.")

    @staticmethod
    def validate_price(price):
        """
        Validates the order price.
        """
        try:
            p = float(price)
            if p <= 0:
                raise ValueError("Price must be greater than 0.")
            return p
        except ValueError:
            raise ValueError("Price must be a valid number.")

    @staticmethod
    def validate_order_type(order_type):
        """
        Validates the order type.
        """
        order_type = order_type.upper()
        if order_type not in ['MARKET', 'LIMIT', 'STOP_LIMIT']:
            raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT.")
        return order_type

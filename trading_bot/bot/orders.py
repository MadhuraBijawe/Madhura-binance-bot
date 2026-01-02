from binance.enums import *
from binance.exceptions import BinanceAPIException
from bot.logger import setup_logger

logger = setup_logger("OrderManager")

class OrderManager:
    """
    Handles placing orders on Binance Futures.
    """
    
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        """
        Places a MARKET order.
        """
        try:
            logger.info(f"Placing MARKET {side} order for {quantity} {symbol}...")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logger.info(f"Market Order Placed: ID={order['orderId']}, Status={order['status']}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Market Order): {e}")
            return None
        except Exception as e:
            logger.error(f"Error placing Market Order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        """
        Places a LIMIT order (GTC).
        """
        try:
            logger.info(f"Placing LIMIT {side} order for {quantity} {symbol} at {price}...")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit Order Placed: ID={order['orderId']}, Status={order['status']}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Limit Order): {e}")
            return None
        except Exception as e:
            logger.error(f"Error placing Limit Order: {e}")
            return None

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """
        Places a STOP_LIMIT order.
        """
        try:
            logger.info(f"Placing STOP-LIMIT {side} order for {quantity} {symbol} at {price}, Stop at {stop_price}...")
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_STOP, # 'STOP' implies Stop Limit usually in Futures, check API docs if STOP_MARKET needed
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logger.info(f"Stop-Limit Order Placed: ID={order['orderId']}, Status={order['status']}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Stop-Limit Order): {e}")
            return None
        except Exception as e:
            logger.error(f"Error placing Stop-Limit Order: {e}")
            return None

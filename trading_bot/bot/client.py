from binance.client import Client
from binance.exceptions import BinanceAPIException
from bot.logger import setup_logger

logger = setup_logger("BinanceClient")

class BinanceTestnetClient:
    """
    Wrapper around python-binance CLI for Testnet usage.
    """
    
    def __init__(self, api_key, api_secret, testnet_url):
        """
        Initialize the Binance Client with Testnet configuration.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.testnet_url = testnet_url
        self.client = None
        
    def connect(self):
        """
        Establishes connection to Binance Futures Testnet.
        """
        logger.info("Connecting to Binance Futures Testnet...")
        try:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            # Override to ensure we are strictly on testnet futures
            self.client.FUTURES_URL = self.testnet_url
            
            # Simple ping to verify connection
            self.client.futures_ping()
            logger.info("Successfully connected to Binance Futures Testnet.")
            return self.client
        except BinanceAPIException as e:
            logger.error(f"Failed to connect to Binance: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred during connection: {e}")
            raise

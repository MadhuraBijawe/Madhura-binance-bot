import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Configuration class to hold application settings.
    """
    API_KEY = os.getenv('BINANCE_TESTNET_API_KEY')
    API_SECRET = os.getenv('BINANCE_TESTNET_API_SECRET')
    
    # Binance Futures Testnet Base URL
    TESTNET_BASE_URL = 'https://testnet.binancefuture.com'

    @staticmethod
    def validate():
        """
        Validates that necessary configuration is present.
        """
        if not Config.API_KEY or Config.API_KEY == 'your_testnet_api_key_here':
            raise ValueError("Missing or invalid BINANCE_TESTNET_API_KEY in .env file.")
        if not Config.API_SECRET or Config.API_SECRET == 'your_testnet_api_secret_here':
            raise ValueError("Missing or invalid BINANCE_TESTNET_API_SECRET in .env file.")
        return True

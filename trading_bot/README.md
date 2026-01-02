# Simplified Trading Bot (Binance Futures Testnet)

## Overview
A production-ready CLI trading bot for Binance USDT-M Futures Testnet. It allows users to place Market, Limit, and Stop-Limit orders safely using the `python-binance` library.

## Tech Stack
- **Language**: Python 3.8+
- **Library**: `python-binance`
- **Config**: `python-dotenv` for environment management
- **Logging**: Standard `logging` module (File + Console)

## Project Structure
```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance client connection logic
│   ├── orders.py          # Order placement logic
│   ├── validator.py       # Input validation
│   └── logger.py          # Centralized logging
│
├── logs/
│   └── bot.log            # Execution logs
│
├── config.py              # Environment configuration
├── main.py                # CLI Entry point
├── requirements.txt       # Dependencies
└── .env.example           # API Key template
```

## Setup Instructions

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure API Keys**:
    - Rename `.env.example` to `.env`:
      ```bash
      # On Windows PowerShell
      cp .env.example .env
      ```
    - Open `.env` and paste your Testnet API Key and Secret from [Binance Futures Testnet](https://testnet.binancefuture.com/en/futures/BTCUSDT).

## How to Run
Run the main script from the `trading_bot` directory:
```bash
python main.py
```

## Sample Interaction
```text
--- Simplified Binance Futures Testnet Bot ---
1. Place Market Order
2. Place Limit Order
3. Place Stop-Limit Order
4. Exit
----------------------------------------------
Select an option: 1
Enter Symbol (e.g., BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Quantity: 0.001
2023-10-27 10:00:00 - OrderManager - INFO - Placing MARKET BUY order for 0.001 BTCUSDT...
2023-10-27 10:00:01 - OrderManager - INFO - Market Order Placed: ID=12345678, Status=NEW
```


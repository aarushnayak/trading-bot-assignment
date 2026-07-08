##Ths is import argparse..
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT)")

    args = parser.parse_args()

    setup_logging()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ Order Request Summary")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price: {args.price}")

        print("\n📌 Order Response Details")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Quantity: {order.get('executedQty')}")

        print("\n🎉 Order placed successfully!")

    except Exception as e:
        print("\n❌ Error:", str(e))

if __name__ == "__main__":
    main()

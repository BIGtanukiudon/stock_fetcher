import yfinance as yf

from src.models import StockPrices


def download_stock_prices(
    ticker: str, start_date: str, end_date: str, interval: str = "1h"
) -> list[StockPrices]:
    """株価データをダウンロードする

    Args:
        ticker (str): ティッカー
        start_date (str): 開始日時
        end_date (str): 終了日時
        interval (str, optional): 取得間隔. Defaults to "1h".

    Returns:
        list[StockPrices]: StockPricesのリスト
    """
    stock_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    # stock_dataはdatetime,Open,High,Low,Close,Adj Close,Volumeのカラムを持つ
    stock_prices: list[StockPrices] = []
    for index, row in stock_data.iterrows():
        stock_prices.append(
            StockPrices(
                opening_price=row["Open"],
                high_price=row["High"],
                low_price=row["Low"],
                close_price=row["Close"],
                adjust_close_price=row["Adj Close"],
                datetime=index.strftime("%Y-%m-%d %H:%M:%S"),
            )
        )

    return stock_prices

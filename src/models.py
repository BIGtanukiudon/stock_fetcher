from dataclasses import dataclass


@dataclass
class StockPrices:
    opening_price: float | None
    high_price: float | None
    low_price: float | None
    close_price: float | None
    adjust_close_price: float | None
    datetime: str

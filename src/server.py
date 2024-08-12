from concurrent import futures

import stock.v1.stock_pb2 as stock_pb2
import stock.v1.stock_pb2_grpc as stock_pb2_grpc
from grpc import server as grpc_server

from src.logger import logger
from src.stock_fetcher import download_stock_prices


class StockService(stock_pb2_grpc.StockServiceServicer):
    def GetStockPrices(
        self, request: stock_pb2.GetStockPricesRequest, context
    ) -> stock_pb2.GetStockPricesResponse:
        stock_prices = download_stock_prices(
            ticker=request.ticker,
            start_date=request.start_date,
            end_date=request.end_date,
        )

        res: list[stock_pb2.StockPrice] = []
        for stock_price in stock_prices:
            res.append(
                stock_pb2.StockPrice(
                    opening_price=stock_price.opening_price,
                    high_price=stock_price.high_price,
                    low_price=stock_price.low_price,
                    close_price=stock_price.close_price,
                    adjust_close_price=stock_price.adjust_close_price,
                    datetime=stock_price.datetime,
                )
            )

        return stock_pb2.GetStockPricesResponse(stock_prices=res)


def main():
    port = 50051
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))

    stock_pb2_grpc.add_StockServiceServicer_to_server(StockService(), server)

    server.add_insecure_port(f"localhost:{port}")

    server.start()
    logger.info(f"server started..., listening on {port}")

    server.wait_for_termination()


if __name__ == "__main__":
    main()

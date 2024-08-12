import datetime
import logging
from os import mkdir, path

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format = "%(asctime)s %(name)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s"

st_handler = logging.StreamHandler()
st_handler.setFormatter(logging.Formatter(format))

# Format the date and time as a string
datetime_string = datetime.datetime.now().strftime("%Y-%m-%d")

# Create the file handler with the log file name
file_name = path.join("logs", f"log_{datetime_string}.log")

# logDirectoryが存在しない場合は作成する
if not path.exists("logs"):
    mkdir("logs")

fl_handler = logging.FileHandler(file_name, encoding="utf-8")

# Create a formatter and add it to the handler
formatter = logging.Formatter(format)
fl_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(st_handler)
logger.addHandler(fl_handler)

import datetime
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format = "%(levelname)-9s  %(asctime)s [%(filename)s:%(lineno)d] %(message)s"

st_handler = logging.StreamHandler()
st_handler.setFormatter(logging.Formatter(format))

# Format the date and time as a string
datetime_string = datetime.datetime.now().strftime("%Y-%m-%d")

# Create the file handler with the log file name
fl_handler = logging.FileHandler(f"log_{datetime_string}.txt", encoding="utf-8")

# Create a formatter and add it to the handler
formatter = logging.Formatter(format)
fl_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(st_handler)
logger.addHandler(fl_handler)

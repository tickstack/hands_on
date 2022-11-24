from loguru import logger
if __name__ == '__main__':
    logger.add("../logs/log_{time:YYYY-MM-DD-HH-mm}.log", format="<black>{time:YYYY-MM-DD-HH-mm} </black> :{message}")
    logger.info('Its cool to use this lib, right!!!!')
    logger.info('Information')
    logger.debug("Its debugging message")
    logger.success("Completed")
    logger.warning("Its warning for you")


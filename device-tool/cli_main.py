import argparse
from device_tester import test_device
from logger_config import setUpLogger

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Smart Diagnostics CLI Tool")
    parser.add_argument("ip_or_hostname",type=str,help="IP address or hostname of the device to test")

    args=parser.parse_args()
    logger=setUpLogger("cli_tool")
    logger.info("Starting device test...")
    try:
        results=test_device(args.ip_or_hostname)
        logger.info(f"Test results for {args.ip_or_hostname}: {results}")
    except Exception as e:
        logger.error(f"An error occurred during device testing: {e}")
        raise e
    logger.info("Device test completed.")



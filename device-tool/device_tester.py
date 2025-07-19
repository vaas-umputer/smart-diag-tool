from net_communicator import get_ip_from_user, port_check, ping_device
from logger_config import setUpLogger

# Define common ports to check for devices
COMMON_PORTS = [22, 80, 443, 8080]  # SSH, HTTP, HTTPS, alternative HTTP

logger = setUpLogger("device_tester")

def test_device(ip_or_hostname):
    results = {}

    ip_address = get_ip_from_user(logger)

    # 1️⃣ Perform ping once
    result_ping = ping_device(ip_address, logger)
    results["ping"] = "Success" if result_ping else "Failed"

    if not result_ping:
        logger.error(f"Device {ip_address} is not reachable. Skipping port checks.")
        return results  # Only ping result will be returned

    # 2️⃣ If ping successful, perform port checks
    for port in COMMON_PORTS:
        try:
            logger.info(f"Testing port {port} on {ip_address}...")
            result = port_check(ip_address, port, logger)
            results[port] = "Open" if result else "Closed"
        except Exception as e:
            logger.error(f"Error testing port {port}: {e}")
            results[port] = "Error"

    return results

"""if __name__ == "__main__":
    try:
        ip_or_hostname = input("Enter the IP address or hostname of the device to test: ").strip()
        if not ip_or_hostname:
            raise ValueError("IP address or hostname cannot be empty.")
        
        results = test_device(ip_or_hostname)
        logger.info(f"Test results for {ip_or_hostname}: {results}")
    except Exception as e:
        logger.error(f"An error occurred during device testing: {e}")"""

import subprocess
import platform
import socket
def ping_device(ip_address,logger):
    logger.info(f"Pinging {ip_address}...")
    command=["ping","-n","4",ip_address] if platform.system().lower() == "windows" else ["ping","-c","1",ip_address]
    try:
        output=subprocess.check_output(command,text=True,stderr=subprocess.STDOUT)
        logger.info(f"Ping to {ip_address} successful.\n{output}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Ping to {ip_address} failed.\n{e.output}")
        return False

def get_ip_from_user(logger):
    ip_address = input("Enter the IP address or host name to ping: ").strip()
    if not ip_address:
        logger.error("No IP address provided.")
        raise ValueError("IP address cannot be empty.")
    try:
        ip_address=socket.gethostbyname(ip_address)
    except socket.error:
        logger.error("Invalid IP address or host name.")
        raise ValueError("Invalid IP address or host name.")
    logger.info(f"User provided IP address: {ip_address}")
    return ip_address

def port_check(ip_address, port, logger):
    logger.info(f"checking port {port} on {ip_address}...")
    try:
        with socket.create_connection((ip_address,port),timeout=5) as sock:
            logger.info(f"Port {port} on {ip_address} is open.")
            return True
    except (socket.timeout, ConnectionRefusedError, OSError) as e:
        logger.error(f"Port {port} on {ip_address} is closed or unreachable. Reason: {e}")
        return False
    
"""if __name__ == "__main__":
    from logger_config import setUpLogger

    logger = setUpLogger("network")
    #ip = get_ip_from_user(logger)
    #ping_device(ip, logger)
    port_check("8.8.8.8", 53, logger)  # Example port check"""


from pyModbusTCP.server import ModbusServer, DataBank
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create and start Modbus server
server = ModbusServer('0.0.0.0', port=502, no_block=True)

logging.debug("Starting Modbus server on port 502...")

try:
    server.start()
    logging.debug("Modbus server started successfully.")
    
    while True:
        try:
            # Simulate data change every second
            DataBank.set_words(0, [100])  # Update holding register 0 to 100
            DataBank.set_words(1, [200])  # Update holding register 1 to 200
            time.sleep(1)
        except Exception as e:
            logging.error(f"Error while updating Modbus registers: {e}")
except Exception as e:
    logging.error(f"Error while running Modbus server: {e}")
finally:
    server.stop()
    logging.debug("Modbus server stopped.")

import re
import serial

# ESP-IDF default baud rate is 115200
ser = serial.Serial('/dev/cu.usbserial-0001', 115200, timeout=1)
# ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1)

ANSI_ESCAPE = re.compile(r'\x1b\[[0-9;]*m')

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8', errors='replace').strip()
            line = ANSI_ESCAPE.sub('', line)
            print(line)
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()

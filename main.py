# ponytail: inlined port selector, literal baud rate — single-use script
import re, serial, serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
if not ports:
    raise SystemExit("No serial ports found.")
for i, p in enumerate(ports):
    print(f"  [{i}] {p.device} — {p.description}")
while True:
    try:
        idx = int(input(f"\nSelect port [0-{len(ports)-1}]: "))
        if 0 <= idx < len(ports): break
    except (ValueError, EOFError): pass
print()

ser = serial.Serial(ports[idx].device, 115200, timeout=1)
ANSI = re.compile(r'\x1b\[[0-9;]*m')
try:
    while True:
        if ser.in_waiting:
            print(ANSI.sub('', ser.readline().decode('utf-8', errors='replace').strip()))
except KeyboardInterrupt:
    print("\nStopped.")
finally:
    ser.close()

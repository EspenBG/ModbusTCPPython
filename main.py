# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pyModbusTCP.client import ModbusClient


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    # TCP auto connect on first modbus request
    c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)

    regs = c.read_holding_registers(0, 2)
    if regs:
        print(regs)
    else:
        print("read error")

    if c.write_multiple_registers(10, [44, 55]):
        print("write ok")
    else:
        print("write error")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

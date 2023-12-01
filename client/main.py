import sys
import serial
import time


ser = serial.Serial('/dev/tty.usbmodem103', 115200)  # adjust as necessary


def send_serial(query):
    # split query into list of characters
    query_list = list(query)
    for i in range(len(query_list)):
        # Write to the serial port

        # encode query_list[i] to bytes
        ser.write(query_list[i].encode('utf-8'))
        #ser.write(query_list[i])
        time.sleep(0.01)
    ser.write(b'\n')


def main(argv):

    # Open serial port
    query = argv[0]

    send_serial(query)

    try:
        send_serial(query)

        # Read from the serial port
        if ser.in_waiting > 0:
            data = ser.readline()
            print(data.decode('utf-8'))

    finally:
        # Close the serial port
        ser.close()


if __name__ == "__main__":
   main(sys.argv[1:])

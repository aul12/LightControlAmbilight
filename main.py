import pyscreenshot as ImageGrab
import RadioControlProtocolPy.rc_lib as rc_lib
import socket

def get_color():
    im = ImageGrab.grab(bbox=(325, 159, 325 + 1285, 159 + 882))  # X1,Y1,X2,Y2

    color = im.resize((1,1)).getpixel((0,0))

    return color

def get_package(color):
    pkg = rc_lib.Package(1024, 4)
    pkg.setChannel(0, 0)
    pkg.setChannel(1, color[0] * 4)
    pkg.setChannel(2, color[1] * 4)
    pkg.setChannel(3, color[2] * 4)

    return bytearray(pkg.encode())

def send_package(data, ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port)) 
    sock.send(data)
    sock.close()


def main():
    last_color = (0, 0, 0)
    alpha = 0.5

    while True:
        color = get_color()

        print(color)

        filtered_color = (int(color[0] * alpha + last_color[0] * (1-alpha)),
                        int(color[1] * alpha + last_color[1] * (1-alpha)),
                        int(color[2] * alpha + last_color[2] * (1-alpha)))

        last_color = filtered_color

        data = get_package(filtered_color)

        send_package(data, "192.168.2.200", 1337)

if __name__ == "__main__":
    main()

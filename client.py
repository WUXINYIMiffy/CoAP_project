import time
from coapthon.client.helperclient import HelperClient

host = "192.168.0.134"
port = 5683
path = "basic"


def main():
    client = HelperClient(server=(host, port))

    try:
        for _ in range(50):
            #response = client.put(path, "hello miffy.", _type=1)  # NON
            response = client.put(path, "hello miffy.")  # CON
            if response is not None:
                print(response.pretty_print())
            else:
                print('EMPTY RESPONSE')
            # time.sleep(5)  # 5 seconds
    finally:
        client.stop()


if __name__ == '__main__':
    main()

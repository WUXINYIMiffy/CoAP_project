import time
from coapthon.client.helperclient import HelperClient

host = "192.168.0.129"
port = 5683
path = "basic"


def main():
    client = HelperClient(server=(host, port))

    for _ in range(50):
        # response = client.put(path, "hello miffy.", _type=1)  # NON
        response = client.put(path, "hello miffy.")  # CON
        print(response.pretty_print())
        # time.sleep(5)  # 5 seconds
    client.stop()


if __name__ == '__main__':
    main()

import time
from coapthon.client.helperclient import HelperClient

host = "192.168.0.129"
port = 5683
path = "basic"


def main():
    client = HelperClient(server=(host, port))
    try:
        while True:
            response = client.put(path, "hello miffy.", _type=1)
            print(response.pretty_print())
            time.sleep(5)  # 5 seconds
    finally:
        client.stop()


if __name__ == '__main__':
    main()

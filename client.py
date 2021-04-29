import time
from coapthon.client.helperclient import HelperClient

host = "192.168.0.100"
port = 5683
path = "basic"

def main():
    client = HelperClient(server=(host, port))
    while True :
        response = client.put(path,"hello miffy.")
        print(response.pretty_print())
        time.sleep(5) #5 seconds
    client.stop()

if __name__ == '__main__':
    main()
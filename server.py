import coapthon.server.coap
from coapthon.resources.resource import Resource
from coapthon.messages.request import Request

Host = "0.0.0.0"
Port = 5683


class BasicResource(Resource):
    def __init__(self, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Basic Resource"

    def render_GET(self, request: Request):
        return self

    def render_PUT(self, request: Request):
        self.payload = request.payload
        return self

    def render_POST(self, request: Request):
        res = BasicResource()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request: Request):
        return True


class CoAPServer(coapthon.server.coap.CoAP):
    def __init__(self, host, port):
        coapthon.server.coap.CoAP.__init__(self, (host, port))
        self.add_resource('basic', BasicResource())


def main():
    print("CoAPServer IP addr : %s port : %d " % (Host, Port))
    server = CoAPServer(Host, Port)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("bye")


if __name__ == '__main__':
    main()

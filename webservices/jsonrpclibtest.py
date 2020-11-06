import jsonrpclib

DB = "odoo-demodb"
USER = "fernanda@vauxoo.com"
PASS = "Vauxoo"

# server proxy object
url = "http://{}:{}/jsonrpc".format("localhost", "8069")
server = jsonrpclib.Server(url)

# log in the given database
uid = server.call(service="common", method="login", args=[DB, USER, PASS])


# helper function for invoking model methods
def invoke(model, method, *args):
    args = [DB, uid, PASS, model, method] + list(args)
    return server.call(service="object", method="execute", args=args)


# create a new course
args = {
    "name": "New Course",
}
co = invoke("openacademy.course", "create", args)

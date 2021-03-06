# flake8: noqa
# pylint: disable-all
import functools
import xmlrpc.client

HOST = "localhost"
PORT = 8069
DB = "odoo-demodb"
USER = "fernanda@vauxoo.com"
PASS = "Vauxoo"
ROOT = "http://%s:%d/xmlrpc/" % (HOST, PORT)

# 1. Login
uid = xmlrpc.client.ServerProxy(ROOT + "common").login(DB, USER, PASS)
print("Logged in as %s (uid:%d)" % (USER, uid))

call = functools.partial(
    xmlrpc.client.ServerProxy(ROOT + "object").execute, DB, uid, PASS
)

# 2. Read the sessions
sessions = call(
    "openacademy.session", "search_read", [], ["name", "seats", "course_id"]
)
for session in sessions:
    print(
        "Session %s (%s seats) %s"
        % (session["name"], session["seats"], session["course_id"])
    )
# 3.create a new session
session_id = call(
    "openacademy.session",
    "create",
    {"name": "My session test from xmlrpc", "course_id": 5},
)

course_id = call("openacademy.course", "search", [("name", "ilike", "Odoo")])[0]
session_id = call(
    "openacademy.session",
    "create",
    {"name": "My session test assigned", "course_id": course_id},
)

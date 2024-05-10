import pytest

from moschitta_routing.router import Router


def test_add_route():
    router = Router()
    router.add_route("/users", "GET", lambda req: "Get Users")
    assert len(router) == 1


def test_get():
    router = Router()
    router.add_route("/users", "GET", lambda req: "Get Users")
    handler = router.get("/users", "GET")
    assert handler is not None
    assert handler({}) == "Get Users"


def test_get_invalid_route():
    router = Router()
    handler = router.get("/invalid", "GET")
    assert handler is None


def test_len():
    router = Router()
    router.add_route("/users", "GET", lambda req: "Get Users")
    router.add_route("/posts", "GET", lambda req: "Get Posts")
    assert len(router) == 2


def test_iteration():
    router = Router()
    router.add_route("/users", "GET", lambda req: "Get Users")
    router.add_route("/posts", "GET", lambda req: "Get Posts")
    paths = list(router)
    assert "/users" in paths
    assert "/posts" in paths

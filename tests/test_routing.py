import json
from http import HTTPStatus

import pytest

from moschitta_routing.routing import GET, POST, router


@pytest.fixture
def mock_request():
    """Mock request object."""
    return {"param1": "value1", "param2": "value2"}


def test_get_route(mock_request):
    @GET("/test")
    def test_get(request):
        return {"method": "GET", "params": request}

    # Add route to the router
    test_get(mock_request)

    # Retrieve handler from router
    handler = router.get("/test", "GET")
    assert handler is not None

    # Invoke handler
    response = handler(mock_request)

    # Check response
    expected_response = {"data": {"method": "GET", "params": mock_request}}
    assert response == (
        json.dumps(expected_response),
        HTTPStatus.OK,
        {"Content-Type": "application/json"},
    )


def test_post_route(mock_request):
    @POST("/test")
    def test_post(request):
        return {"method": "POST", "params": request}

    # Add route to the router
    test_post(mock_request)

    # Retrieve handler from router
    handler = router.get("/test", "POST")
    assert handler is not None

    # Invoke handler
    response = handler(mock_request)

    # Check response
    expected_response = {"data": {"method": "POST", "params": mock_request}}
    assert response == (
        json.dumps(expected_response),
        HTTPStatus.OK,
        {"Content-Type": "application/json"},
    )

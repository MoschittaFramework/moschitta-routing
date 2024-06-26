# Moschitta Routing Documentation

The `moschitta-routing` package provides a simple and flexible routing system for the Moschitta Framework, allowing developers to define and handle HTTP routes easily.

## Installation

You can install `moschitta-routing` via pip:

```bash
pip install moschitta-routing
```

Or use it with Poetry:

```bash
poetry add moschitta-routing
```

## Usage

### Creating Routes

Routes are created using the provided decorators (`@GET`, `@POST`, `@PUT`, `@PATCH`, `@DELETE`, `@OPTIONS`, `@HEAD`, `@CONNECT`, `@TRACE`) and registered with the router.

```python
from moschitta_routing import GET, POST

@GET('/users')
def get_users(request):
    # Handler logic to retrieve users
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]

@POST('/users')
def create_user(request):
    # Handler logic to create a new user
    return {"message": "User created successfully"}
```

### Handling Requests

Handlers are simple functions that take a request object as input and return a JSON response. You can access request parameters within the handler function.

```python
def get_users(request):
    # Handler logic to retrieve users
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]
```

### Running the Router

After defining routes and handlers, you can run the router to handle incoming HTTP requests.

```python
from moschitta_routing.router import Router

router = Router()

# Add routes here using the provided decorators

if __name__ == "__main__":
    # Run the router
    router.run(host='0.0.0.0', port=8000)
```

## API Reference

### `moschitta_routing.router.Router`

- `add_route(path: str, method: str, handler: Callable[[Any], Any]) -> None`: Adds a new route to the router.
- `get(path: str, method: str = 'GET') -> Optional[Callable[[Any], Any]]`: Retrieves the handler function associated with a specific route.
- `__len__() -> int`: Returns the total number of routes currently defined in the router.
- `__iter__()`: Allows iterating over all registered route paths in the router.

### Decorators

- `@GET(path: str) -> Callable`: Decorator for handling GET requests.
- `@POST(path: str) -> Callable`: Decorator for handling POST requests.
- `@PUT(path: str) -> Callable`: Decorator for handling PUT requests.
- `@PATCH(path: str) -> Callable`: Decorator for handling PATCH requests.
- `@DELETE(path: str) -> Callable`: Decorator for handling DELETE requests.
- `@OPTIONS(path: str) -> Callable`: Decorator for handling OPTIONS requests.
- `@HEAD(path: str) -> Callable`: Decorator for handling HEAD requests.
- `@CONNECT(path: str) -> Callable`: Decorator for handling CONNECT requests.
- `@TRACE(path: str) -> Callable`: Decorator for handling TRACE requests.

## Contributing

Contributions to `moschitta-routing` are welcome! You can contribute by opening issues for bugs or feature requests, submitting pull requests, or helping improve the documentation.

## License

This project is licensed under the [MIT LICENSE](LICENSE).



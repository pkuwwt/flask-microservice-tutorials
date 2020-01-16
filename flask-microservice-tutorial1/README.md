
# A basic flask demo

## Usage

Execute
```python
python3 app.py
```

Then access `http://127.0.0.1:9099/v1.0/ui`.

## Description

A basic flask demo with Swagger API documentation.

  * In `app.py`, application's API is configured as `swagger/my_app.yaml`.
  * Based on `my_app.yaml`, the system will handle the API requests by specified/implied functions in `api.items`.
  * In `api.items`, a `search` function corresponding to the `GET` operation (implied by `yaml` file)
  * The `yaml` file use `operationId` to specify the route functions. If ignored, the default ones will be used.

```yaml
paths:
  /:
    get:
       # Implied operationId: api.get
  /foo:
    get:
       # Implied operationId: api.foo.search
    post:
       # Implied operationId: api.foo.post

  '/foo/{id}':
    get:
       # Implied operationId: api.foo.get
    put:
       # Implied operationId: api.foo.put
    copy:
       # Implied operationId: api.foo.copy
    delete:
       # Implied operationId: api.foo.delete
```

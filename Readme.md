## Como utilizar com Docker

De forma mais simples, basta rodar estes comandos na raíz do projeto:

``` make dbuild ```

Para rodar os teste:
``` make integration-tests ```

A documentacao está:
``` http://0.0.0.0:8000/docs ```

## Endpoints

1 – Registering a vessel. The vessel data input is its code, which can’t be repeated (return the HTTP code appropriate and an error
message if the user tries to register an existing code). For instance, a valid input of a vessel is:“code”:“MV102”.

```
POST: api/v1/vessels
```

2 – Registering a new equipment in a vessel. The data inputs of each equipment are name, code, location and status. Each equipment is
associated to a given vessel and has a unique code, which can’t be repeated (return the HTTP code appropriate and an error message if
the user tries to register a existing code). For each new equipment registered, the equipment status is automatically active. For instance, a
valid input of a new equipment related to a vessel “MV102”is: { "name": "compressor", "code": "5310B9D7", "location": "Brazil" }

```
POST: api/v1/equipments/{vessel_code}
```

3 – Setting an equipment’s status to inactive. The input data should be one or a list of equipment code.

```
NOT
```

4 – Returning all active equipment of a vessel Feel free to use the programming language and tools you would like.

```
GET: api/v1/equipments/{vessel_code}
```

5 -- Add an operation order with a cost to a equipment. For instance, a valid input of a new operation related to a equipment “5310B9D7”
is: {"code": "5310B9D7", type: "replacement", "cost": "10000"}

```
POST: api/v1/order/{equipment_code}
```

6 -- Return the total cost in operation of an equipment by code.

```
GET: api/v1/order/total-costs/{equipment_code}
```

7 -- Return the total cost in operation of a set of equipments by name.

```
NOT
```

8 -- Return the average cost in operation in each vessel.

```
GET: api/v1/order/average-costs
```


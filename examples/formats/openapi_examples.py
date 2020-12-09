from holon.base import BaseModel
from holon.formats.openapi import (
    OpenAPI,
    Components,
    Info,
    PathItem,
    Operation,
    Reference,
    RequestBody,
    MediaType,
    Response,
    Schema,
)


class Email(BaseModel):
    value: str


class Person(BaseModel):
    name: str
    email: Email


api = OpenAPI(
    info=Info(title="My API", version="1.0.0"),
    paths={
        "/foo": PathItem(
            get=Operation(
                requestBody=RequestBody(
                    content={
                        "application/json": MediaType(
                            schema=Person.schema(
                                ref_template="#/components/schemas/{model}"
                            )
                        )
                    }
                ),
                responses={"200": Response(description="Hello world")},
            )
        )
    },
    components=Components(schemas={"Email": Email.schema()}),
)

print(api.json(by_alias=True, exclude_none=True))

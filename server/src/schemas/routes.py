from pydantic import BaseModel


class RouteCreate(BaseModel):
    waypoints: list
    origin: str
    destination: str


class RouteRequest(BaseModel):
    origin: str
    destination: str
    waypoints: list[str]
    route_data: dict


class RouteResponse(BaseModel):
    id: int
    origin: str
    destination: str
    waypoints: list[str]
    route_data: dict


class RouteUpdateRequest(BaseModel):
    origin: str | None = None
    destination: str | None = None
    waypoints: list[str] | None = []
    route_data: dict | None = {}

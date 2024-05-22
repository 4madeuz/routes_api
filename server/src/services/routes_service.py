from fastapi import Depends,  HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.db.postgres import get_session
from src.models.routes import Route
from src.schemas.routes import RouteCreate, RouteRequest, RouteUpdateRequest, RouteResponse


class RouteService():
    """Сервис для управления URL"""

    def __init__(
        self,
        session: AsyncSession,
    ):
        self.session = session

    async def create_route(self, route_request: RouteCreate) -> RouteCreate:
        db_route = Route(
            origin=route_request.origin,
            destination=route_request.destination,
            waypoints=route_request.waypoints,
            route_data=route_request.route_data
        )
        self.session.add(db_route)
        await self.session.commit()
        await self.session.refresh(db_route)
        return db_route

    async def delete_route(self, route_id: int) -> dict:
        db_route = await self.session.get(Route, route_id)
        if db_route is None:
            raise HTTPException(status_code=404, detail="Route not found")

        await self.session.delete(db_route)
        await self.session.commit()
        return {"message": "Route deleted successfully"}

    async def put_route(self, route_request: RouteRequest, route_id: int) -> RouteResponse:
        db_route = await self.session.get(Route, route_id)
        if db_route is None:
            raise HTTPException(status_code=404, detail="Route not found")

        db_route.origin = route_request.origin
        db_route.destination = route_request.destination
        db_route.waypoints = route_request.waypoints
        db_route.route_data = route_request.route_data

        await self.session.commit()
        await self.session.refresh(db_route)
        return db_route

    async def patch_route(self, route_id: int, route_update: RouteUpdateRequest) -> RouteResponse:
        db_route = await self.session.get(Route, route_id)
        if db_route is None:
            raise HTTPException(status_code=404, detail="Route not found")

        if route_update.origin is not None:
            db_route.origin = route_update.origin
        if route_update.destination is not None:
            db_route.destination = route_update.destination
        if route_update.waypoints is not None:
            db_route.waypoints = route_update.waypoints
        if route_update.route_data is not None:
            db_route.route_data = route_update.route_data

        await self.session.commit()
        await self.session.refresh(db_route)
        return db_route

    async def load_routes(self) -> list[RouteResponse]:
        routes = await self.session.execute(select(Route))
        return routes.unique().scalars().all()

    async def get_by_id(self, route_id: int) -> RouteResponse:
        db_route = await self.session.get(Route, route_id)
        if db_route is None:
            raise HTTPException(status_code=404, detail="Route not found")
        return db_route


def get_route_service(
    pg_session: AsyncSession = Depends(get_session),
) -> RouteService:
    return RouteService(
        session=pg_session,
    )

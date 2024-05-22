from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime

from src.schemas.routes import RouteCreate, RouteRequest, RouteResponse, RouteUpdateRequest
from src.services.routes_service import RouteService, get_route_service

router = APIRouter()


@router.post("/", response_model=RouteRequest)
async def create_route(
    route_data: RouteRequest,
    service: RouteService = Depends(get_route_service),
        ):
    return await service.create_route(route_data)


@router.get("/", response_model=list[RouteResponse])
async def get_routes(
    service: RouteService = Depends(get_route_service),
        ):
    return await service.load_routes()


@router.put("/{route_id}", response_model=RouteResponse)
async def put_route(
    route_id: int,
    route_request: RouteRequest,
    service: RouteService = Depends(get_route_service),
        ):
    return await service.put_route(route_request, route_id)


@router.patch("/{route_id}")
async def patch_route(
    route_id: int,
    route_request: RouteUpdateRequest,
    service: RouteService = Depends(get_route_service),
        ):
    return await service.patch_route(route_id, route_request)


@router.delete("/{route_id}")
async def delete_route(
    route_id: int,
    service: RouteService = Depends(get_route_service),
        ):
    return await service.delete_route(route_id)


@router.get("/{route_id}")
async def get_by_id(
    route_id: int,
    service: RouteService = Depends(get_route_service),
        ):
    return await service.get_by_id(route_id)

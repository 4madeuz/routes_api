from sqlalchemy import Column, Integer, String, JSON

from src.db.postgres import Base


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    origin = Column(String, index=True)
    destination = Column(String, index=True)
    waypoints = Column(JSON)
    route_data = Column(JSON)

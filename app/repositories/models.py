from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from .orm import Base


class Vessels(Base):
    __tablename__ = "vessels"

    id = Column(Integer, primary_key=True, unique=True)
    code = Column(String, index=True, unique=True)

    equipments = relationship("Equipments", back_populates="owner")


class Equipments(Base):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True, unique=True)
    equipment_code = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    location = Column(String, index=True)
    active = Column(Boolean, index=True, default=True)

    vessel_code = Column(String, ForeignKey("vessels.code"))
    owner = relationship("Vessels", back_populates="equipments")

    orders = relationship("Orders", back_populates="owner_orders")


class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String, index=True)
    cost = Column(Float, index=True)

    equipment_code = Column(String, ForeignKey("equipments.equipment_code"))
    owner_orders = relationship("Equipments", back_populates="orders")
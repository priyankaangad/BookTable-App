from sqlalchemy import Column, DateTime, ForeignKey, Integer
from app.database import Base
from sqlalchemy.orm import relationship
from app.models import UserModel, RestaurantModel

class RestaurantManager(Base):
    __tablename__ = "restaurant_managers"

    manager_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False, unique=True)
    approved_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="restaurant_manager")
    restaurants = relationship("Restaurant", back_populates="manager")
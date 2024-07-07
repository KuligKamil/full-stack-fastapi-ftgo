from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, func
from uuid import uuid4
from sqlalchemy.orm import relationship
from data_access.models.base import Base
from config.timezone import tz

class Address(Base):
    __tablename__ = "user_address"

    id = Column(String, primary_key=True, default=lambda: uuid4().hex)
    user_id = Column(String, ForeignKey("user_profile.id"), nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    postal_code = Column(String, nullable=True)
    country = Column(String, nullable=True, default="IR")
    is_default = Column(Boolean, nullable=True, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    profile = relationship("Profile", back_populates="addresses")

from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image_url = Column(String, index=True)
    tags = Column(String, index=True)
    strategies = relationship("Strategy", back_populates="track")

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
    name = Column(String, nullable=False)
    position_min = Column(Integer, nullable=False)
    position_max = Column(Integer, nullable=False)
    track = relationship("Track", back_populates="strategies")
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cup = Column(String, index=True)
    laps = Column(Integer)
    header_color = Column(String)
    description = Column(String)
    # Traits shown as tags under the title (also used for filtering).
    traits = Column(JSON)
    # True for DLC (Booster Course Pass) tracks — shows a DLC pill on the card.
    dlc = Column(Boolean, default=False, nullable=False)
    strategies = relationship("Strategy", back_populates="track")

class Strategy(Base):
    __tablename__ = "strategies"

    id = Column(Integer, primary_key=True, index=True)
    track_id = Column(Integer, ForeignKey("tracks.id"), nullable=False)
    name = Column(String, nullable=False)
    position_min = Column(Integer, nullable=False)
    position_max = Column(Integer, nullable=False)
    track = relationship("Track", back_populates="strategies")
from database import Base
from sqlalchemy import Integer, String, ForeignKey, JSON, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    cup: Mapped[str] = mapped_column(String, index=True)
    laps: Mapped[int] = mapped_column(Integer)
    header_color: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    # Slippery off-road classification: "None" (no traction-reducing
    # surface), "Sand", or "Ice".
    terrain: Mapped[str] = mapped_column(String)
    # Traits shown as tags under the title (also used for filtering).
    traits: Mapped[list[str]] = mapped_column(JSON)
    # True for DLC (Booster Course Pass) tracks — shows a DLC pill on the card.
    dlc: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    strategies: Mapped[list["Strategy"]] = relationship(
        "Strategy", back_populates="track"
    )

class Strategy(Base):
    __tablename__ = "strategies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    track_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tracks.id"), nullable=False
    )
    position_min: Mapped[int] = mapped_column(Integer, nullable=False)
    position_max: Mapped[int] = mapped_column(Integer, nullable=False)
    # Tips for executing this specific strategy (list of short strings).
    tips: Mapped[list[str]] = mapped_column(JSON)
    track: Mapped["Track"] = relationship("Track", back_populates="strategies")

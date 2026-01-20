#!/usr/bin/env python3

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def display_station(station: SpaceStation) -> None:
    print("ID:", station.station_id)
    print("Name:", station.name)
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print("Status:", "Operational" if station.is_operational
          else "Non Operational")


def main():
    print("Space Station Data Validation")
    print("========================================")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        last_maintenance=datetime.now(),
        power_level=85.5,
        oxygen_level=92.3
    )
    print("Valid station created:")
    display_station(station)
    print()
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS002",
            name="International Space Station2",
            crew_size=30,
            last_maintenance="1768480218",
            power_level=85.5,
            oxygen_level=92.3
        )
    except Exception as e:
        print("Expected validation error:")
        message = str(e).split('[')[0].split('\n')[2].strip()
        print(message)


if __name__ == "__main__":
    main()

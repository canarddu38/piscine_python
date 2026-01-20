#!/usr/bin/env python3

from typing import List
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(m.rank in {Rank.COMMANDER, Rank.CAPTAIN}
                   for m in self.crew):
            raise ValueError("Mission must have at least one \
Commander or Captain")

        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                raise ValueError("Long missions require at least \
50% experienced crew")
        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    mission = SpaceMission(
        mission_name="Mars Colony Establishment",
        mission_id="M2024_MARS",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=[
            CrewMember(
                member_id="member1",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=18,
                specialization="Mission Command",
                years_experience=10
            ),
            CrewMember(
                member_id="member2",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=18,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="member3",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=18,
                specialization="Engineering",
                years_experience=10
            )
        ],
        launch_date=datetime.now()
    )
    print("Valid mission created:")
    print("Mission:", mission.mission_name)
    print("ID:", mission.mission_id)
    print("Destination:", mission.destination)
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew size:", len(mission.crew))
    print("Crew members:")
    for crewmate in mission.crew:
        print(f"- {crewmate.name} ({crewmate.rank._name_.lower()})\
 - {crewmate.specialization}")
    print("\n=========================================")
    try:
        mission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="member3",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=18,
                    specialization="Engineering",
                    years_experience=10
                )
            ],
            launch_date=datetime.now()
        )
    except ValueError as e:
        print("Expected validation error:")
        print(str(e).split('\n')[1].strip()
              .replace("Value error, ", '').split('[')[0])


if __name__ == "__main__":
    main()

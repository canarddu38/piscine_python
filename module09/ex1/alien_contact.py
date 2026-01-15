#!/usr/bin/env python3

from typing import Optional
from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self
from enum import Enum
from datetime import datetime


class ContactType(Enum):
    radio = 0
    visual = 1
    physical = 2
    telepathic = 3


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(..., max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise Exception("Invalid contact ID")
        if self.is_verified is False and self.contact_type == ContactType.physical:
            raise Exception("Contact need to be verified")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise Exception("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0:
            if not hasattr(self, "message_received"):
                raise Exception("Strong signals must include messages")
        return self


def main():
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact = AlienContact(
        contact_id="AC_2024_001",
        contact_type=ContactType.radio,
        location="Area 51, Nevada",
        timestamp="1768488824",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )
    print("ID:", contact.contact_id)
    print("Type:", str(contact.contact_type).split('.')[1])
    print("Location:", contact.location)
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print("Witnesses:", contact.witness_count)
    print(f"Message: '{contact.message_received}'\n")
    print("======================================")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.telepathic,
            location="Area 51, Nevada",
            timestamp="1768488824",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except Exception as e:
        print("Expected validation error:")
        message = str(e)
        print(message)


if __name__ == "__main__":
    main()

"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = MudroomLowLight()
    add_entities([ent])


class MudroomLowLight(NewLight):
    """Mudroom Low Light."""

    def __init__(self) -> None:
        """Initialize Mudroom Low Light."""
        super(MudroomLowLight, self).__init__(
            "Mudroom Low Light", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.mudroom_low_group"] = None
        self.switch = "Mudroom Switch"
        self.motion_sensors.append("Mudroom Low Motion Sensor")
        self.motion_sensors.append("Mudroom High Motion Sensor")
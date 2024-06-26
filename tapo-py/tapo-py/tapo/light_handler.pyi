from enum import StrEnum
from typing import Optional

from .types import (
    DefaultBrightnessState,
    DefaultPowerType,
    DeviceUsageResult,
)

class LightHandler:
    """Handler for the [L510](https://www.tapo.com/en/search/?q=L510), [L520](https://www.tapo.com/en/search/?q=L520) and [L610](https://www.tapo.com/en/search/?q=L610) devices."""

    def __init__(self, handler: object):
        """Private constructor.
        It should not be called from outside the tapo library.
        """

    async def refresh_session(self) -> None:
        """Refreshes the authentication session."""

    async def on(self) -> None:
        """Turns *on* the device."""

    async def off(self) -> None:
        """Turns *off* the device."""

    async def device_reset(self) -> None:
        """*Hardware resets* the device.

        Warning:
            This action will reset the device to its factory settings.
            The connection to the Wi-Fi network and the Tapo app will be lost,
            and the device will need to be reconfigured.

        This feature is especially useful when the device is difficult to access
        and requires reconfiguration.
        """

    async def get_device_info(self) -> DeviceInfoLightResult:
        """Returns *device info* as `DeviceInfoLightResult`.
        It is not guaranteed to contain all the properties returned from the Tapo API.
        If the deserialization fails, or if a property that you care about it's not present,
        try `LightHandler.get_device_info_json`.

        Returns:
            DeviceInfoLightResult: Device info of Tapo L510, L520 and L610.
            Superset of `GenericDeviceInfoResult`.
        """

    async def get_device_info_json(self) -> dict:
        """Returns *device info* as json.
        It contains all the properties returned from the Tapo API.

        Returns:
            dict: Device info as a dictionary.
        """

    async def get_device_usage(self) -> DeviceUsageResult:
        """Returns *device usage* as `DeviceUsageResult`.

        Returns:
            DeviceUsageResult: Contains the time usage.
        """

    async def set_brightness(self, brightness: int) -> None:
        """Sets the *brightness* and turns *on* the device.

        Args:
            brightness (int): between 1 and 100
        """

class DeviceInfoLightResult:
    """Device info of Tapo L510, L520 and L610. Superset of `GenericDeviceInfoResult`."""

    device_id: str
    type: str
    model: str
    hw_id: str
    hw_ver: str
    fw_id: str
    fw_ver: str
    oem_id: str
    mac: str
    ip: str
    ssid: str
    signal_level: int
    rssi: int
    specs: str
    lang: str
    device_on: bool
    on_time: int
    """The time in seconds this device has been ON since the last state change (ON/OFF)."""
    overheated: bool
    nickname: str
    avatar: str
    has_set_location_info: bool
    region: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    time_diff: Optional[int]

    # Unique to this device
    brightness: int
    default_states: DefaultLightState
    """The default state of a device to be used when internet connectivity is lost after a power cut."""

    def to_dict(self) -> dict:
        """Gets all the properties of this result as a dictionary.

        Returns:
            dict: The result as a dictionary.
        """

class DefaultLightState:
    """Light Default State."""

    brightness: DefaultBrightnessState
    re_power_type: Optional[DefaultPowerType]

"""
Custom PVPositioner class using supplied PVs & values.

This is an alternative to defining subclasses of
PVPositioner for each set of PVs.
"""

from typing import Optional
from typing import Union

from apstools.utils import dynamic_import
from ophyd import Component
from ophyd import Device
from ophyd import EpicsSignal
from ophyd import EpicsSignalRO


def pvpositioner_factory(
    readback_pv: str = "",
    setpoint_pv: str = "",
    done_pv: str = "",
    stop_pv:str = "",
    *,
    done_value: Optional[Union[int, str]]  =1,
    stop_value: Optional[Union[int, str]] =1,
    actuate_pv: str =None,
    actuate_value:Optional[Union[int, str]]=None,
) -> Device:
    """Build a PVPositioner class with supplied PVs and values."""
    base_class = dynamic_import("ophyd.PVPositioner")

    # Define attributes of the custom class.
    attrs = dict(
        readback = Component(EpicsSignalRO, readback_pv),
        setpoint = Component(EpicsSignal, setpoint_pv),
        done = Component(EpicsSignalRO, done_pv, kind="omitted"),
        stop_signal = Component(EpicsSignal, stop_pv, kind="omitted"),

        done_value = done_value,
        stop_value = stop_value,
    )

    # Optional attributes
    if actuate_pv is not None:
        attrs["actuate"] = Component(EpicsSignal, actuate_pv, kind="omitted")
        if actuate_value is not None:
            attrs["actuate_value"] = actuate_value

    # Return the custom class.
    return type("PVPositioner", tuple([base_class,]), attrs)

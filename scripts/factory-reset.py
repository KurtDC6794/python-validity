import time

import usb.core as usb_core

from validitysensor.sensor import factory_reset, RebootException
from validitysensor.usb import usb

# The internal sensor can't be replugged, so reset it first to clear a stuck session.
_d = usb_core.find(idVendor=0x06CB, idProduct=0x0081)
if _d is not None:
    try:
        _d.reset()
    except Exception:
        pass
    time.sleep(2)

try:
    usb.open()
    factory_reset()
except RebootException:
    pass

#!/usr/bin/env python3
"""
Kill a qemu guest
=================

Retargetable: False
-------------------

Step arguments
--------------

* step.with.guest_name
  - can be specified in the configuration file with key cijoe.qemu.default.guest_name
"""
import logging as log

from cijoe.qemu.wrapper import Guest


def main(args, cijoe, step):
    """Kill a qemu guest"""

    guest_name = step.get("with", {}).get(
        "guest_name", cijoe.getconf("cijoe.qemu.default.guest_name", None)
    )
    if guest_name is None:
        log.error("missing step-argument: with.guest_name")
        return 1

    guest = Guest(cijoe, cijoe.config, guest_name)

    return guest.kill()

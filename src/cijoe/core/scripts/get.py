"""
get
===

Copies a file from remote to local.

Step Arguments
--------------

* step.with.src: path to the file on remote machine
  - can be specified in the configuration file with key cijoe.core.default.get_src

* step.with.dst: path to where the file should be placed on the local machine
  - can be specified in the configuration file with key cijoe.core.default.get_dst

Retargetable: True
------------------
"""

import errno
import logging as log


def main(args, cijoe, step):
    """Copies the file at step.with.src on the remote machine to step.with.dst on the local machine"""

    src = step.get("with", {}).get(
        "src", cijoe.getconf("cijoe.core.default.get_src", None)
    )
    dst = step.get("with", {}).get(
        "dst", cijoe.getconf("cijoe.core.default.get_dst", None)
    )
    if not (src and dst):
        log.error("missing step-argument: with.src and/or with.dst")
        return errno.EINVAL

    return int(not cijoe.get(step["with"]["src"], step["with"]["dst"]))

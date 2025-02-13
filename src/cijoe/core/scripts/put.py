"""
put
===

Copies a file from local to remote.

Step Arguments
--------------

* step.with.src: path to the file on local machine
    can be specified in the configuration file under key cijoe.core.default.put_src

* step.with.dst: path to where the file should be placed on the remote machine
    can be specified in the configuration file under key cijoe.core.default.dst_src

Retargetable: True
------------------
"""

import errno
import logging as log


def main(args, cijoe, step):
    """Copies the file at step.with.src on the local machine to step.with.dst on the remote machine"""

    src = step.get("with", {}).get(
        "src", cijoe.getconf("cijoe.core.default.put_src", None)
    )
    dst = step.get("with", {}).get(
        "dst", cijoe.getconf("cijoe.core.default.put_dst", None)
    )
    if not (src and dst):
        log.error("missing step-argument: with.src and/or with.dst")
        return errno.EINVAL

    return int(not cijoe.put(step["with"]["src"], step["with"]["dst"]))

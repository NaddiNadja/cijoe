"""
cmdrunner
=========

Executes a list of commands in the given order. Note that multi-line commands are not
supported, each line or list of strings are treated as individual commands.

Retargetable: True
------------------

Step Arguments
--------------

* step.with.commands: the commands that will be executed.
  - can be specified in the configuration file with key cijoe.core.default.commands
"""

import errno
import logging as log


def main(args, cijoe, step):
    """Run commands one at a time via cijoe.run()"""

    err = 0
    commands = step.get("with", {}).get(
        "commands", cijoe.getconf("cijoe.core.default.commands", None)
    )
    if not commands:
        log.error("missing step-argument: with.commands")
        return errno.EINVAL

    for cmd in step["with"]["commands"]:
        err, state = cijoe.run(cmd)
        if err:
            break

    return err

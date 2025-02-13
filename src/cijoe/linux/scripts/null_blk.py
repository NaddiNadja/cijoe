"""
insert / remove null_blk
========================

Insert or remove null_blk instances, based on the value of step.with.do
If step.with.do is not specified, the script will try to find the value
in the configuration file under key cijoe.linux.default.null_blk_do

* steps.with.do == "insert"
  - Insert the nullblk module

* step.with.do == "remove"
  - Remove the nullblk module

Retargetable: True
------------------
"""

import errno

import cijoe.linux.null_blk as null_blk


def main(args, cijoe, step):
    """Insert or remove the null_blk"""

    do = step.get("with", {}).get(
        "do", cijoe.getconf("cijoe.linux.default.null_blk_do", "insert")
    )
    if do == "insert":
        err, _ = null_blk.insert(cijoe)
    elif do == "remove":
        err, _ = null_blk.remove(cijoe)
    else:
        err = errno.EINVAL

    return err

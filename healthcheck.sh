#!/bin/bash
pgrep -f openclaw > /dev/null || /home/plagueis/.npm-global/bin/openclaw gateway restart

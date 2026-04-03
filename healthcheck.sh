#!/bin/bash
pgrep -f openclaw > /dev/null || /home/seva/.npm-global/bin/openclaw gateway restart

#!/bin/bash

socat TCP-LISTEN:10001,fork,max-children=1,reuseaddr EXEC:/teespace/run.sh,pty,stderr,setsid,ctty

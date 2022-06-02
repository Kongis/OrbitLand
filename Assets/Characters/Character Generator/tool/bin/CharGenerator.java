#!/bin/sh
JLINK_VM_OPTIONS=
DIR=`dirname $0`
$DIR/java $JLINK_VM_OPTIONS -m mario.main/com.almasb.fxglgames.mario.chargen.CharGenerator "$@"

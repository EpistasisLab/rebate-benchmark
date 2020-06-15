#!/bin/bash
for f in `find . -type d`; do
    mv `echo "$f"` `echo "$f" | sed 's/\(.*\)\/.*EDM/\1\/EDM/g'`
done

#!/bin/bash

# Add mods to the server
cat modlist.txt | while read line; do
    packwiz mr add $line
done

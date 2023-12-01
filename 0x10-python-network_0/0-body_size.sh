#!/bin/bash
curl -s -i "$1" | grep "Content-Length" | cut -d " " -f 2

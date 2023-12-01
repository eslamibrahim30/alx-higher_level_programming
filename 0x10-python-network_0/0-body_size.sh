#!/bin/bash
curl -i "$1" | grep "Content-Length" | cut -d " " -f 2

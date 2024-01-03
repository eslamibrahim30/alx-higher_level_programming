#!/bin/bash
# displays the size of the body of the response
curl -s -i "$1" | grep "Content-Length" | cut -d " " -f 2

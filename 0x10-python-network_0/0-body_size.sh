#!/bin/bash
#Bash script that takes in a URL & displays the size of the body of the response
curl -sI "$1" | grep -i content-length | cut -d " " -f2

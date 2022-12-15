#!/bin/bash
# Bash script that takes in a URL & displays the body of the response
curl -s "$1" GET -H "X-HolbertonSchool-User-Id: 98"

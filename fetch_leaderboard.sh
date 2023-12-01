#!/bin/bash
curl -b "session=$(cat session-cookie.txt)" https://adventofcode.com/2023/leaderboard/private/view/1234837.json

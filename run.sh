#!/bin/bash
docker run -ti --rm -e DATE_FROM -e DATE_TO -e LENDO_API_TOKEN ecerulm/lendofetch:latest

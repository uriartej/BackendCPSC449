#!/bin/sh

http --verbose POST localhost:5400/auth_api/books/ @"$1"

# Put in port to KrakenD; Not Finished
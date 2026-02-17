# Log Analyzer (Python CLI Tool)

A small but practical log analysis tool I built while wrapping up my Python phase.
The goal wasn’t to create something huge — just a clean utility that actually feels like a real backend support tool.

## What it does

* Reads a log file from the command line
* Counts INFO, WARNING, and ERROR entries
* Detects repeated error patterns
* Identifies possible error spikes (consecutive errors)
* Generates a simple `report.txt` summary automatically

## Built With

* Python
* argparse (CLI arguments)
* collections.Counter (pattern detection)
* basic file handling

## How to Run

Example command:

python log_analyzer.py --file test.log

Optional filter:

python log_analyzer.py --file test.log --level ERROR

## Features

* CLI-based workflow
* Log level filtering
* Top repeated error detection
* Simple spike detection logic
* Report file generation

## Why I made this

This project was part of my Python wrap-up phase.
The focus was on building small but realistic tools before moving into backend development with Java.

## Notes

Not meant to be a full production monitoring system — just a lightweight engineering-style analyzer that demonstrates structured thinking and CLI tool design.

Built while learning — simple, practical, and always improving. Feel free to upgrade or modify it, Happy coding !

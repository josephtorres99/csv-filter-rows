![CSV Filter Rows](assets/hero.png)

# CSV Filter Rows

*A where-clause for a CSV.*

## About

**CSV Filter Rows** is a developer utility. Filter CSV rows by a column equals or contains a value.

Opening a 100 MB CSV in Excel just to keep one status is waste.

The CLI is the source of truth. The desktop build is optional if you do not want Python installed.

## How to get it

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## What it does

- Equals or contains
- Column name
- Case option
- Keeps the header

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/josephtorres99/csv-filter-rows

MIT license. See `LICENSE`.

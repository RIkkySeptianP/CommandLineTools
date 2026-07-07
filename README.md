# CommandLineTools

A simple command-line utility written in Python for converting log files into either JSON or plain text format.

## Features

- Convert text log files into JSON format
- Export plain text files
- Custom output file name
- Lightweight command-line interface using argparse

## Tech Stack

- Python 3
- argparse
- pathlib
- json

## Project Structure

```
CommandLineTools/
│
├── main.py
├── README.md
└── sample/
    ├── input.txt
    └── output.json
```

## Usage

Convert to JSON

```bash
python main.py input.txt -t json -o output.json
```

Convert to Text

```bash
python main.py input.txt -t text -o output.txt
```

Default Output

```bash
python main.py input.txt
```

This will generate:

```
mytools.txt
```

## Example Input

```
Login Success
Create User
Delete User
```

## Example Output (JSON)

```json
{
  "data": [
    {
      "count": "1",
      "text": "Login Success"
    },
    {
      "count": "2",
      "text": "Create User"
    }
  ]
}
```

## Future Improvements

- CSV Export
- XML Export
- Log Filtering
- Batch File Processing
- Progress Indicator

## Author

**Rikky Septian Prasetiyo**

Backend Engineer (.NET & Python)

Currently learning Kotlin and Kubernetes.

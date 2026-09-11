# serial-reader

A simple utility to read from a selected serial port and strip ANSI escape codes.

## Installation

```bash
uv pip install .
```

Or to install with uv and create a virtual environment:

```bash
uv venv          # creates virtual environment using uv
uv pip install -e .  # install in development mode
```

## Usage

Run the script and select a serial port from the list:

```bash
python main.py
```

The application will:
1. List all available serial ports
2. Prompt you to select one by index
3. Read data from the selected port at 115200 baud
4. Strip ANSI escape codes (like color codes) from the received data
5. Print the cleaned lines to the console

Press `Ctrl+C` to stop reading and exit.

## Dependencies

- Python 3.14+
- pyserial>=3.5

## Development

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

To set up for development:

```bash
uv venv          # creates virtual environment
uv pip install -e .  # install package in editable mode
uv pip install pytest  # install test dependencies (if adding tests)
```

## License

This project is open source and available under the MIT License.
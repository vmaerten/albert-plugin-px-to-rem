# Albert PX to REM Converter

A simple [Albert](https://albertlauncher.github.io/) plugin to convert pixels to rem units and vice versa.

## Installation

```bash
task install
```

Then enable the plugin in Albert Settings → Plugins → Python → "PX to REM Converter".

To uninstall:

```bash
task uninstall
```

## Usage

Trigger: `px `

| Input | Output | Description |
|-------|--------|-------------|
| `px 16` | `1rem` | Convert 16px to rem (base 16) |
| `px 24` | `1.5rem` | Convert 24px to rem |
| `px 1rem` | `16px` | Convert 1rem to px |
| `px 1.5rem` | `24px` | Convert 1.5rem to px |
| `px 32 10` | `3.2rem` | Convert 32px with custom base (10px) |
| `px 2rem 10` | `20px` | Convert 2rem with custom base (10px) |

## Actions

- **Enter/Click**: Copy result with unit (e.g., `1.5rem`)
- **Alt+Enter**: Copy number only (e.g., `1.5`)

## Requirements

- Albert 33+
- Python plugin enabled
- [Task](https://taskfile.dev/) (for installation)

## License

MIT

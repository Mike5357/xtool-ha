# xTool F1 Home Assistant Integration

This is a custom integration for Home Assistant to interface with the xTool F1 laser engraver.

## Features
- Displays the current status of the xTool F1 (e.g., "P_WORK_DONE").
- Can be integrated into Home Assistant for monitoring and automation.

## Installation

1. Download or clone this repository.
2. Place the `xtool_f1` folder in the `custom_components` directory of your Home Assistant installation.
3. Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: xtool_f1

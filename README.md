# XTool Home Assistant Integration

This is a custom integration for Home Assistant to interface with the XTool laser engraver.

## Features
- Displays the current status of the XTool (e.g., "In Arbeit", "Abgeschlossen", "Im Leerlauf").
- Can be integrated into Home Assistant for monitoring and automation.

## Installation

1. Download or clone this repository.
2. Place the `xtool` folder in the `custom_components` directory of your Home Assistant installation.
3. Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: xtool
    ip_address: "xxx.xxx.xxx.xxx"  # Replace with the IP address of your XTool
```

## Usage

Once the integration is installed and configured, a sensor will be created in Home Assistant displaying the current status of the XTool. The status values can include:

- **In Arbeit**: The XTool is currently working.
- **Abgeschlossen**: The work is completed.
- **Im Leerlauf**: The XTool is idle.
- **Schlafmodus**: The XTool is in sleep mode.
- **Unbekannt**: The status could not be retrieved.

You can use these sensor states in automations to monitor and control the XTool's activities.

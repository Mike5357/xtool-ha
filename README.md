# XTool Home Assistant Integration

This is a custom integration for Home Assistant to interface with the XTool laser engraver.

## Features
- Displays the current status of the XTool in English (e.g., "Working", "Completed". "Idle").
- Can be integrated into Home Assistant for monitoring and automation.
- Configurable status sensor name

## Installation

1. Download or clone this repository.
2. Place the `xtool` folder in the `custom_components` directory of your Home Assistant installation.
3. Add the following to your `configuration.yaml`:

```yaml
sensor:
  - platform: xtool
    ip_address: "xxx.xxx.xxx.xxx"  # Replace with the IP address of your XTool
    name: "XTool Status"
```

## Usage

Once the integration is installed and configured, a sensor will be created in Home Assistant displaying the current status of the XTool. The status values can include:

- **Working**: The XTool is currently working.
- **Completed**: The work is completed.
- **Idle**: The XTool is idle.
- **Sleeping**: The XTool is in sleep mode.
- **Unknown**: The status could not be retrieved.

You can use these sensor states in automations to monitor and control the XTool's activities.

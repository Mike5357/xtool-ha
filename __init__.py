from homeassistant.core import HomeAssistant

async def async_setup(hass: HomeAssistant, config: dict):
    """Setup the xTool F1 integration."""
    hass.states.async_set("xtool_f1.status", "unknown")
    return True

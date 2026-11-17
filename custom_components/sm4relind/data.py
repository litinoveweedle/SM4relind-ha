import lib4relind

FULL_NAME = "Four Relays Four Inputs"
LINK = (
    "https://sequentmicrosystems.com/products/four-relays-four-inputs-for-raspberry-pi"
)
API = lib4relind
DOMAIN = "sm4relind"
NAME_PREFIX = "sm4ri"
SM_MAP = {
    "binary_sensor": {
        "opto": {
            "chan_no": 4,
            "uom": "",
            "com": {
                "get": "get_opto",
            },
        },
    },
    "switch": {
        "relay": {
            "chan_no": 4,
            "com": {
                "get": "get_relay",
                "set": "set_relay",
            },
        }
    },
}

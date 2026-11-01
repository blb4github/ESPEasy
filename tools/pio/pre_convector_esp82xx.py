# Dedicated compact ESPEasy build for the PET10 V2 convector controllers.
# Based on official mega-20260720, without changing other build variants.
# Keep source plugin P026 (System Info), even if HA monitoring only exposes
# a subset of the device's internal tasks.
Import("env")

defines = [
    "-DESP8266",
    "-DPLUGIN_SET_NONE",
    "-DCONTROLLER_SET_NONE",
    "-DNOTIFIER_SET_NONE",
    "-DUSES_C005",  # Existing CW MQTT controller: Home Assistant (openHAB) MQTT
    "-DUSES_C013",  # Existing CW P2P controller (configured but disabled)
    "-DUSES_P003",  # Generic Pulse Counter: fan tachometer
    "-DUSES_P004",  # Dallas: inlet temperature
    "-DUSES_P005",  # DHT22
    "-DUSES_P026",  # System Info: existing Status task
    "-DUSES_P033",  # Dummy: Control, Runtime, FanConfig, Validity, TempConfig
    "-DUSES_P037",  # MQTT Import: heat pump and presence
    "-DFEATURE_MQTT_TLS=0",
    "-DFEATURE_EMAIL_TLS=0",
    "-DFEATURE_MDNS=0",
    "-DFEATURE_PLUGIN_STATS=0",
    "-DFEATURE_CHART_JS=0",
    "-DFEATURE_SETTINGS_ARCHIVE=0",
    "-DFEATURE_ESPEASY_P2P=1",
    "-DFEATURE_EXT_RTC=0",
    "-DFEATURE_I2CMULTIPLEXER=0",
    "-DFEATURE_TRIGONOMETRIC_FUNCTIONS_RULES=0",
]
env.Append(CXXFLAGS=defines)
print("Convector build: " + " ".join(defines))

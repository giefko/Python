import wmi
w = wmi.WMI(namespace="root\wmi")
temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
print temperature_info.CurrentTemperature

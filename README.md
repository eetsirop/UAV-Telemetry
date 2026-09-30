# UAV-Telemetry

This repository contains per-node telemetry data collected from wireless sensor nodes during UAV-assisted data collection experiments on the PROTON testbed. The dataset is organized as individual CSV files, where each file corresponds to one sensor node and each row corresponds to one telemetry epoch.

The data can be used for research on UAV-enabled wireless sensing, low-altitude edge data collection, solar-powered sensor networks, wireless link quality analysis, energy-aware communication, and time-series forecasting.

## Dataset Overview

The full dataset contains telemetry from 74 individual sensor nodes. Each node file follows the naming format:

```text
node_data_<DEVICE_ID>.csv
```

For example:

```text
node_data_901564800F9C.csv
```

Each file stores epoch-level measurements from a single node, including battery state, photovoltaic energy harvesting, wireless packet statistics, received signal strength, packet reception ratio, throughput, and battery energy estimates.

## Data Format

Each CSV file contains one row per telemetry epoch. The sample node file `node_data_901564800F9C.csv` contains 72 epochs and 22 columns.

| Column | Description |
| --- | --- |
| `Device ID` | Unique identifier of the sensor node. |
| `Device Slot` | Slot or logical index assigned to the device during the experiment. |
| `Event` | Type of logged event, such as telemetry. |
| `Epoch Number` | Sequential epoch index for the node. |
| `Bat mV` | Battery voltage in millivolts. |
| `Bat mA` | Battery current in milliamperes. |
| `Bat mW` | Battery power in milliwatts. |
| `Bat mJ (Epoch)` | Battery energy used during the epoch in millijoules. |
| `PV mV` | Photovoltaic voltage in millivolts. |
| `PV mA` | Photovoltaic current in milliamperes. |
| `PV mW` | Photovoltaic power in milliwatts. |
| `PV mJ (Epoch)` | Photovoltaic energy harvested during the epoch in millijoules. |
| `RSSI(dBm)` | Received signal strength indicator in dBm. |
| `MPPT Epoch Uptime (s)` | Maximum power point tracking uptime during the epoch in seconds. |
| `Epoch TX Packets` | Number of packets transmitted by the node during the epoch. |
| `Epoch RX Packets` | Number of packets received during the epoch. |
| `Epoch PRR` | Packet reception ratio for the epoch. |
| `Epoch TX Bytes` | Number of bytes transmitted during the epoch. |
| `Epoch RX Bytes` | Number of bytes received during the epoch. |
| `RX Throughput (bytes/s)` | Received throughput in bytes per second. |
| `Battery Energy Start (J)` | Estimated battery energy at the beginning of the epoch in joules. |
| `Battery Energy End (J)` | Estimated battery energy at the end of the epoch in joules. |

## Example Row

```csv
Device ID,Device Slot,Event,Epoch Number,Bat mV,Bat mA,Bat mW,Bat mJ (Epoch),PV mV,PV mA,PV mW,PV mJ (Epoch),RSSI(dBm),MPPT Epoch Uptime (s),Epoch TX Packets,Epoch RX Packets,Epoch PRR,Epoch TX Bytes,Epoch RX Bytes,RX Throughput (bytes/s),Battery Energy Start (J),Battery Energy End (J)
901564800F9C,64,telemetry,1,3317.0,14.0,46.44,1393.14,1190.0,3.0,3.57,107.1,-69,30,25.0,2.0,0.08,39615.0,3169.2,211.28,6912.0,6907.1
```

## Processing Selected Columns

The repository includes `data_process.py`, a simple preprocessing script for extracting selected columns from all node CSV files.

The script:

1. Finds all `.csv` files in the input folder.
2. Keeps only the columns listed in `COLUMNS_TO_KEEP`.
3. Checks whether the `Device ID` in the CSV matches the device ID in the filename.
4. Fixes mismatched `Device ID` values in the output file.
5. Saves the processed files into a `dataset/` folder.

To run the script:

```bash
python data_process.py
```

## Selecting Specific Columns

Users can customize the preprocessing step by editing the `COLUMNS_TO_KEEP` list in `data_process.py`.

For example, to keep only battery and packet reception information:

```python
COLUMNS_TO_KEEP = [
    "Device ID",
    "Epoch Number",
    "Bat mV",
    "Bat mA",
    "Bat mW",
    "Epoch TX Packets",
    "Epoch RX Packets",
    "Epoch PRR",
]
```

To keep photovoltaic and wireless link measurements:

```python
COLUMNS_TO_KEEP = [
    "Device ID",
    "Epoch Number",
    "PV mV",
    "PV mA",
    "PV mW",
    "PV mJ (Epoch)",
    "RSSI(dBm)",
]
```

If a selected column is missing from a file, the script skips that file and prints the missing column names.

## Citation

If you use this dataset in academic work, please cite the associated paper or repository:

```bibtex
@misc{uav_telemetry,
  title        = {UAV-Telemetry: UAV-Assisted Wireless Sensor Node Telemetry Dataset},
  author       = {K M Rumman, Sai Harsha Nimmagadda and Eirini Eleni Tsiropoulou},
  year         = {2026},
  howpublished = {\url{https://github.com/eetsirop/UAV-Telemetry}},
  note         = {{P}erformance and Resource Optimization in Networks (PROTON) Lab}
}
```

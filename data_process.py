import os
import glob
import pandas as pd

# Select the columns you want to keep
COLUMNS_TO_KEEP = [
    # Example:
    "Device ID",
    "Device Slot",
    "Event",
    "Epoch Number",
    "Bat mV",
    "Bat mA",
    "Bat mW",
    "Bat mJ (Epoch)",
    "PV mV",
    "PV mA",
    "PV mW",
    "PV mJ (Epoch)",
    "RSSI(dBm)",
    "MPPT Epoch Uptime (s)",
    "Epoch TX Packets",
    "Epoch RX Packets",
    "Epoch PRR",
    "Epoch TX Bytes",
    "Epoch RX Bytes",
    "RX Throughput (bytes/s)",
    "Battery Energy Start (J)",
    "Battery Energy End (J)",


]

# Input and Output folders
INPUT_FOLDER = "."
OUTPUT_FOLDER = "dataset"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def device_id_from_filename(csv_file):
    """Return the device id from filenames like node_data_9015648008E4.csv."""
    filename = os.path.splitext(os.path.basename(csv_file))[0]
    prefix = "node_data_"

    if filename.startswith(prefix):
        return filename[len(prefix):]

    return None

def normalize_device_id(value):
    """Normalize CSV device ids so text and float-looking values compare cleanly."""
    if pd.isna(value):
        return ""

    value = str(value).strip()

    if value.endswith(".0"):
        value = value[:-2]

    return value

# Find all CSV files
csv_files = sorted(glob.glob(os.path.join(INPUT_FOLDER, "*.csv")))

print(f"Found {len(csv_files)} CSV files.\n")

processed = 0

for csv_file in csv_files:
    try:
        # Read CSV
        df = pd.read_csv(csv_file)

        # Number of rows
        num_rows = len(df)

        # Keep selected columns
        if len(COLUMNS_TO_KEEP) > 0:
            missing_columns = [col for col in COLUMNS_TO_KEEP if col not in df.columns]

            if missing_columns:
                print(f"Skipping {os.path.basename(csv_file)}")
                print(f"Missing columns: {missing_columns}\n")
                continue

            df = df[COLUMNS_TO_KEEP]

        # Fix Device ID values that do not match the device id in the filename
        expected_device_id = device_id_from_filename(csv_file)

        if expected_device_id and "Device ID" in df.columns:
            current_device_ids = df["Device ID"].map(normalize_device_id).unique()
            mismatched_device_ids = [
                device_id
                for device_id in current_device_ids
                if device_id != expected_device_id
            ]

            if mismatched_device_ids:
                print(f"Device ID mismatch in {os.path.basename(csv_file)}")
                print(f"Expected Device ID: {expected_device_id}")
                print(f"Found Device ID(s): {mismatched_device_ids}")
                print("Fixed Device ID column in output.\n")

            df["Device ID"] = expected_device_id

        # Output filename
        output_path = os.path.join(
            OUTPUT_FOLDER,
            os.path.basename(csv_file)
        )

        # Save modified CSV
        df.to_csv(output_path, index=False)

        # Print information
        print(f"File : {os.path.basename(csv_file)}")
        print(f"Rows : {num_rows}")
        # print(f"Saved: {output_path}")

        processed += 1

    except Exception as e:
        print(f"Error processing {csv_file}")
        print(e)
        print("-" * 50)

print(f"Total CSV files found: {len(csv_files)}")
print(f"Successfully processed: {processed}")
print(f"Output folder: {OUTPUT_FOLDER}")

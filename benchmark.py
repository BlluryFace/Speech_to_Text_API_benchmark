import csv
import os
import re
import string
from collections import defaultdict
from pathlib import Path


from jiwer import wer

root_path = Path('./transcriptions')
def processing(file_path: Path) -> str:
    with (open(file_path, "r") as f):
        text = f.read()
        text = re.sub(r'\bdot\b', ' ', text)
        text = text.lower()
        text = text.translate(str.maketrans({p: ' ' for p in string.punctuation}))
        text = re.sub(r'\s+', ' ', text).strip()
    return text


def benchmark(text: str, reference_path: str) -> float:
    with open(reference_path, "r") as f:
        reference = f.read()

    return wer(reference, text)

if __name__ == "__main__":
    results = defaultdict(dict)
    run_ids = set()
    for folder in root_path.iterdir():
        if folder.is_dir():
            model_name = folder.name
            for file in folder.iterdir():
                filename = os.path.splitext(os.path.basename(file))[0]
                run_id = filename.replace('_transcription',
                                          '')
                reference_file = f"./references/{run_id}_reference.txt"

                if reference_file:
                    error = benchmark(processing(file), reference_file)
                    print()
                    results[model_name][run_id] = round(error, 4)
                    run_ids.add(run_id)
                else:
                    print(f"Missing reference file for: {file}")

    # Sort run IDs and map to numbers
    sorted_run_ids = sorted(run_ids)
    run_id_to_number = {run_id: str(i + 1) for i, run_id in enumerate(sorted_run_ids)}

    # Write to CSV
    with open("wer_results2.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Use numbers instead of actual run IDs
        writer.writerow(["Model"] + list(run_id_to_number.values()))

        for model, model_errors in sorted(results.items()):
            row = [model] + [model_errors.get(run_id, "") for run_id in
                             sorted_run_ids]
            writer.writerow(row)

    print(f"✅ WER results saved to wer_results2.csv")
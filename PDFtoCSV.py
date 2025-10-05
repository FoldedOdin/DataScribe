"""
Universal PDF to CSV Extractor
Author: Karthik K Pradeep
Description:
Extracts tabular data from any PDF and exports as CSV.
Handles messy tables, missing columns, and PDFs without tables.
"""

import os
import re
import pandas as pd
import camelot
from PyPDF2 import PdfReader
from datetime import datetime

# ===== CONFIG =====
INPUT_DIR = "C:\\PROJECT\\PDF to CSV\\PDF"
OUTPUT_FILE = "merged_dataset.csv"
TEMP_DIR = "temp_csvs"
LOG_FILE = "extraction_log.txt"

os.makedirs(TEMP_DIR, exist_ok=True)

# Optional: default target columns
TARGET_COLS = ["Turbidity", "Temperature", "pH", "TDS"]

# ===== HELPER FUNCTIONS =====
def extract_year_from_name(filename: str) -> str:
    match = re.search(r"(20[1-2][0-9])", filename)
    return match.group(1) if match else "Unknown"

def log_error(message):
    with open(LOG_FILE, "a", encoding="utf-8") as logf:
        logf.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def extract_tables_from_pdf(pdf_path: str):
    """
    Extract tables using Camelot.
    Fallback to PyPDF2 text extraction if no tables detected.
    """
    tables = []
    try:
        camelot_tables = camelot.read_pdf(pdf_path, pages="all", flavor="lattice")
        if not camelot_tables:
            camelot_tables = camelot.read_pdf(pdf_path, pages="all", flavor="stream")

        if camelot_tables:
            for t in camelot_tables:
                df = t.df
                if not df.empty:
                    tables.append(df)
    except Exception as e:
        log_error(f"⚠️ Camelot failed for {pdf_path}: {e}")

    # Fallback: extract raw text if no tables found
    if not tables:
        try:
            reader = PdfReader(pdf_path)
            text_rows = []
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    for line in text.splitlines():
                        row = [x.strip() for x in line.split() if x.strip()]
                        if row:
                            text_rows.append(row)
            if text_rows:
                df = pd.DataFrame(text_rows)
                tables.append(df)
        except Exception as e:
            log_error(f"⚠️ PyPDF2 text extraction failed for {pdf_path}: {e}")

    return tables

def clean_and_impute(df: pd.DataFrame):
    """
    Clean numeric columns and try to keep only TARGET_COLS if they exist.
    """
    if df.empty:
        return pd.DataFrame()

    # Flatten headers
    df.columns = [str(c).strip().replace("\n", " ") for c in df.columns]
    # Keep only numeric columns
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Optional: keep only TARGET_COLS if they exist
    keep_cols = [c for c in TARGET_COLS if c in df.columns]
    if keep_cols:
        df = df[keep_cols]

    return df

def safe_save(df, pdf_name, idx, year):
    fname = f"{os.path.splitext(pdf_name)[0]}_{year}_{idx}.csv"
    path = os.path.join(TEMP_DIR, fname)
    df.to_csv(path, index=False)
    return path

# ===== MAIN PIPELINE =====
all_data = []
errors = []

pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]
print(f"🔍 Found {len(pdf_files)} PDFs")

for pdf in pdf_files:
    pdf_path = os.path.join(INPUT_DIR, pdf)
    year = extract_year_from_name(pdf)
    print(f"\n📘 Processing {pdf} (Year: {year})")

    try:
        tables = extract_tables_from_pdf(pdf_path)
        if not tables:
            raise ValueError("No tables/text extracted.")

        for i, tbl in enumerate(tables):
            cleaned = clean_and_impute(tbl)
            if cleaned.empty:
                continue
            cleaned["Year"] = year
            safe_save(cleaned, pdf, i, year)
            all_data.append(cleaned)

        print(f"✅ {len(tables)} tables processed from {pdf}")

    except Exception as e:
        err_msg = f"❌ Failed {pdf}: {e}"
        print(err_msg)
        log_error(err_msg)
        errors.append(pdf)

# ===== MERGE & EXPORT =====
if all_data:
    merged = pd.concat(all_data, ignore_index=True)
    merged.to_csv(OUTPUT_FILE, index=False)
    print(f"\n💾 Saved merged dataset: {OUTPUT_FILE} ({len(merged)} rows)")
else:
    print("❌ No valid data extracted from PDFs.")

if errors:
    print("\n⚠️ PDFs failed:")
    for e in errors:
        print("  -", e)

print("\n✅ Extraction complete. Check 'extraction_log.txt' for details.")

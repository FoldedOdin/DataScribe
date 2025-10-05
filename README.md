<div align="center">

# DATASCRIBE

**Universal PDF to CSV Extractor**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.md)
[![Python](https://img.shields.io/badge/Python-3.6+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](https://github.com/FoldedOdin/DataScribe)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/FoldedOdin/DataScribe)

**Author:** Karthik K Pradeep

</div>

## 🌟 About

A **Python script designed to automatically extract tabular data** from multiple PDF files and consolidate it into a single, clean CSV file. Built to be robust, handling various PDF layouts, messy tables, and even PDFs that don't contain structured tables by falling back to raw text extraction.

**Perfect for data science and analysis projects where source data is locked away in PDF reports.**

## ✨ Features

### 📦 Bulk Processing
- **🔄 Batch Extraction** - Process all PDFs in a directory at once
- **⚡ Automated Pipeline** - Set it and forget it processing
- **📁 Directory Scanning** - Automatically finds all PDF files

### 🧠 Intelligent Extraction
- **🎯 Smart Table Detection** - Uses camelot-py for accurate parsing
- **🔀 Dual Method Approach** - Tries both 'lattice' and 'stream' flavors
- **📊 Layout Agnostic** - Handles various PDF table formats

### 🛡️ Fallback Mechanism
- **📝 Text Extraction** - Falls back to PyPDF2 when tables aren't found
- **🔧 Structure Attempt** - Tries to organize raw text into columns
- **✅ Never Fails Empty** - Always extracts something useful

### 🧹 Data Cleaning
- **🔢 Type Conversion** - Automatically converts to numeric types
- **🗑️ Handles Noise** - Manages non-numeric values gracefully
- **📋 Column Filtering** - Keep only the columns you need
- **🎯 Standardization** - Cleans and normalizes column names

### 📅 Temporal Context
- **🗓️ Year Extraction** - Automatically extracts year from filenames
- **📊 Time Series Ready** - Adds temporal dimension to your data
- **🔍 Pattern Recognition** - Finds four-digit years in any filename format

### 🔍 Robust Logging
- **📝 Error Tracking** - Logs all errors with timestamps
- **🐛 Easy Debugging** - Identifies problematic files quickly
- **📊 Processing Summary** - Shows success/failure statistics

### 📂 Organized Output
- **💾 Intermediate Files** - Saves CSV for each extracted table
- **📊 Merged Dataset** - Combines all data into single file
- **🗂️ Clean Structure** - Organized temporary directory

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

**Core Libraries:**

![Camelot](https://img.shields.io/badge/Camelot-PDF%20Extraction-orange?logo=python&logoColor=white)
![PyPDF2](https://img.shields.io/badge/PyPDF2-Text%20Extraction-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white)

</div>

## 🔄 How It Works

DataScribe follows a sophisticated multi-step pipeline:

### 📊 Processing Pipeline

```
1. 🔍 Scan PDFs → 2. 📄 Extract Tables → 3. 🧹 Clean Data → 4. 💾 Save CSVs → 5. 🔗 Merge All
```

### Detailed Workflow

**Step 1: PDF Discovery**
- Scans `INPUT_DIR` for all `.pdf` files
- Creates list of files to process

**Step 2: Data Extraction**
For each PDF file:
- 📅 **Extract Year**: Parses filename for four-digit year (e.g., 2021)
- 📊 **Extract Tables**: Uses camelot with both 'lattice' and 'stream' methods
- 📝 **Fallback to Text**: If camelot fails, uses PyPDF2 for raw text extraction

**Step 3: Data Processing**
Each extracted table undergoes:
- 🧹 Column cleaning and standardization
- 🔢 Numeric type conversion
- 🎯 Filtering to retain only `TARGET_COLS`
- 📅 Addition of extracted 'Year' column

**Step 4: Intermediate Storage**
- 💾 Each cleaned table saved as separate CSV
- 📁 Stored in `temp_csvs` directory
- 🏷️ Named with source PDF and table index

**Step 5: Final Consolidation**
- 🔗 Concatenates all temporary CSVs
- 📊 Creates master file: `merged_dataset.csv`
- 📝 Logs any errors to `extraction_log.txt`

## 🚀 Getting Started

### 📋 Prerequisites

Before you begin, ensure you have:

- ![Python](https://img.shields.io/badge/Python-3.6+-3776AB?logo=python&logoColor=white) (v3.6 or higher)
- ![Ghostscript](https://img.shields.io/badge/Ghostscript-Required-purple.svg) (system dependency)

### ⚡ Installation

#### Step 1: Install System Dependencies (Ghostscript)

Camelot requires Ghostscript to be installed on your system.

<details>
<summary><b>🪟 Windows Installation</b></summary>

1. Download the installer from [Ghostscript website](https://www.ghostscript.com/download/gsdnld.html)
2. Run the installer and follow the setup wizard
3. Verify installation:
```bash
gs --version
```

</details>

<details>
<summary><b>🍎 macOS Installation (Homebrew)</b></summary>

```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Ghostscript
brew install ghostscript

# Verify installation
gs --version
```

</details>

<details>
<summary><b>🐧 Linux Installation (Debian/Ubuntu)</b></summary>

```bash
# Update package list
sudo apt-get update

# Install Ghostscript
sudo apt-get install ghostscript

# Verify installation
gs --version
```

</details>

#### Step 2: Install Python Libraries

Install all required Python packages:

```bash
pip install pandas "camelot-py[cv]" PyPDF2
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### ⚙️ Configuration

Open `PDFtoCSV.py` and modify the CONFIG section:

```python
# ===== CONFIG =====
INPUT_DIR = "path/to/your/pdf/folder"  # Your PDF directory
OUTPUT_FILE = "merged_dataset.csv"      # Final output filename
TEMP_DIR = "temp_csvs"                  # Temporary CSV storage
LOG_FILE = "extraction_log.txt"         # Error log file

# Optional: Specify columns to keep (leave empty for all)
TARGET_COLS = ["Turbidity", "Temperature", "pH", "TDS"]
```

### 📖 Usage

1️⃣ **Prepare your PDFs**: Place all PDF files in your `INPUT_DIR`

2️⃣ **Run the script**:

```bash
python PDFtoCSV.py
```

3️⃣ **Check results**: Find your consolidated data in `merged_dataset.csv`

### Example Output

```bash
Processing: report_2021.pdf
  ✓ Found 2 tables
  ✓ Extracted year: 2021
  ✓ Saved: report_2021_2021_0.csv
  ✓ Saved: report_2021_2021_1.csv

Processing: data_2022.pdf
  ✓ Found 1 table
  ✓ Extracted year: 2022
  ✓ Saved: data_2022_2022_0.csv

=================================
Extraction Complete!
=================================
✓ PDFs processed: 2
✓ Tables extracted: 3
✓ Output file: merged_dataset.csv
✗ Failed files: 0
📝 Check extraction_log.txt for details
```

## 🏗️ Project Structure

```
📦 DataScribe/
├── 📄 PDFtoCSV.py                 # Main extraction script
├── 📄 requirements.txt            # Python dependencies
├── 📄 extraction_log.txt          # Error log (generated)
├── 📊 merged_dataset.csv          # Final output (generated)
├── 📁 your_pdf_folder/            # Input PDFs
│   ├── 📄 report_2021.pdf
│   ├── 📄 data_2022.pdf
│   └── 📄 results_2023.pdf
├── 📁 temp_csvs/                  # Intermediate CSVs (generated)
│   ├── 📄 report_2021_2021_0.csv
│   ├── 📄 report_2021_2021_1.csv
│   ├── 📄 data_2022_2022_0.csv
│   └── 📄 results_2023_2023_0.csv
├── 📄 LICENSE                     # MIT License
└── 📄 README.md                   # You are here
```

## ⚙️ Advanced Configuration

### Custom Column Mapping

```python
# Map PDF column names to standard names
COLUMN_MAPPING = {
    "Temp (°C)": "Temperature",
    "Turb (NTU)": "Turbidity",
    "pH Level": "pH"
}
```

### Filtering Options

```python
# Keep specific columns
TARGET_COLS = ["Temperature", "pH", "TDS"]

# Or keep all columns (empty list)
TARGET_COLS = []
```

### Extraction Methods

```python
# Prioritize lattice method (for bordered tables)
METHODS = ['lattice', 'stream']

# Or try stream first (for borderless tables)
METHODS = ['stream', 'lattice']
```

## 🔧 Troubleshooting

### Common Issues

<details>
<summary><b>❌ "Ghostscript not found" error</b></summary>

**Solution**: Make sure Ghostscript is installed and accessible in your system PATH.

**Verify installation**:
```bash
gs --version
```

If not found, reinstall Ghostscript and restart your terminal.

</details>

<details>
<summary><b>❌ "No module named 'camelot'" error</b></summary>

**Solution**: Install camelot with CV support:
```bash
pip install "camelot-py[cv]"
```

</details>

<details>
<summary><b>⚠️ No tables extracted from PDF</b></summary>

**Possible causes**:
- PDF contains only images (scanned documents)
- Tables have complex layouts
- PDF is password-protected

**Solutions**:
- Use OCR for scanned PDFs (pytesseract)
- Try adjusting camelot flavor settings
- Remove password protection first

</details>

<details>
<summary><b>⚠️ Incorrect data extraction</b></summary>

**Solution**: Check `temp_csvs` folder to see intermediate results. Adjust:
- Column filtering in `TARGET_COLS`
- Extraction method priority
- Data cleaning rules

</details>

<details>
<summary><b>🐌 Slow processing speed</b></summary>

**Solution**: Processing speed depends on:
- PDF complexity and size
- Number of tables per PDF
- System resources

Consider processing in batches for large datasets.

</details>

## 📊 Example Use Cases

### Research Data Collection
```bash
# Extract water quality data from monthly reports
TARGET_COLS = ["Date", "pH", "Temperature", "Turbidity", "DO"]
INPUT_DIR = "water_quality_reports/"
```

### Financial Data Analysis
```bash
# Extract quarterly financial metrics
TARGET_COLS = ["Quarter", "Revenue", "Expenses", "Profit"]
INPUT_DIR = "financial_reports/"
```

### Scientific Data Mining
```bash
# Extract experimental results from publications
TARGET_COLS = ["Sample", "Measurement", "Result", "Error"]
INPUT_DIR = "research_papers/"
```

## 🧪 Testing

Test with sample PDFs first:

```bash
# Create test directory
mkdir test_pdfs
cp sample_*.pdf test_pdfs/

# Update config
INPUT_DIR = "test_pdfs"

# Run script
python PDFtoCSV.py

# Verify output
head merged_dataset.csv
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

<div align="center">

[![Issues](https://img.shields.io/github/issues/yourusername/datascribe)](https://github.com/yourusername/datascribe/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/yourusername/datascribe)](https://github.com/yourusername/datascribe/pulls)

</div>

### How to Contribute

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 📥 Open a Pull Request

## 📝 Roadmap

- [ ] Support for scanned PDFs (OCR integration)
- [ ] GUI interface for easier configuration
- [ ] Multi-language support for international documents
- [ ] Cloud storage integration (Google Drive, Dropbox)
- [ ] Real-time progress bar during extraction
- [ ] Support for Excel and Word documents
- [ ] Automated data validation and quality checks
- [ ] Docker container for easy deployment

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE.md) file for details.

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

## 🙏 Acknowledgments

<div align="center">

Special thanks to these amazing projects:

[![Python](https://img.shields.io/badge/Thanks-Python%20Community-3776AB?logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Thanks-Pandas%20Team-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Camelot](https://img.shields.io/badge/Thanks-Camelot%20Developers-orange?logo=python&logoColor=white)](https://camelot-py.readthedocs.io)

</div>

## 📬 Connect With Author

<div align="center">

**Karthik K Pradeep**

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?logo=github&logoColor=white)](https://github.com/FoldedOdin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/karthikkpradeep)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?logo=gmail&logoColor=white)](mailto:karthikkpradeep123@gmail.com)

</div>

## 🆘 Support

Need help with DataScribe?

- 💬 **Issues**: [Open an issue](https://github.com/FoldedOdin/DataScribe/issues)
- 📖 **Wiki**: [Documentation](https://github.com/FoldedOdin/DataScribe/wiki)

---

<div align="center">

**🎯 Built with ❤️ for data scientists and analysts**

![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-💙-blue.svg)
![Python](https://img.shields.io/badge/Python-💛-yellow.svg)

### ⭐ If you found this project helpful, please give it a star!

[![🚀 Return To TOP](https://img.shields.io/badge/🚀%20Return%20to-%20TOP-FF6B6B?style=for-the-badge&labelColor=4ECDC4)](#datascribe)

</div>

Markdown
# Excel & CSV Data Cleaner 🧹✨

A powerful, automated Python script built with **Pandas** and **OpenPyXL** designed to handle real-world messy data. This tool diagnostics datasets for duplicates and missing values, applies necessary preprocessing steps, and exports a perfectly structured, clean dataset.

---

## 🚀 Features

- **Automated Duplicity Check:** Identifies and removes redundant/duplicate entries from the dataset to maintain data integrity.
- **Smart Missing Value Imputation:** Detects missing (NaN) cells across all columns and safely replaces them with structured placeholders (`'Unknown'`).
- **Data Integrity Validation:** Compares "Before" and "After" diagnostic shapes to verify a 100% clean data execution.
- **Auto-Export:** Seamlessly generates and saves the cleaned output into a new production-ready `.csv` file.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** Pandas, OpenPyXL

---

## 📦 How to Run This Project Local

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/siyakumari-19/Excel-Data-Cleaner.git](https://github.com/siyakumari-19/Excel-Data-Cleaner.git)
   cd Excel-Data-Cleaner
Install the dependencies:

Bash
pip install pandas openpyxl
Place your messy data file (trx-10k.csv) inside the project root folder.

Execute the automated cleaning script:

Bash
python Cleaner.py
📊 Sample Output Preview
Plaintext
--- BEFORE CLEANING ---
Data Size: (10000, 6)
Duplicate rows found: 14
Missing values per column:
type         311
card_type    116

--- AFTER CLEANING ---
Missing values now: 0

Success! Cleaned data saved as 'cleaned_trx.csv'

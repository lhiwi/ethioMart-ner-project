```markdown
# EthioMart Amharic NER

**Transform Telegram e-commerce chatter into structured data for vendor scoring and micro-lending.**


## 🚀 Project Overview

This repository implements a pipeline to:

1. **Ingest** messages (text, images) from Ethiopian Amharic-language Telegram channels  
2. **Preprocess** and clean raw text for NER tasks  
3. **Label**, **fine-tune**, and **interpret** transformer-based NER models  
4. **Generate** vendor scorecards for EthioMart’s micro-lending

Task 1 (Data Ingestion & Preprocessing) is complete on the `task-1` branch. See [notebooks/01_data_ingestion.ipynb] and [scripts/ingest_data.py] for details.


## 📁 Repository Structure

```

ethioMart-ner/
├── .github/                 # CI workflows (Python-CI)
├── .vscode/                 # VS Code settings (auto-format, Jupyter)
├── data/
│   ├── raw/                 # ingested CSVs & media
│   └── processed/           # downstream artifacts
├── notebooks/               # Colab & Jupyter prototypes
│   └── 01\_data\_ingestion.ipynb
├── scripts/                 # automated entry-points
│   └── ingest\_data.py
├── src/                     # core modules
│   ├── telegram\_scraper.py
│   └── preprocessing.py
├── tests/                   # pytest unit tests
├── channels\_to\_crawl.xlsx   # list of Telegram channels
├── requirements.txt         # pinned dependencies
└── README.md                # project overview & setup

````

##  Installation & Setup

1. **Clone & enter** the repo  
   ```bash
   git clone https://github.com/lhiwi/ethioMart-ner-project.git
   cd ethioMart-ner-project
````

2. **Create & activate** a virtual environment

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install** dependencies

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Configure** Telegram credentials

   * Copy your **API ID** & **API Hash** from \[my.telegram.org → API Development Tools]
   * Create a `.env` in project root:

     ```ini
     TELEGRAM_API_ID=YOUR_API_ID
     TELEGRAM_API_HASH=YOUR_API_HASH
     ```
   * (Optional) export them in your shell:

     ```powershell
     $env:TELEGRAM_API_ID="…"
     $env:TELEGRAM_API_HASH="…"
     ```


##  Usage

### Interactive prototype (Colab or Jupyter)

```bash
# on task-1 branch:
git checkout task-1
# open in VS Code:
code notebooks/01_data_ingestion.ipynb
# or in Colab:
start "https://colab.research.google.com/github/lhiwi/ethioMart-ner-project/blob/task-1/notebooks/01_data_ingestion.ipynb"
```
### Automated ingestion

```bash
# ensure .env is set or environment vars exported
python -m scripts.ingest_data
# produces data/raw/telegram_data.csv
```

##  Next Steps

* **Task 2**: Label cleaned text in CoNLL format
* **Task 3**: Fine-tune multilingual transformers for Amharic NER
* **Task 4**: Compare, interpret, and select the best model
* **Task 5**: Build vendor scorecards for micro-lending

---

## 📝 License & Credits

This project is part of the 10 Academy: Artificial Intelligence Mastery curriculum, guided by Mahlet, Rediet, Kerod, and Rehmet.

```
```

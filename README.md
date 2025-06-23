# EthioMart Amharic NER

**Transform Telegram e-commerce chatter into structured data for vendor scoring and micro-lending.**

##  Project Overview

This repository implements a pipeline to:

1. **Ingest** messages (text, images) from Ethiopian Amharic-language Telegram channels  
2. **Preprocess** and clean raw text for NER tasks  
3. **Label**, **fine-tune**, and **interpret** transformer-based NER models  
4. **Generate** vendor scorecards for EthioMart’s micro-lending  


## Progress to Date

- **Task 1: Data Ingestion & Preprocessing**  
  We selected five representative Telegram channels and streamed 500 messages from each, producing a 2,500-row dataset with metadata (`date`, `sender`, `views`, `channel`) and raw text. A custom `clean_text()` function removed non-Amharic characters and noise, reducing average message length by 12.5 %. The entire pipeline was encapsulated in `scripts/ingest_data.py`, yielding a reproducible `data/raw/telegram_data.csv`.

- **Task 2: CoNLL Labeling**  
  From the cleaned corpus, we sampled 50 messages, tokenized them using NLTK’s `WordPunctTokenizer`, and generated a CoNLL template. In VS Code, each token was annotated with `B-Product`/`I-Product`, `B-PRICE`/`I-PRICE`, and `B-LOC`/`I-LOC` tags, producing `data/raw/labels_sample.conll`. Annotation was verified by reloading in Colab to ensure proper formatting and coverage.

These completed tasks establish a high-quality dataset and annotation set, ready for Task 3: fine-tuning a transformer-based NER model.


##  Future Work

- **Task 3: Model Fine-Tuning**  
  Convert `labels_sample.conll` into a Hugging Face `datasets` object, align token-level labels with an XLM-RoBERTa tokenizer, and fine-tune for Amharic NER.

- **Expand Annotation**  
  Increase manual labeling from 50 to 200–500 messages to improve model robustness and domain coverage.

- **Media & Metadata Ingestion**  
  Extend the scraper to download images and documents into `data/raw/media/`, and capture additional metadata (e.g., replies, forwards) for richer feature engineering.

- **Model Comparison & Interpretability**  
  Evaluate multiple transformer variants (mBERT, DistilBERT) and apply SHAP/LIME to explain model decisions and ensure trust.

- **Vendor Scorecard Development**  
  Combine NER outputs with engagement metrics (views, posting frequency) to compute lending scores and generate vendor profiles for micro-lending decisions.


##  Repository Structure

```
ethioMart-ner/
├── .github/                 # CI workflows (Python-CI)
├── .vscode/                 # VS Code settings
├── data/
│   ├── raw/                 # telegram\_data.csv, labels\_sample.conll, media/
│   └── processed/           # downstream artifacts
├── notebooks/               # Colab & Jupyter prototypes
│   ├── 01\_data\_ingestion.ipynb
│   └── labeling.ipynb
├── scripts/                 # automated entry-points
│   └── ingest\_data.py
├── src/                     # core modules
│   ├── telegram\_scraper.py
│   └── preprocessing.py
├── tests/                   # pytest unit tests
├── channels\_to\_crawl.xlsx   # list of Telegram channels
├── requirements.txt         # pinned dependencies
└── README.md                # project overview & setup

```

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


## Usage

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






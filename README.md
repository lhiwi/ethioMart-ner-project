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
- **Task 3: Fine-Tuning NER Models**  
- Loaded CoNLL annotations into a Hugging Face `Dataset`.  
- Token-aligned labels with the `rasyosef/bert-tiny-amharic` model.  
- Trained for 5 epochs on our 50-message set; observed zero training loss and evaluated on validation split.  
- Saved the fine-tuned model under `models/final_ner_model/` and downloaded locally.

- **Task 4: Model Comparison & Selection**  
- Benchmarked four models:  
  - `bert-tiny-amharic`  
  - `xlm-roberta-base`  
  - `distilbert-base-multilingual-cased`  
  - `bert-base-multilingual-cased` (mBERT)  
- Fine-tuned each for 3 epochs on the same dataset.  
- Due to limited sample size, all F1 scores were zero. We therefore compared **training runtime** as a proxy for efficiency.  
- Plotted training times and selected the fastest model (e.g., `bert-tiny-amharic`) for production deployment.



##  Future Work

- **Task 5: Model Interpretability**  
  Apply SHAP and LIME to explain token-level predictions and build trust in NER outputs.

- **Task 6: Vendor Scorecard**  
  Combine NER-extracted entities with engagement metrics (views, posting frequency) to compute lending scores and visualize vendor rankings.


##  Repository Structure

```
ethioMart-ner/
├── .github/
├── .vscode/
├── data/
│ ├── raw/
│ │ ├── telegram_data.csv
│ │ └── labels_sample.conll
│ └── processed/
├── models/
│ └── final_ner_model/
├── notebooks/
│ ├── 01_data_ingestion.ipynb
│ ├── labeling.ipynb
│ ├── 03_fine_tune_ner.ipynb
│ └── 04_model_comparison.ipynb
├── scripts/
│ ├── ingest_data.py
│ └── vendor_scorecard.py
├── src/
│ ├── telegram_scraper.py
│ └── preprocessing.py
├── tests/
├── channels_to_crawl.xlsx
├── requirements.txt
└── README.md
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






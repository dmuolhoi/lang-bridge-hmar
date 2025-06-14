# Hmar Phrase Translator

A lightweight Python tool for translating **Hmar phrases** into English using a word-level + phrase-level dataset mapping system.

---

## Why This Exists

Hmar is an underrepresented language with very limited digital resources. Direct word-to-word translation often leads to unnatural or incorrect results due to context-specific meaning.

This project solves that by:
- Mapping **individual Hmar words** to a value and literal translation.
- Mapping **phrases as sequences of word values** to natural English translations.
- Allowing smart lookup by combining both levels.

---

## Project Structure

```
.
├── word_dataset.csv         # Contains words and their literal English meaning
├── phrase_dataset.csv       # Contains full phrase value sequences and proper translations
├── translator.py            # Python script that powers the lookup
└── README.md                # You're reading this
```

---

## Dataset Format

### 1. `word_dataset.csv`

| val   | word   | literal_en |
|--------|--------|-------------|
| 11001 | iem    | what        |
| 11002 | i      | you         |
| 11003 | thaw   | do/doing    |

- `val`: Unique ID for the word  
- `word`: Hmar word  
- `literal_en`: Basic/isolated translation  

---

### 2. `phrase_dataset.csv`

| val_sequence       | phrase_hmar        | phrase_en             |
|--------------------|--------------------|------------------------|
| 11001-11002-11003  | iem i thaw         | what are you doing?   |

- `val_sequence`: Hyphen-separated `val`s from the word dataset (in order of appearance)  
- `phrase_hmar`: Original Hmar phrase  
- `phrase_en`: Full, natural English translation  

---

## How to Run

Make sure you have Python 3 installed.

```bash
python translator.py
```

Then enter a Hmar phrase like:

```
iem i thaw?
```

---

## Features

- Removes punctuation like `?`, `.` before lookup
- Displays:
  - Each word's literal translation
  - Final phrase-level English meaning (if matched)
- Shows “Not Found” if a word or phrase doesn’t exist yet in the dataset

---

## Example Output

```
🗣️ Enter a Hmar phrase: iem i thaw?

Word-Level Lookup:
- iem → what (val: 11001)
- i → you (val: 11002)
- thaw → do/doing (val: 11003)

Constructed Value Sequence: 11001-11002-11003

Phrase-Level Lookup:
- Original Phrase: iem i thaw
- English Translation: what are you doing?
```

---

## Roadmap

- [ ] Add more words and phrases  
- [ ] Support fuzzy word matching  
- [ ] GUI or mobile frontend  
- [ ] Handle synonyms/context better  

---

## Credits

Built by [dmuolhoi]  
Inspired by the need for proper Hmar digital language tools.
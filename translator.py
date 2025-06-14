import csv
import string

# Clean and normalize the input phrase
def clean_phrase(phrase):
    return phrase.translate(str.maketrans('', '', string.punctuation)).lower().strip()
   
# Load word dataset into a dictionary: word -> (val, literal_en)
def load_word_dataset(path):
    word_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            word_dict[row['word'].strip()] = {
                'val': row['val'].strip(),
                'literal_en': row['literal_en'].strip()
            }
    return word_dict

# Load phrase dataset into a dictionary: val_sequence -> (phrase_hmar, phrase_en)
def load_phrase_dataset(path):
    phrase_dict = {}
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            phrase_dict[row['val_sequence'].strip()] = {
                'phrase_hmar': row['phrase_hmar'].strip(),
                'phrase_en': row['phrase_en'].strip()
            }
    return phrase_dict

# Process input phrase
def process_input(input_phrase, word_dict, phrase_dict):
    words = input_phrase.strip().lower().split()
    val_sequence = []
    print("\nWord-Level Lookup:")

    for word in words:
        if word in word_dict:
            data = word_dict[word]
            val_sequence.append(data['val'])
            print(f"- {word} → {data['literal_en']} (val: {data['val']})")
        else:
            print(f"- {word} → Not Found")
            val_sequence.append("XXXX")  # Placeholder for missing val

    val_key = "-".join(val_sequence)
    print("\nConstructed Value Sequence:", val_key)

    print("\n Phrase-Level Lookup:")
    if val_key in phrase_dict:
        phrase_data = phrase_dict[val_key]
        print(f"- Original Phrase: {phrase_data['phrase_hmar']}")
        print(f"- English Translation: {phrase_data['phrase_en']}")
    else:
        print("- Phrase not found in dataset.")

# === USAGE ===
if __name__ == "__main__":
    word_dict = load_word_dataset("word_dataset.csv")
    phrase_dict = load_phrase_dataset("phrase_dataset.csv")

    user_input = clean_phrase(input(" Enter a Hmar phrase: "))
    process_input(user_input, word_dict, phrase_dict)
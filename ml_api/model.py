import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

DB_FILE = "document_db.pkl"

if os.path.exists(DB_FILE):
    document_db = joblib.load(DB_FILE)
else:
    document_db = {}

SIMILARITY_THRESHOLD = 0.15


def extract_text(file_path):
    text = ""
    try:
        pages = convert_from_path(file_path,
        poppler_path=r"C:\poppler-25.12.0\Library\bin")
        for page in pages:
            text += pytesseract.image_to_string(page)
    except:
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)

    return text.lower()


def find_best_category(text):
    if not document_db:
        return None, 0

    all_texts = []
    categories = []

    for cat, texts in document_db.items():
        for t in texts:
            all_texts.append(t)
            categories.append(cat)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(all_texts + [text])

    similarity = cosine_similarity(X[-1], X[:-1])[0]

    best_idx = similarity.argmax()
    best_score = similarity[best_idx]

    return categories[best_idx], best_score


def classify_document(file_path):
    global document_db

    text = extract_text(file_path)
    category, score = find_best_category(text)

    if category is None or score < SIMILARITY_THRESHOLD:
        new_category = f"new_type_{len(document_db)+1}"
        document_db[new_category] = [text]
        joblib.dump(document_db, DB_FILE)

        return {
            "category": new_category,
            "score": float(score),
            "is_new_type": True
        }

    document_db[category].append(text)
    joblib.dump(document_db, DB_FILE)

    return {
        "category": category,
        "score": float(score),
        "is_new_type": False
    }

"""
Standalone Document Payload & Link Extractor Service
"""
import io
import re
from typing import Dict, Any, List

def extract_links_from_text(text: str) -> List[str]:
    pattern = re.compile(r"http[s]?://(?:[a-zA-Z0-9$\-_.+!*'(),;:@&=/?#%])+")
    return list(set(pattern.findall(text)))

def inspect_document_payload(filename: str, file_bytes: bytes) -> Dict[str, Any]:
    ext = "." + filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    extracted_text = ""
    urls_found = []

    if ext == ".txt":
        try:
            extracted_text = file_bytes.decode("utf-8", errors="ignore")
        except Exception:
            pass
    elif ext == ".pdf":
        try:
            import pdfplumber
            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                extracted_text = "\n".join([page.extract_text() or "" for page in pdf.pages])
        except Exception:
            pass

    urls_found = extract_links_from_text(extracted_text)

    return {
        "filename": filename,
        "extension": ext,
        "size_bytes": len(file_bytes),
        "urls_count": len(urls_found),
        "urls": urls_found[:15],
        "has_suspicious_links": len(urls_found) > 0,
        "text_sample": extracted_text[:300]
    }

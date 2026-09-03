"""
Standalone NLP Social Engineering & Phishing Intent Classifier Engine
"""
import re
from typing import Dict, Any, List, Tuple

URGENCY_PATTERNS = [
    r"\bsegera\b", r"\bsekarang\b", r"\burgent\b", r"\bmendesak\b",
    r"\bjam lagi\b", r"\bdeadline\b", r"\bblokir\b", r"\bterbatas\b",
    r"\b24 jam\b", r"\b48 jam\b", r"\bsebelum terlambat\b"
]

THREAT_PATTERNS = [
    r"\bditutup\b", r"\bakan dihapus\b", r"\bdenda\b", r"\bpenalti\b",
    r"\bdisuspend\b", r"\baktivitas mencurigakan\b", r"\bdiblokir permanen\b",
    r"\bverifikasi data\b", r"\bpolisi\b", r"\bpelanggaran hukum\b"
]

REWARD_PATTERNS = [
    r"\bmenang\b", r"\bhadiah\b", r"\bgratis\b", r"\bbonus\b",
    r"\bcashback\b", r"\bgiveaway\b", r"\bjuta rupiah\b", r"\bundian\b"
]

SUSPICIOUS_PHRASES = [
    "klik link berikut", "verifikasi akun", "segera konfirmasi",
    "kata sandi", "pin atm", "kode otp", "nomor kartu", "login sekarang",
    "update data", "akun anda diblokir", "hadiah tunai", "klaim sekarang"
]

def analyze_phishing_text(text: str) -> Dict[str, Any]:
    text_lower = text.lower()
    
    urgency_hits = [p.strip(r"\b") for p in URGENCY_PATTERNS if re.search(p, text_lower)]
    threat_hits = [p.strip(r"\b") for p in THREAT_PATTERNS if re.search(p, text_lower)]
    reward_hits = [p.strip(r"\b") for p in REWARD_PATTERNS if re.search(p, text_lower)]
    phrase_hits = [phrase for phrase in SUSPICIOUS_PHRASES if phrase in text_lower]

    urgency_score = min(len(urgency_hits) * 0.25, 1.0)
    threat_score = min(len(threat_hits) * 0.30, 1.0)
    reward_score = min(len(reward_hits) * 0.25, 1.0)
    phrase_score = min(len(phrase_hits) * 0.35, 1.0)

    combined_score = min(round((urgency_score * 0.3) + (threat_score * 0.35) + (reward_score * 0.15) + (phrase_score * 0.2), 3), 1.0)
    verdict = "phishing" if combined_score >= 0.60 else ("suspicious" if combined_score >= 0.30 else "safe")

    return {
        "text_preview": text[:120],
        "urgency_score": urgency_score,
        "threat_score": threat_score,
        "reward_score": reward_score,
        "flagged_phrases": phrase_hits + urgency_hits + threat_hits + reward_hits,
        "risk_score": combined_score,
        "verdict": verdict
    }

if __name__ == "__main__":
    sample = "URGENT: Akun Bank Mandiri Anda akan diblokir dalam 24 jam! Klik link berikut untuk verifikasi kode OTP dan PIN ATM."
    print("Test NLP Analysis:", analyze_phishing_text(sample))

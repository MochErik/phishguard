"""
Standalone URL Heuristic & Threat Analyzer Service
"""
import re
import math
from typing import Dict, Any, List
from urllib.parse import urlparse, unquote

SUSPICIOUS_KEYWORDS = [
    "login", "signin", "verify", "account", "secure", "update",
    "confirm", "banking", "paypal", "apple", "google", "microsoft",
    "password", "credential", "wallet", "crypto", "winner", "prize",
    "free", "urgent", "suspended", "limited", "expire", "click",
    "bri", "bca", "mandiri", "bni", "shopee", "tokopedia", "dana", "gopay"
]

SUSPICIOUS_TLDS = {
    ".xyz", ".top", ".club", ".work", ".click", ".link", ".surf",
    ".buzz", ".cfd", ".sbs", ".rest", ".fit", ".monster", ".icu"
}

def url_entropy(url: str) -> float:
    if not url:
        return 0.0
    freq = {}
    for c in url:
        freq[c] = freq.get(c, 0) + 1
    n = len(url)
    return -sum((f / n) * math.log2(f / n) for f in freq.values())

def analyze_url_heuristics(url: str) -> Dict[str, Any]:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    path = parsed.path.lower()
    full_url = unquote(url.lower())

    has_ip = bool(re.search(r"(\d{1,3}\.){3}\d{1,3}", domain))
    entropy = url_entropy(url)
    matched_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in full_url]
    tld_risk = any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS)
    subdomain_count = domain.count(".") - 1 if domain.count(".") > 1 else 0

    score = 0.0
    if has_ip: score += 0.35
    if tld_risk: score += 0.25
    if entropy > 4.5: score += 0.20
    if len(matched_keywords) >= 2: score += 0.30
    elif len(matched_keywords) == 1: score += 0.15
    if subdomain_count >= 3: score += 0.15
    if "@" in url: score += 0.40

    risk_score = min(round(score, 3), 1.0)
    verdict = "phishing" if risk_score >= 0.65 else ("suspicious" if risk_score >= 0.35 else "safe")

    return {
        "url": url,
        "domain": domain,
        "has_ip": has_ip,
        "url_entropy": round(entropy, 3),
        "suspicious_keywords": matched_keywords,
        "subdomain_count": max(0, subdomain_count),
        "heuristic_score": risk_score,
        "verdict": verdict
    }

if __name__ == "__main__":
    test_url = "http://192.168.1.1/bca-secure-login-verify-account.xyz"
    print("Test URL Analysis:", analyze_url_heuristics(test_url))

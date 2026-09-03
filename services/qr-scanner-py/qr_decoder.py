"""
Standalone QR Code Threat Decoder Service
"""
import io
from typing import Optional, Dict, Any

def inspect_qr_data(decoded_text: str) -> Dict[str, Any]:
    is_link = decoded_text.startswith("http://") or decoded_text.startswith("https://")
    return {
        "decoded_content": decoded_text,
        "is_url": is_link,
        "type": "URL" if is_link else "RAW_TEXT",
        "length": len(decoded_text)
    }

def decode_qr_image(image_bytes: bytes) -> Optional[str]:
    try:
        from PIL import Image
        from pyzbar.pyzbar import decode
        img = Image.open(io.BytesIO(image_bytes))
        results = decode(img)
        if results:
            return results[0].data.decode("utf-8", errors="ignore")
    except Exception:
        pass
    return None

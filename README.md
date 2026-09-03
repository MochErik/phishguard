# 🛡️ PhishGuard — Enterprise AI Multi-Vector Phishing & Social Engineering Monorepo

> **Enterprise-Grade AI Multi-Vector Threat Intelligence & Social Engineering Defense Engine**  
> **UI Aesthetic**: Dark Tactical Cyber-Security Glassmorphism (`#090d16` / `#111827` / `#6366f1` / `#10b981`)  
> **Target Devices**: 100% Fit di iPhone (Termasuk iPhone 12 Mini & Dynamic Island), Android, iPad, MacBook, Laptop, & PC Widescreen  
> **Live Frontend App**: [https://mocherik.github.io/phishguard/](https://mocherik.github.io/phishguard/)  
> **Live Backend API**: [https://phishguard-api.vercel.app](https://phishguard-api.vercel.app) *(Vercel Serverless ASGI)*  
> **Author**: Moch. Erik Irriansyah (NIM 04123003 — Universitas Narotama)

---

## 🛡️ Laporan Audit Keamanan & Proteksi Sistem (Security & Threat Assessment)

Aplikasi **PhishGuard v2.0** dibangun dengan kepatuhan terhadap standar industri **OWASP Top 10 for Web Applications & API Security**, pengujian penetrasi statis (*Static Application Security Testing - SAST*), serta mekanisme mitigasi serangan rekayasa sosial mutakhir (*AI-Powered Social Engineering & Quishing Defense*).

### 📋 Matriks Hasil Pengujian Keamanan:

| Kategori Pengujian | Vektor Serangan (*Attack Vector*) | Mekanisme Pertahanan (*Security Defense*) | Status Hasil Uji |
|---|---|---|:---:|
| **Zero-Day Phishing URL** | Typosquatting, IDN Homograph Attack, Subdomain Chaining, TLD Berisiko Tinggi (`.xyz`, `.top`, `.icu`) | **Shannon Entropy Calculator & Heuristic Engine**: Menganalisis keacakan karakter, rasio subnet IP, dan pola subdomain berlapis sebelum eksekusi browser. | 🟢 **100% SAFE (PASSED)** |
| **Social Engineering NLP** | Urgensi Palsu, Ancaman Pemblokiran Rekening, Penipuan Hadiah, Pencurian OTP/PIN | **NLP Psychological Manipulation Classifier**: Deteksi kata pemicu panik (*Urgency Scorer*), ancaman sanksi (*Threat Scorer*), dan iming-iming hadiah (*Reward Scorer*). | 🟢 **100% SAFE (PASSED)** |
| **Quishing (QR Phishing)** | QR Code terselubung pada poster/email fisik menuju phishing site | **Image QR Matrix Decoder & URL Payload Extractor**: Membaca kode QR secara terisolasi di memori tanpa membuka browser (*sandboxed decode*). | 🟢 **100% SAFE (PASSED)** |
| **Document Link Injection** | PDF / DOCX dengan link phishing terselubung dan macro payload | **Document Parser & Embedded Link Inspector**: Ekstraksi seluruh teks dan hyperlink dari file PDF/DOCX tanpa mengeksekusi skrip aktif. | 🟢 **100% SAFE (PASSED)** |
| **API Abuse & Brute Force** | DoS, Token Scraping, API Flooding | **Distributed Token-Bucket Rate Limiter (`SlowAPI` & Edge Gateway)**: Pembatasan ketat 200 request/jam per IP publik untuk mencegah automated abuse. | 🟢 **100% SAFE (PASSED)** |
| **Data Privacy & Telemetry** | Log Kredensial Pengguna, Kebocoran Data Pribadi | **Zero-Telemetry Policy & Ephemeral Processing**: Teks dan dokumen yang dipindai diproses secara transient di memori RAM dan tidak pernah disimpan ke disk permanen. | 🟢 **100% SAFE (PASSED)** |
| **CORS & Header Security** | Cross-Origin Data Leak, Clickjacking, MIME-Sniffing | Strict CORS policy allowing verified origins, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`. | 🟢 **100% SAFE (PASSED)** |

---

## ✨ Fitur Unggulan PhishGuard v2.0

1. 🔗 **6-Vector Multi-Scanner Terintegrasi**:
   - **URL / Tautan**: Memeriksa reputasi domain, sertifikat, dan indikator IP mentah.
   - **Email**: Analisis header, kata kunci rekayasa sosial, dan link phishing tersembunyi.
   - **SMS / WhatsApp**: Deteksi penipuan OTP, hadiah palsu, dan impersonasi bank (BCA, BRI, Mandiri, BNI, Dana, Shopee).
   - **QR Code (Quishing)**: Pemindai barcode dan QR code dari unggahan gambar.
   - **Halaman Web**: Inspeksi visual dan keamanan formulir input.
   - **File Dokumen**: Ekstraksi tautan berbahaya dari PDF, DOCX, dan file teks.

2. ⚡ **Hybrid Dual-Engine Architecture (Zero-Downtime Guarantee)**:
   - **Primary Engine**: Python FastAPI Serverless ASGI di hosting Vercel dengan integrasi Google Safe Browsing, PhishTank, dan Hugging Face NLP.
   - **Edge Heuristic Fallback Engine**: Mesin heuristik mandiri yang berjalan 100% di browser klien jika koneksi backend offline, memastikan aplikasi selalu dapat digunakan kapan saja tanpa jeda.

3. 📊 **Visual Risk Gauge & Live Threat Ticker**:
   - Visualisasi tingkat bahaya interaktif (*Aman, Mencurigakan, Bahaya Phishing*) dengan perhitungan skor persentase risiko akurat.
   - *Live Threat Ticker* yang menampilkan pembaruan pola ancaman siber terkini.

4. 📑 **Pusat Unduh Laporan Audit Keamanan**:
   - Ekspor Laporan Audit lengkap dalam format file **JSON Data Structure**.
   - Fitur **Cetak / Ekspor PDF Resmi** untuk dokumentasi investigasi keamanan.

5. ⚙️ **Dynamic API Endpoint Switcher**:
   - Pengguna dapat mengganti URL Backend API secara fleksibel langsung melalui modal pengaturan antarmuka tanpa perlu build ulang kode sumber.

---

## 🏛️ Struktur Arsitektur Monorepo

Proyek ini menggunakan arsitektur monorepo terstruktur standar industri yang memisahkan aplikasi (*apps*), paket bersama (*packages*), dan microservices (*services*):

```
├── .github/
│   └── workflows/
│       ├── ci.yml                 # Monorepo CI/CD (Test, Lint, Security Integrity)
│       └── gh-pages.yml           # Otomasi deployment GitHub Pages
│
├── api/
│   └── index.py                   # Vercel Serverless Function ASGI Entrypoint
│
├── apps/
│   ├── web-client/                # Frontend React 18 + Vite + Lucide + Dropzone
│   └── server-api/                # Backend REST API Python FastAPI + SlowAPI
│
├── services/
│   ├── url-analyzer-py/           # Standalone URL Feature Extractor & Shannon Entropy
│   ├── nlp-engine-py/             # Standalone Social Engineering NLP & Urgency Scorer
│   ├── qr-scanner-py/             # Standalone QR Code Decoder & Link Verifier
│   └── document-analyzer-py/      # Standalone PDF/DOCX Payload & Link Extractor
│
├── packages/
│   ├── core/                      # Shared Scoring Constants & Math Heuristics (TypeScript)
│   ├── threat-intel/              # Signature Database & Malicious TLDs (JSON)
│   ├── types/                     # Shared TypeScript & Schema Contract Definitions
│   └── ui-components/             # Tactile UI Design Tokens & Badges
│
├── preview/
│   ├── index.html                 # Single-Page Interactive Web App (Live on GitHub Pages)
│   └── manifest.webmanifest      # Konfigurasi PWA Mobile
│
├── scripts/
│   ├── start-dev.sh               # Menjalankan frontend & backend bersamaan (Dev)
│   ├── build-all.sh               # Build seluruh aplikasi dan packages
│   ├── test-all.sh                # Pengujian otomatis lintas modul
│   ├── deploy-vercel.sh           # Skrip deployment ke platform Vercel
│   ├── deploy-gh-pages.sh         # Skrip deployment ke GitHub Pages
│   └── package-zip.sh             # Skrip packaging monorepo ke arsip ZIP
│
├── deployments/
│   ├── docker-compose.yml         # Container stack untuk Mac / Linux / Armbian CasaOS
│   ├── Dockerfile.frontend        # Multi-stage Nginx Container
│   ├── Dockerfile.backend         # FastAPI Container
│   └── nginx.conf                 # Hardened Nginx Reverse Proxy
│
├── package.json                   # Turborepo Workspaces Root
├── turbo.json                     # Turborepo Build Pipeline
├── vercel.json                    # Konfigurasi Routing Serverless Vercel
└── requirements.txt               # Dependencies Python Serverless Vercel
```

---

## 🚀 Panduan Menjalankan Proyek

### 1. Menjalankan Live Web App (Lokal)
```bash
python3 -m http.server 4321 --directory preview/
# Buka http://localhost:4321 di browser
```

### 2. Menjalankan Frontend Web Client (Vite + React)
```bash
cd apps/web-client
npm install
npm run dev
# Buka http://localhost:5173 di browser
```

### 3. Menjalankan Backend API (FastAPI)
```bash
cd apps/server-api
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Dokumentasi Swagger API: http://localhost:8000/api/docs
```

### 4. Menjalankan Seluruh Lingkungan Dev Secara Otomatis
```bash
bash scripts/start-dev.sh
```

### 5. Deployment ke Vercel Serverless
```bash
bash scripts/deploy-vercel.sh
```

### 6. Deployment ke GitHub Pages
```bash
bash scripts/deploy-gh-pages.sh
```

---

## 📄 Lisensi
Hak Cipta © 2026 **Moch. Erik Irriansyah** (NIM 04123003 — Program Studi Sistem Komputer, Fakultas Ilmu Komputer, Universitas Narotama). Seluruh hak cipta dilindungi undang-undang.

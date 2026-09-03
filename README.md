# 🛡️ PhishGuard — Enterprise AI Multi-Vector Phishing & Social Engineering Monorepo

> **Enterprise-Grade AI Multi-Vector Threat Intelligence & Social Engineering Defense Engine**  
> **UI Aesthetic**: Dark Tactical Cyber-Security Glassmorphism (`#090d16` / `#111827` / `#6366f1` / `#10b981`)  
> **Target Devices**: All Device  
> **Live Frontend App**: [https://mocherik.github.io/phishguard/](https://mocherik.github.io/phishguard/)  
> **Live Backend API**: [https://phishguard-api.vercel.app](https://phishguard-api.vercel.app) *(Vercel Serverless ASGI)*  
> **Author**: Moch. Erik Irriansyah (NIM 04123003 — Universitas Narotama)

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

## 💻 Instalasi Cepat & Penggunaan Langsung via Terminal (CLI)

Bagi pengguna atau developer yang tidak ingin repot membuka browser atau mesin pencari, **PhishGuard** menyediakan perkakas terminal **PhishGuard CLI** yang dapat diinstal dan dijalankan secara instan dengan **1 baris perintah**:

### ⚡ 1. Install Global CLI Otomatis (1 Baris Perintah):
```bash
curl -sSL https://raw.githubusercontent.com/MochErik/phishguard/main/scripts/install-cli.sh | bash
```

### ⚡ 2. Menjalankan Langsung Tanpa Install (*On-the-Fly*):
```bash
curl -sSL https://raw.githubusercontent.com/MochErik/phishguard/main/bin/phishguard | python3 - scan "https://bca-login-verify.xyz"
```

### 🛠️ 3. Contoh Penggunaan Perintah CLI:
```bash
# 1. Buka Menu Interaktif Terminal Dashboard
phishguard

# 2. Pindai Tautan / URL Langsung
phishguard scan https://bca-update-data.xyz/login

# 3. Pindai Teks Pesan SMS / WhatsApp Rekayasa Sosial
phishguard text "URGENT: Rekening Mandiri Anda diblokir dalam 24 jam! Segera verifikasi kode OTP sekarang."

# 4. Format Output JSON Mentah (Cocok untuk Integrasi CI/CD & Automasi)
phishguard --json https://bca-update-data.xyz
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

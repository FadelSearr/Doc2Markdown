# Doc2Markdown

Sistem konversi dokumen (PDF, DOCX, XLSX, PPTX) menjadi format Markdown dengan keakuratan tinggi, deterministik, dan tanpa halusinasi untuk konsumsi model kecerdasan buatan (LLM).

---

## 📌 Tentang Proyek (About)

**Doc2Markdown** dirancang untuk mengatasi masalah degradasi teks dan kehilangan struktur saat dokumen diubah menjadi data teks. Menggunakan mesin parsing deterministik (berbasis *Microsoft MarkItDown*), sistem ini mengekstrak teks, hierarki heading, dan struktur tabel secara utuh tanpa mengubah makna kata atau mengarang isi dokumen.

### Mengapa Doc2Markdown?
- **100% Deterministik**: Tanpa model generatif di tahap ekstraksi, mencegah halusinasi data.
- **Preservasi Tabel & Format**: Tabel tetap berformat tabel Markdown murni (`| col | col |`).
- **Optimal untuk LLM**: Output langsung dapat dibaca oleh ChatGPT, Claude, Gemini, maupun embedding pipeline RAG.
- **Workflow Mudah**: Antarmuka 3 langkah sederhana: Unggah -> Proses -> Unduh / Salin.

---

## 🚀 Format File yang Didukung

| Format | Ekstensi | Keterangan |
| :--- | :--- | :--- |
| **PDF** | `.pdf` | Dokumen teks, jurnal, panduan, laporan |
| **Word** | `.docx` | Dokumen Microsoft Word |
| **Excel** | `.xlsx` | Tabel lembar kerja spreadsheet |
| **PowerPoint** | `.pptx` | Presentasi slide |

---

## 🔌 API Endpoint

### `POST /api/convert`
Menerima file dokumen via `multipart/form-data` dan mengembalikan respons JSON.

**Request:**
- `file`: File dokumen (`.pdf`, `.docx`, `.xlsx`, `.pptx`)

**Response:**
```json
{
  "status": "success",
  "filename": "dokumen.md",
  "markdown": "# Judul Dokumen\n\nTeks isi dokumen..."
}
```

---

## 📄 Lisensi
MIT License. Bebas digunakan untuk keperluan pribadi maupun riset akademis.

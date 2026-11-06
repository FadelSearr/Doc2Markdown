import io
import json
import asyncio
import fitz
from fastapi import UploadFile
from server import convert_document

def test_api_convert():
    # Buat PDF dummy
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Dokumen Uji API Doc2Markdown")
    pdf_bytes = doc.tobytes()
    doc.close()

    # Eksekusi endpoint handler
    upload_file = UploadFile(filename="test.pdf", file=io.BytesIO(pdf_bytes))
    response = asyncio.run(convert_document(upload_file))

    assert response.status_code == 200, f"Status gagal: {response.status_code}"
    data = json.loads(response.body)
    assert data["status"] == "success"
    assert data["filename"] == "test.md"
    assert "Dokumen Uji API Doc2Markdown" in data["markdown"], "Isi teks tidak sesuai"
    print("TEST API SERVER: PASSED")

if __name__ == "__main__":
    test_api_convert()

from pathlib import Path
import fitz
from convert import convert

# Self-check: buat PDF dummy, konversi ke Markdown, validasi isi teks
def test_convert():
    pdf_path = Path("sample_test.pdf")
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Dokumen Uji Keakuratan Tinggi")
    doc.save(str(pdf_path))
    doc.close()

    md_path = convert(str(pdf_path))
    assert Path(md_path).exists(), "Output markdown tidak dibuat"
    content = Path(md_path).read_text(encoding="utf-8")
    assert "Dokumen Uji Keakuratan Tinggi" in content, "Teks tidak sesuai atau hilang"

    # Cleanup
    pdf_path.unlink()
    Path(md_path).unlink()
    print("ALL ASSERTIONS PASSED")

if __name__ == "__main__":
    test_convert()


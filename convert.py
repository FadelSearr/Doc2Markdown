import sys
from pathlib import Path
from markitdown import MarkItDown

# ponytail: konversi lokal standar (PDF, DOCX, XLSX, dsb). tambah OCR/LLM vision jika PDF hasil scan gambar murni.
def convert(src_path: str, dst_path: str | None = None) -> str:
    path = Path(src_path)
    if not path.is_file():
        raise FileNotFoundError(f"File missing: {src_path}")
    res = MarkItDown().convert(str(path))
    out = Path(dst_path) if dst_path else path.with_suffix(".md")
    out.write_text(res.text_content, encoding="utf-8")
    return str(out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <input_file> [output.md]")
        sys.exit(1)
    print(convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))


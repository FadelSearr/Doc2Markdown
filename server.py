import os
import tempfile
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from markitdown import MarkItDown

app = FastAPI(title="DocToMarkdown API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

md_converter = MarkItDown()

# ponytail: konversi multi-file sekuensial. Upgrade multiprocessing jika batch > 20 dokumen.
@app.post("/api/convert")
async def convert_documents(files: list[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="Tidak ada file yang diunggah.")
    
    results = []
    for file in files:
        if not file.filename:
            continue
        suffix = Path(file.filename).suffix.lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp_path = tmp.name
            tmp.write(await file.read())
        try:
            res = md_converter.convert(tmp_path)
            base_name = Path(file.filename).stem
            results.append({
                "filename": f"{base_name}.md",
                "markdown": res.text_content
            })
        except Exception as e:
            base_name = Path(file.filename).stem
            results.append({
                "filename": f"{base_name}.md",
                "error": str(e),
                "markdown": ""
            })
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    return JSONResponse({"status": "success", "results": results})

# Static frontend mount
static_dir = Path(__file__).parent / "public"
if static_dir.exists():
    app.mount("/", StaticFiles(directory=str(static_dir), html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("server:app", host="0.0.0.0", port=port, reload=True)

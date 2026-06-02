from pypdf import PdfReader, PdfWriter
import os
from pathlib import Path

source_dir = Path(r"D:\04_claude_code\01_Fitness\fitness-advisor\failed_pdf")
output_dir = source_dir / "split"
output_dir.mkdir(exist_ok=True)

pdfs = list(source_dir.glob("*.pdf"))

for pdf_path in pdfs:
    reader = PdfReader(str(pdf_path))
    total = len(reader.pages)
    parts = 4
    chunk_size = total // parts

    print(f"\n{'='*60}")
    print(f"Splitting: {pdf_path.name}")
    print(f"Total pages: {total}, per part: ~{chunk_size}")
    print(f"{'='*60}")

    for i in range(parts):
        writer = PdfWriter()
        start = i * chunk_size
        end = total if i == parts - 1 else (i + 1) * chunk_size

        for j in range(start, end):
            writer.add_page(reader.pages[j])

        out_name = f"{pdf_path.stem}_part{i+1}.pdf"
        out_path = output_dir / out_name
        with open(out_path, "wb") as f:
            writer.write(f)
        print(f"  [OK] {out_name}: pages {start+1}-{end} ({end-start} pages)")

print(f"\nAll done! Output: {output_dir}")

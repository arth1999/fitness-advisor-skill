"""Split new fitness books into max 200 pages per part, with pinyin filenames."""
from pypdf import PdfReader, PdfWriter
import os
import shutil

book_dir = r"D:\04_claude_code\01_Fitness\fitness-advisor\pdf_source\new_fitness_book"
out_dir = r"D:\04_claude_code\01_Fitness\fitness-advisor\pdf_source\new_fitness_book\split"
os.makedirs(out_dir, exist_ok=True)

# Mapping: original filename prefix -> pinyin safe name
NAME_MAP = {
    "NSCA-CSCS_5th": "NSCA_CSCS_5th",
    "NASM Essentials of Personal Fitness Training - 7th Edition": "NASM_CPT_7th",
    "基础肌动学": "jichu_jidongxue",
    "基础肌动学 第4版": "jichu_jidongxue_4th",
    "功能性动作科学": "gongnengxing_dongzuo_kexue",
    "体能训练": "tineng_xunlian",
    "基于生物力学的纠正性训练": "jiuzhengxing_xunlian",
    "重返巅峰": "chongfan_dianfeng",
    "Peter Brukner - Brukner and Khan's clinical sports medicine_v1": "Brukner_Khan_clinical_sports_medicine_v1",
    "Peter Brukner - Brukner and Khan's clinical sports medicine_v2": "Brukner_Khan_clinical_sports_medicine_v2",
    "National Strength & Conditioning Association (Estats Units d'Amè - NSCA's essentials of training special populations (2018, Human Kinetics)": "NSCA_special_populations",
}

MAX_PAGES = 200

def get_safe_name(filename):
    """Match filename to pinyin safe name."""
    name_no_ext = filename.replace(".pdf", "")
    for key, safe in NAME_MAP.items():
        if key in name_no_ext or name_no_ext in key:
            return safe
    # Fallback: just sanitize
    safe = name_no_ext.replace(" ", "_").replace("'", "").replace("(", "").replace(")", "").replace(",", "").replace("&", "")
    return safe[:60]

files = [f for f in os.listdir(book_dir) if f.endswith(".pdf")]
files.sort()

print("=" * 70)
print("STEP 1: Count pages")
print("=" * 70)

total_parts = 0
file_info = []

for f in files:
    path = os.path.join(book_dir, f)
    try:
        reader = PdfReader(path)
        total = len(reader.pages)
        parts = (total + MAX_PAGES - 1) // MAX_PAGES
        safe_name = get_safe_name(f)
        file_info.append((f, path, total, parts, safe_name))
        print(f"  {total:>5}p  {parts:>3} parts  ->  {safe_name}")
        total_parts += parts
    except Exception as e:
        print(f"  ERROR: {f} -> {e}")

print(f"\n  Total: {total_parts} parts to generate")

print("\n" + "=" * 70)
print("STEP 2: Split PDFs")
print("=" * 70)

for fname, path, total, num_parts, safe_name in file_info:
    print(f"\n  {safe_name}  ({total}p -> {num_parts} parts)")
    reader = PdfReader(path)

    for i in range(num_parts):
        writer = PdfWriter()
        start = i * MAX_PAGES
        end = min((i + 1) * MAX_PAGES, total)

        for j in range(start, end):
            writer.add_page(reader.pages[j])

        out_name = f"{safe_name}_part{i+1}.pdf"
        out_path = os.path.join(out_dir, out_name)
        with open(out_path, "wb") as fout:
            writer.write(fout)
        print(f"    [OK] {out_name}  pages {start+1}-{end} ({end-start}p)")

print(f"\n{'=' * 70}")
print(f"ALL DONE! {total_parts} parts in: {out_dir}")
print(f"{'=' * 70}")

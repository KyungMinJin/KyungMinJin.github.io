import pypdf
import os

def extract_pdf_pages(input_path, output_path, start_page, end_page):
    """
    Extracts pages from start_page to end_page (1-based, inclusive)
    and writes them to output_path.
    """
    if not os.path.exists(input_path):
        print(f"Error: Input file '{input_path}' does not exist.")
        return False
        
    print(f"Reading {input_path}...")
    reader = pypdf.PdfReader(input_path)
    writer = pypdf.PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}. Extracting pages {start_page} to {end_page}...")
    
    # 1-based to 0-indexed transition
    for idx in range(start_page - 1, min(end_page, total_pages)):
        writer.add_page(reader.pages[idx])
        
    with open(output_path, "wb") as out_f:
        writer.write(out_f)
    print(f"Successfully saved to {output_path} (Total pages: {len(writer.pages)})\n")
    return True

if __name__ == "__main__":
    # 1. First PDF: 진경민_직무역량기술서.pdf
    # Pages 3 to 20 are project-specific.
    extract_pdf_pages(
        input_path="_notion/진경민_직무역량기술서.pdf",
        output_path="_notion/진경민_직무역량기술서_프로젝트.pdf",
        start_page=3,
        end_page=20
    )
    
    # 2. Second PDF: 진경민_직무역량기술서_2차면접.pdf
    # Pages 2 to 20 are project-specific.
    extract_pdf_pages(
        input_path="_notion/진경민_직무역량기술서_2차면접.pdf",
        output_path="_notion/진경민_직무역량기술서_2차_프로젝트.pdf",
        start_page=2,
        end_page=20
    )

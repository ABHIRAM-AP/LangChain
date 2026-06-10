from pathlib import Path
from typing import List, Any
from langchain_docling.loader import DoclingLoader  


def load_all_documents(data_dir:str)->List[Any]:
    """
        Loads all supported files from data directory and convert to LangChain document structure.
        Supported formats: [ PDF,TXT,CSV,EXCEL,WORD,JSON]
    """

    data_path=Path(data_dir).resolve()
    print(f"[DEBUG], Data path: {data_path}")
    documents-[]

    # PDF Files
    pdf_files=list(data_path.glob("**/*.pdf"))
    print(f"[DEBUG] Found {len(pdf_files)} PDF Files: {[str(file) for file in pdf_files]}")

    for pdf_file in pdf_files:
        print(f"[DEBUG] Loading PDF: {pdf_file}")
        try:
            documents=DoclingLoader.load(str(pdf_file))
            print(documents)
        except Exception as e:
            print(f"[DEBUG] Error occured while loading pdf {e}")
            


load_all_documents('data/pdf')
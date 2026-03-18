from __future__ import annotations

import csv
import json
import re
import ssl
from pathlib import Path
from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import urlopen

API_URL = "https://backend.softecnu.org/api/competitions_listable/"


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_") or "competition"


def parse_extension_from_url(url: str, default: str) -> str:
    path = urlparse(url).path
    ext = Path(path).suffix.lower()
    return ext if ext else default


def open_url(url: str, timeout: int = 30):
    try:
        return urlopen(url, timeout=timeout)
    except URLError as error:
        message = str(error)
        if "CERTIFICATE_VERIFY_FAILED" not in message:
            raise
        insecure_context = ssl._create_unverified_context()
        return urlopen(url, timeout=timeout, context=insecure_context)


def fetch_api_competitions() -> list[dict]:
    with open_url(API_URL, timeout=30) as response:
        data = json.load(response)
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def save_logo(logos_dir: Path, index: int, name: str, api_logo_url: str | None) -> str:
    logos_dir.mkdir(parents=True, exist_ok=True)
    if not api_logo_url:
        return ""

    safe_name = slugify(name)
    ext = parse_extension_from_url(api_logo_url, default=".png")
    file_name = f"{index:02d}_{safe_name}{ext}"
    file_path = logos_dir / file_name

    try:
        with open_url(api_logo_url, timeout=30) as response, file_path.open("wb") as output:
            output.write(response.read())
        return file_name
    except Exception:
        return ""


def extract_document_urls(item: dict) -> list[str]:
    details = item.get("details")
    if not isinstance(details, list):
        return []

    urls: list[str] = []
    for entry in details:
        if not isinstance(entry, dict):
            continue
        document_url = entry.get("document")
        if not isinstance(document_url, str):
            continue
        document_url = document_url.strip()
        if not document_url:
            continue
        urls.append(document_url)
    return urls


def save_documents(docs_dir: Path, index: int, name: str, document_urls: list[str]) -> list[str]:
    docs_dir.mkdir(parents=True, exist_ok=True)
    if not document_urls:
        return []

    safe_name = slugify(name)
    saved_files: list[str] = []
    for doc_index, document_url in enumerate(document_urls, start=1):
        ext = parse_extension_from_url(document_url, default=".pdf")
        file_name = f"{index:02d}_{safe_name}_doc{doc_index:02d}{ext}"
        file_path = docs_dir / file_name

        try:
            with open_url(document_url, timeout=30) as response, file_path.open("wb") as output:
                output.write(response.read())
            saved_files.append(file_name)
        except Exception:
            continue

    return saved_files


def main() -> None:
    root = Path(__file__).resolve().parent
    output_csv = root / "competitions_data.csv"
    logos_dir = root / "competition_logos"
    docs_dir = root / "competition_pdfs"

    api_items = fetch_api_competitions()

    rows: list[dict] = []
    for idx, item in enumerate(api_items, start=1):
        name = str(item.get("name") or item.get(
            "registration_name") or "").strip()
        if not name:
            continue

        logo_file = save_logo(
            logos_dir=logos_dir,
            index=idx,
            name=name,
            api_logo_url=item.get("logo"),
        )

        saved_docs = save_documents(
            docs_dir=docs_dir,
            index=idx,
            name=name,
            document_urls=extract_document_urls(item),
        )

        rows.append(
            {
                "logo": logo_file,
                "documents": "|".join(saved_docs),
                "Competition Name": name,
                "Winner Prize": item.get("winner_Prize", ""),
                "Runner Up Prize": item.get("runnerUp_Prize", ""),
                "Registration Fees": item.get("fees", ""),
                "Minimum Team Member Allowed": item.get("min_team_size", ""),
                "Maximum Team Member Allowed": item.get("max_team_size", ""),
            }
        )

    with output_csv.open("w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=[
                "logo",
                "documents",
                "Competition Name",
                "Winner Prize",
                "Runner Up Prize",
                "Registration Fees",
                "Minimum Team Member Allowed",
                "Maximum Team Member Allowed",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"API competitions fetched: {len(api_items)}")
    print(f"Rows written: {len(rows)}")
    print(f"CSV written: {output_csv}")
    print(f"Logos folder: {logos_dir}")
    print(f"Documents folder: {docs_dir}")


if __name__ == "__main__":
    main()

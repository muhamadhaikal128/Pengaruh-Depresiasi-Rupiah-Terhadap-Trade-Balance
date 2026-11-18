"""Download source bytes unchanged; inventory candidates before selecting economic series.

Run from repository root: python Tio/script/02_download_macro_sources.py
Requires httpx. FRED distributes IMF/OECD/national-agency series; inspect metadata
before selecting levels, growth rates, adjustment and quotation conventions.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import re
import httpx

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'input' / 'raw' / 'macro_external_20261117'
RAW.mkdir(parents=True, exist_ok=True)

def fetch(item):
    label, url, ext = item
    path = RAW / (label + ext)
    meta = dict(label=label, requested_url=url,
                retrieved_utc=datetime.now(timezone.utc).isoformat())
    try:
        with httpx.Client(follow_redirects=True, timeout=50) as client:
            r = client.get(url)
        path.write_bytes(r.content)
        meta.update(status=r.status_code, final_url=str(r.url), bytes=len(r.content),
                    content_type=r.headers.get('content-type'),
                    sha256=hashlib.sha256(r.content).hexdigest(), path=path.relative_to(ROOT).as_posix())
        if r.status_code == 200 and ext == '.csv':
            lines=r.text.splitlines()
            meta.update(header=lines[:1], first=lines[1:2], last=lines[-1:])
        elif r.status_code == 200 and ext == '.html':
            title=re.search(r'<title[^>]*>(.*?)</title>',r.text,re.S)
            meta['title']=title.group(1) if title else ''
    except Exception as exc:
        meta['error']=str(exc)
    return meta

def main():
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh',action='store_true',help='Explicitly replace the saved source vintage')
    args=parser.parse_args()
    requests=json.loads(Path(__file__).with_name('macro_source_requests.json').read_text('utf-8'))
    tasks=[(x['label'],x['url'],x['extension']) for x in requests]
    old=RAW/'download_manifest.json'
    rows=json.loads(old.read_text('utf-8')) if old.exists() else []
    labels=set()
    if not args.refresh:
        for x in rows:
            p=ROOT/x.get('path','').replace('\\','/')
            if x.get('status')==200 and p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==x.get('sha256'):
                labels.add(x['label'])
    tasks=[t for t in tasks if t[0] not in labels]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for future in as_completed([pool.submit(fetch,t) for t in tasks]):
            result=future.result(); rows=[x for x in rows if x['label']!=result['label']]+[result]
            old.write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
            print(result['label'],result.get('status'),result.get('error',''),flush=True)
    if not tasks: print('All configured sources already present; SHA-256 checked. Use --refresh for a new vintage.')

if __name__=='__main__':
    main()

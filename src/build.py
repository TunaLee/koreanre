#!/usr/bin/env python3
"""오전 · 오후 덱을 docs/am.html · docs/pm.html 로 만든다.

사용: python3 src/build.py
"""
from pathlib import Path

import am
import pm

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"


def render(title, parts):
    tpl = (SRC / "template.html").read_text(encoding="utf-8")
    theme = (SRC / "theme.css").read_text(encoding="utf-8")
    tpl = tpl.replace("</style>\n</head>", theme + "\n</style>\n</head>", 1)
    return tpl.replace("{{DECK_TITLE}}", title).replace("{{SLIDES}}", "\n\n".join(parts))


INDEX = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>AI 업무도구 제작 교육</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/pretendard@1.3.9/dist/web/static/pretendard.min.css">
<style>
:root{--ink:#111;--mut:#6B6B73;--line:#E6E6EA;--red:#E8002D;}
body{margin:0;font-family:Pretendard,-apple-system,sans-serif;color:var(--ink);background:#fff;}
main{max-width:860px;margin:0 auto;padding:56px 16px 80px;}
.k{font-weight:800;color:var(--red);font-size:14px;} h1{font-size:40px;letter-spacing:-.03em;margin:10px 0 6px;}
p.s{color:var(--mut);margin:0 0 36px;} h2{font-size:20px;margin:36px 0 12px;padding-bottom:8px;border-bottom:2px solid var(--ink);}
a.row{display:flex;justify-content:space-between;gap:16px;padding:14px 4px;border-bottom:1px solid var(--line);color:var(--ink);text-decoration:none;}
a.row:hover{background:#FFF5F7;} a.row span{color:var(--mut);font-size:14px;} a.row b{font-weight:700;}
.note{margin-top:28px;font-size:14px;color:var(--mut);line-height:1.6;}
</style></head><body><main>
<div class="k">코리안리재보험 AI 업무도구 제작 교육 · 2026</div>
<h1>강의 슬라이드 · 실습 자료</h1>
<p class="s">오전과 오후는 서로 독립된 과정입니다.</p>
<h2>오전 · 반복 지시는 스킬로</h2>
<a class="row" href="am.html"><b>오전 강의 슬라이드</b><span>열기 →</span></a>
<a class="row" href="dl/오전_실습자료.zip" download><b>오전 실습 자료 (더미)</b><span>zip 내려받기</span></a>
<h2>오후 · 조사 자료는 보고서로</h2>
<a class="row" href="pm.html"><b>오후 강의 슬라이드</b><span>열기 →</span></a>
<a class="row" href="dl/오후_공통데이터.csv" download><b>오후 공통 데이터 (CSV)</b><span>내려받기</span></a>
<a class="row" href="dl/오후_공통데이터_출처.md" download><b>공통 데이터 출처</b><span>내려받기</span></a>
<a class="row" href="dl/GAS_업무관리.zip" download><b>심화 · GAS 업무 관리 웹 완성본</b><span>zip 내려받기</span></a>
<a class="row" href="gas_preview.html"><b>GAS 업무 관리 웹 미리보기 (가짜 데이터)</b><span>열기 →</span></a>
<p class="note">실습 자료의 이름 · 숫자는 모두 가상입니다(오후 공통 데이터는 공식 통계). 회사 실데이터는 입력하지 마세요.</p>
</main></body></html>
"""


def downloads(out):
    import shutil
    import zipfile
    dl = out / "dl"
    if dl.exists():
        shutil.rmtree(dl)
    dl.mkdir()
    data = ROOT / "data"
    with zipfile.ZipFile(dl / "오전_실습자료.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted((data / "오전").rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, Path("오전_실습자료") / f.relative_to(data / "오전"))
    for name in ("오후_공통데이터.csv", "오후_공통데이터_출처.md"):
        shutil.copy(data / name, dl / name)
    with zipfile.ZipFile(dl / "GAS_업무관리.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted((data / "GAS_업무관리").iterdir()):
            z.write(f, Path("GAS_업무관리") / f.name)
    gas = (data / "GAS_업무관리" / "Index.html").read_text(encoding="utf-8")
    stub = (SRC / "gas_stub.js").read_text(encoding="utf-8")
    (out / "gas_preview.html").write_text(gas.replace("<head>", "<head><script>" + stub + "</script>", 1), encoding="utf-8")
    (out / "index.html").write_text(INDEX, encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")


def main():
    out = ROOT / "docs"
    out.mkdir(exist_ok=True)
    downloads(out)
    for name, title, mod in (("am", "반복 지시는 스킬로 · 오전", am), ("pm", "조사 자료는 보고서로 · 오후", pm)):
        parts = mod.slides()
        (out / f"{name}.html").write_text(render(title, parts), encoding="utf-8")
        print(name, len(parts), "장")


if __name__ == "__main__":
    main()

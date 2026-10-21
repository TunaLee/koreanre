"""그림 요소: 개념 도해와 화면 모형. 모두 HTML · 인라인 SVG라 외부 파일 없이 그려진다."""


def _tile(icon, title, desc, cls=""):
    return f'<div class="ftile {cls}"><div class="fi">{icon}</div><div class="ft">{title}</div><div class="fd">{desc}</div></div>'


# ── 개념 도해 ───────────────────────────────────────────────

def agent_parts():
    """에이전트 = 모델 + 도구 + 지침 + 자료."""
    return ('<div class="parts">'
            + _tile("🧠", "모델", "읽고 · 판단하고 · 쓰는 두뇌", "core")
            + '<div class="plus">+</div>'
            + _tile("🛠️", "도구", "검색 · 파일 · 시트 · 캘린더<br>직접 열어 보는 손")
            + '<div class="plus">+</div>'
            + _tile("📘", "지침", "우리 팀 방식대로<br>일하는 매뉴얼")
            + '<div class="plus">+</div>'
            + _tile("🗂️", "자료", "양식 · 예시 · 지난 결과<br>책상 위 참고자료")
            + '</div>')


def agent_loop(ask="「이번 주 보고서 써 줘」", out="보고서 초안", steps=None):
    """요청 → 계획 → 도구 실행 → 결과 확인 → (반복) → 답."""
    st = steps or [("계획", "무엇이 필요한지"), ("도구 실행", "시트 · 캘린더 읽기"), ("결과 확인", "빠진 것 · 틀린 것"), ("다시", "부족하면 한 번 더")]
    nodes = [(t, d, x, y) for (t, d), (x, y) in zip(st, [(300, 70), (500, 190), (300, 310), (100, 190)])]
    svg = ['<svg viewBox="0 0 600 380" class="loop">',
           '<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">'
           '<path d="M0,0 L10,5 L0,10 z" fill="#E8002D"/></marker></defs>',
           '<circle cx="300" cy="190" r="120" fill="none" stroke="#F3C0CB" stroke-width="3" stroke-dasharray="8 8"/>']
    arcs = ["M370 95 Q450 120 470 160", "M470 225 Q450 270 370 290", "M230 290 Q150 270 130 225", "M130 160 Q150 115 230 95"]
    for d in arcs:
        svg.append(f'<path d="{d}" fill="none" stroke="#E8002D" stroke-width="3" marker-end="url(#ah)"/>')
    for t, s, x, y in nodes:
        svg.append(f'<rect x="{x - 78}" y="{y - 32}" width="156" height="64" rx="12" fill="#fff" stroke="#111" stroke-width="2"/>'
                   f'<text x="{x}" y="{y - 4}" text-anchor="middle" class="lt">{t}</text>'
                   f'<text x="{x}" y="{y + 18}" text-anchor="middle" class="ls">{s}</text>')
    svg.append('<text x="300" y="186" text-anchor="middle" class="lc">스스로 반복</text>'
               '<text x="300" y="210" text-anchor="middle" class="ls">끝날 때까지</text></svg>')
    return (f'<div class="loopwrap"><div class="lend">요청<br><b>{ask}</b></div>'
            + "".join(svg) + f'<div class="lend r">답<br><b>{out}</b></div></div>')


def tool_call():
    """모델은 직접 접속하지 않는다 — 도구에 부탁하고, 도구는 내 권한으로 가져온다."""
    st = [("💬", "나", "「이번 주 현황 요약해 줘」"), ("🧠", "ChatGPT", "「시트가 필요해」 판단"),
          ("🔌", "플러그인", "Google Sheets 앱"), ("🔑", "내 권한", "연결할 때 허용한 범위만"),
          ("📊", "내 시트", "팀 업무 현황")]
    cells = '<div class="tc-arr">→</div>'.join(
        f'<div class="tc"><div class="fi">{i}</div><div class="ft">{t}</div><div class="fd">{d}</div></div>' for i, t, d in st)
    return (f'<div class="tcall">{cells}</div>'
            '<div class="tback">← 읽은 내용이 같은 길로 돌아와 ChatGPT가 요약</div>')


def disclosure():
    """스킬은 설명만 먼저 읽고, 필요할 때 본문 · 파일을 펼친다."""
    return ('<div class="disc">'
            '<div class="dl"><div class="dk">항상</div><div class="dbar w1"><b>이름 · 설명</b> 한두 줄</div>'
            '<div class="dn">스킬이 30개여도 설명만 훑어봄</div></div>'
            '<div class="dl"><div class="dk">요청이 맞으면</div><div class="dbar w2"><b>지침 본문</b> 규칙 · 순서 · 형식</div>'
            '<div class="dn">「주간 보고」 요청 → 이 스킬만 펼침</div></div>'
            '<div class="dl"><div class="dk">더 필요하면</div><div class="dbar w3"><b>참고 파일</b> 양식 · 예시 · 메일</div>'
            '<div class="dn">작성 중 필요한 파일만 열어 봄</div></div>'
            '</div>')


def bundle():
    """플러그인 = 스킬 + 앱 묶음."""
    return ('<div class="bundle"><div class="bh">플러그인 · 「팀 업무 보고」</div><div class="bb">'
            '<div class="bs"><span>SKILL</span><b>주간업무보고</b><i>4항목 · 마감 초과 맨 위 · 추정 금지</i></div>'
            '<div class="bs app"><span>APP</span><b>Google Sheets</b><i>팀 업무 현황 읽기</i></div>'
            '<div class="bs app"><span>APP</span><b>Google Calendar</b><i>팀 일정 읽기</i></div>'
            '</div><div class="bf">한 번 설치 → 지침과 연결이 같이 따라옴</div></div>')


def forgetting():
    """대화창 지시는 흘러가고, 저장한 지침은 남는다."""
    lines = ["지난주: 「4항목 · 마감 초과 맨 위로」", "…", "다른 질문", "다른 질문", "…", "이번 주: 「보고서 써 줘」"]
    chat = "".join(f'<div class="fl" style="opacity:{0.25 + i * 0.15:.2f}">{t}</div>' for i, t in enumerate(lines))
    return ('<div class="forget">'
            f'<div class="fc"><div class="fh">대화창에만 말한 규칙</div>{chat}<div class="fx">규칙은 이미 저 위로 · 매번 다시 설명</div></div>'
            '<div class="fc good"><div class="fh">스킬로 저장한 규칙</div>'
            '<div class="pin">📌 주간업무보고<br><small>4항목 · 마감 초과 맨 위 · 추정 금지</small></div>'
            '<div class="fl">이번 주: 「보고서 써 줘」</div><div class="fx ok">새 대화에서도 같은 규칙</div></div></div>')


def timeline(items):
    """items: [(시기, 제목, 설명, 강조여부)]"""
    out = "".join(f'<div class="tl{" on" if hl else ""}"><div class="ty">{y}</div><div class="tdot"></div>'
                  f'<div class="tt">{t}</div><div class="td">{d}</div></div>' for y, t, d, hl in items)
    return f'<div class="tline">{out}</div>'


# ── 화면 모형 ───────────────────────────────────────────────

def window(title, body, kind="app"):
    return (f'<div class="win {kind}"><div class="wbar"><i></i><i></i><i></i><span>{title}</span></div>'
            f'<div class="wbody">{body}</div></div>')


def sheet(rows, title="팀 업무 현황"):
    head = '<tr><th></th>' + "".join(f"<th>{c}</th>" for c in "ABCDE") + "</tr>"
    body = "".join(f'<tr><th>{i + 1}</th>' + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for i, r in enumerate(rows))
    return window(title + " · Google 시트", f'<table class="gsheet">{head}{body}</table>', "gs")


def calendar(events):
    """events: [(요일 0~4, 시작 시 9~18 소수, 길이 시간, 제목)]"""
    days = "월화수목금"
    cols = ""
    for d in range(5):
        ev = "".join(f'<div class="ev" style="top:{(s - 9) * 14}px;height:{max(l * 14, 14)}px">{t}</div>'
                     for dd, s, l, t in events if dd == d)
        cols += f'<div class="cd"><div class="ch">{days[d]}</div><div class="cb">{ev}</div></div>'
    return window("실습용 팀 일정 · Google 캘린더", f'<div class="gcal">{cols}</div>', "gc")


def skill_editor(name, desc, guide, files):
    f = "".join(f'<span class="file">📄 {x}</span>' for x in files)
    return window("스킬 만들기", (
        f'<div class="se"><label>이름</label><div class="in">{name}</div>'
        f'<label>설명 <em>← 언제 부를지 정함</em></label><div class="in">{desc}</div>'
        f'<label>지침</label><div class="in ta">{guide}</div>'
        f'<label>참고 파일</label><div class="files">{f}</div>'
        '<div class="sv">저장</div></div>'), "se-w")


def report_card(rows, title="주간업무보고_결과"):
    """rows: [(업무, 진행률, 배지, 배지종류)]"""
    body = "".join(f'<div class="rr"><span>{a}</span><b>{b}</b><em class="{k}">{c}</em></div>' for a, b, c, k in rows)
    return window(title, f'<div class="rcard">{body}</div>', "doc")


def bars(items, unit="%", hl=None, top=100):
    """가로 막대. items: [(이름, 값)]"""
    out = ""
    for i, (n, v) in enumerate(items):
        c = " on" if hl is not None and (i == hl or n == hl) else ""
        out += (f'<div class="br{c}"><span class="bn">{n}</span><span class="bt"><i style="width:{v / top * 100:.1f}%"></i></span>'
                f'<span class="bv">{v}{unit}</span></div>')
    return f'<div class="bars">{out}</div>'


def kpis(items):
    """items: [(라벨, 값, 단위, 보조)]"""
    return '<div class="kpis">' + "".join(
        f'<div class="kpi"><span>{l}</span><b>{v}<small>{u}</small></b><em>{s}</em></div>' for l, v, u, s in items) + "</div>"


def browser(url, body):
    return (f'<div class="win br-w"><div class="wbar"><i></i><i></i><i></i><span class="url">{url}</span></div>'
            f'<div class="wbody">{body}</div></div>')


def file_flow():
    """요청문 → Canvas 미리보기 → .html 파일 → 브라우저."""
    st = [("💬", "요청문", "만들 화면을 말로"), ("🖼️", "미리보기", "Canvas에서 바로 확인"),
          ("📄", ".html 파일", "내려받기 · 한 파일"), ("🌐", "브라우저", "더블클릭 · 메일 첨부")]
    cells = '<div class="tc-arr">→</div>'.join(
        f'<div class="tc"><div class="fi">{i}</div><div class="ft">{t}</div><div class="fd">{d}</div></div>' for i, t, d in st)
    return f'<div class="tcall">{cells}</div>'


def research_flow():
    st = [("🔎", "웹 검색", "ChatGPT가 공개 자료 찾기"), ("🔗", "링크 확인", "직접 열어 숫자 대조"),
          ("📊", "표 · CSV", "확인한 값만"), ("📑", "보고서 HTML", "요약 · 근거 · 출처")]
    cells = '<div class="tc-arr">→</div>'.join(
        f'<div class="tc"><div class="fi">{i}</div><div class="ft">{t}</div><div class="fd">{d}</div></div>' for i, t, d in st)
    return f'<div class="tcall">{cells}</div>'


def a4(cut):
    """인쇄 미리보기: 잘린 것 vs 맞춘 것."""
    w = 150 if cut else 100
    cls = "cut" if cut else "fit"
    return (f'<div class="a4 {cls}"><div class="a4h"></div><div class="a4l"></div><div class="a4l s"></div>'
            f'<div class="a4t" style="width:{w}%"></div><div class="a4t" style="width:{w}%"></div>'
            f'<div class="a4c" style="width:{w * .9}%"></div></div>')

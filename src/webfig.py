"""웹 구조 도해 (농심 덱 deck_gas 에서 가져와 문구를 일반 사무용으로 바꿈)."""
from art import G, N, O, W

_P = ["a"]  # 그림마다 화살표 머리 id 를 다르게 (숨은 장의 id 를 참조하면 안 보인다)
_MARKERS = (f'<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{N}"/></marker>'
            f'<marker id="aho" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 Z" fill="{O}"/></marker></defs>')
SOFT = "#F1F1F4"


def markers(prefix):
    _P[0] = prefix
    return _MARKERS.replace('id="ah"', f'id="{prefix}ah"').replace('id="aho"', f'id="{prefix}aho"')


def box(x, y, w, h, title, sub="", fill=W, stroke=N, tcolor=N, rx=14, scls="bs"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="3"/>'
    s += f'<text x="{x+w/2}" y="{y+(h/2 if not sub else h/2-8)}" text-anchor="middle" dominant-baseline="middle" class="bt" fill="{tcolor}">{title}</text>'
    if sub:
        s += f'<text x="{x+w/2}" y="{y+h/2+16}" text-anchor="middle" dominant-baseline="middle" class="{scls}">{sub}</text>'
    return s


def arrow(x1, y1, x2, y2, color=N, dash="", w=3, mid="ah"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} marker-end="url(#{_P[0]}{mid})"/>'


def browser(x, y, w, h, inner):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{W}" stroke="{N}" stroke-width="3"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="12" fill="{G}"/><rect x="{x}" y="{y+14}" width="{w}" height="12" fill="{G}"/>'
            + "".join(f'<circle cx="{x+16+i*14}" cy="{y+13}" r="4" fill="{N}"/>' for i in range(3))
            + inner)


def bars(x, y, hs, color=N, bw=22, gap=12):
    return "".join(f'<rect x="{x+i*(bw+gap)}" y="{y-h}" width="{bw}" height="{h}" rx="3" fill="{color}"/>' for i, h in enumerate(hs))


def db(x, y, w=120, h=130, label="시트"):
    ry = 16
    return (f'<path d="M{x} {y+ry} L{x} {y+h-ry} A{w/2} {ry} 0 0 0 {x+w} {y+h-ry} L{x+w} {y+ry}" fill="{G}" stroke="{N}" stroke-width="3"/>'
            f'<ellipse cx="{x+w/2}" cy="{y+ry}" rx="{w/2}" ry="{ry}" fill="{W}" stroke="{N}" stroke-width="3"/>'
            f'<path d="M{x} {y+h*0.45} A{w/2} {ry} 0 0 0 {x+w} {y+h*0.45}" fill="none" stroke="{N}" stroke-width="2"/>'
            f'<path d="M{x} {y+h*0.7} A{w/2} {ry} 0 0 0 {x+w} {y+h*0.7}" fill="none" stroke="{N}" stroke-width="2"/>'
            f'<text x="{x+w/2}" y="{y+h+30}" text-anchor="middle" class="bt" fill="{N}">{label}</text>')


def folder(x, y, w=140, h=104, label="드라이브"):
    return (f'<path d="M{x} {y+18} Q{x} {y} {x+18} {y} L{x+50} {y} L{x+64} {y+16} L{x+w-14} {y+16} Q{x+w} {y+16} {x+w} {y+30} '
            f'L{x+w} {y+h-14} Q{x+w} {y+h} {x+w-14} {y+h} L{x+14} {y+h} Q{x} {y+h} {x} {y+h-14} Z" fill="{G}" stroke="{N}" stroke-width="3"/>'
            f'<rect x="{x+22}" y="{y+34}" width="{w*0.32}" height="{h*0.42}" rx="4" fill="{W}" stroke="{N}" stroke-width="2"/>'
            f'<rect x="{x+w*0.5}" y="{y+42}" width="{w*0.32}" height="{h*0.42}" rx="4" fill="{W}" stroke="{N}" stroke-width="2"/>'
            f'<text x="{x+w/2}" y="{y+h+30}" text-anchor="middle" class="bt" fill="{N}">{label}</text>')


def static_web():
    mk = markers("st")
    page = browser(760, 70, 330, 250, bars(800, 290, [90, 140, 70, 170, 120], G))
    file_ = (f'<path d="M140 90 L250 90 L290 130 L290 300 L140 300 Z" fill="{W}" stroke="{N}" stroke-width="3"/>'
             f'<path d="M250 90 L250 130 L290 130" fill="none" stroke="{N}" stroke-width="3"/>'
             + "".join(f'<rect x="160" y="{150+i*26}" width="{100 - (i%2)*30}" height="9" rx="4" fill="{G}"/>' for i in range(5))
             + f'<text x="215" y="340" text-anchor="middle" class="bt" fill="{N}">완성된 HTML 파일</text>'
             + f'<text x="215" y="366" text-anchor="middle" class="bs">숫자가 파일 안에 고정</text>')
    flowline = arrow(310, 195, 740, 195, N, w=4) + '<text x="525" y="178" text-anchor="middle" class="bs">메일 첨부 · 그대로 전달</text>'
    return f'''<svg viewBox="0 0 1180 400" class="websvg">{mk}{file_}{flowline}{page}
<text x="925" y="352" text-anchor="middle" class="bt" fill="{N}">브라우저</text>
<text x="925" y="378" text-anchor="middle" class="bs">숫자를 바꾸려면 파일을 다시 만듦</text></svg>'''


def dynamic_web():
    mk = markers("dy")
    page = browser(40, 80, 300, 230, bars(80, 280, [80, 120, 150, 100, 170], O))
    server = box(470, 120, 220, 150, "Apps Script", "화면 틀 + 데이터", fill=SOFT)
    sheet = db(880, 110)
    req = (arrow(345, 130, 465, 130, N, "7 6") + '<text x="405" y="112" text-anchor="middle" class="bs">① 요청</text>'
           + arrow(695, 150, 875, 150, N, "7 6") + '<text x="785" y="132" text-anchor="middle" class="bs">② 조회</text>')
    res = (arrow(875, 250, 695, 250, O, w=4, mid="aho") + '<text x="785" y="282" text-anchor="middle" class="bso">③ 최신 데이터</text>'
           + arrow(465, 270, 345, 270, O, w=4, mid="aho") + '<text x="405" y="302" text-anchor="middle" class="bso">④ 화면 그리기</text>')
    dots = "".join(
        f'<circle r="8" fill="{O}"><animateMotion dur="2.4s" begin="{d}s" repeatCount="indefinite" path="M875 250 L695 250 L580 260 L465 270 L345 270"/></circle>'
        for d in (0, .8, 1.6))
    return f'''<svg viewBox="0 0 1180 400" class="websvg">{mk}{page}{server}{sheet}{req}{res}{dots}
<text x="190" y="350" text-anchor="middle" class="bt" fill="{N}">브라우저</text>
<text x="190" y="376" text-anchor="middle" class="bs">열 때마다 지금 숫자</text></svg>'''


def pipeline():
    """업무 관리 웹 전체 구조 — 화면 입력 · 업로드 → Apps Script → 시트 · 드라이브 → 화면 · AI."""
    s = markers("pl")
    s += browser(40, 30, 300, 150, bars(80, 160, [40, 70, 55, 90], O, bw=26, gap=16))
    s += f'<text x="190" y="210" text-anchor="middle" class="bt" fill="{N}">업무 관리 웹</text><text x="190" y="236" text-anchor="middle" class="bs">입력 · 수정 · 파일 올리기</text>'
    s += box(470, 60, 240, 110, "Apps Script", "검증 · 저장 · 조회", fill=SOFT)
    s += db(840, 40, 120, 110, "시트 · 기록")
    s += folder(1000, 46, 140, 104, "드라이브 · 파일")
    s += arrow(345, 100, 465, 100, O, w=4, mid="aho") + arrow(715, 90, 835, 90, O, w=4, mid="aho")
    s += arrow(715, 140, 995, 140, O, w=4, mid="aho")
    s += box(470, 300, 240, 100, "ChatGPT + 플러그인", "시트 · 드라이브 읽기", fill=N, stroke=N, tcolor=W, scls="bsw")
    s += arrow(900, 230, 715, 330, N, "7 6") + arrow(1070, 230, 715, 360, N, "7 6")
    s += box(840, 330, 300, 90, "주간 보고 · 분석 초안", "AI가 쌓인 기록을 정리", fill=W)
    s += arrow(715, 375, 835, 375, N, w=3)
    return f'<svg viewBox="0 0 1180 440" class="websvg pipe2">{s}</svg>'


def lock(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<path d="M-12 0 V-10 A12 12 0 0 1 12 -10 V0" fill="none" stroke="{O}" stroke-width="5"/>'
            f'<rect x="-18" y="0" width="36" height="28" rx="6" fill="{O}"/><circle cx="0" cy="12" r="4" fill="{W}"/></g>')


def proxy():
    """원본 시트는 잠가 두고, 웹 앱(실행: 나)이 대신 접근."""
    s = markers("px")
    s += f'<rect x="30" y="20" width="560" height="420" rx="22" fill="#F7F7F9" stroke="{N}" stroke-width="2.5" stroke-dasharray="9 7"/>'
    s += f'<text x="58" y="56" class="bt" fill="{N}">내 Google 계정</text>'
    s += db(110, 120, 130, 140, "")
    s += lock(175, 104, 1.1)
    s += f'<text x="175" y="300" text-anchor="middle" class="bt" fill="{N}">시트 · 드라이브</text>'
    s += '<text x="175" y="326" text-anchor="middle" class="bs">공유: 제한됨 · 나만</text>'
    s += box(360, 150, 190, 120, "Apps Script", "실행: 나", fill=SOFT)
    s += arrow(355, 190, 245, 190) + arrow(245, 230, 355, 230)
    s += '<text x="300" y="176" text-anchor="middle" class="bs">읽기</text><text x="300" y="256" text-anchor="middle" class="bs">쓰기</text>'
    s += '<text x="455" y="300" text-anchor="middle" class="bs">내 권한으로 대신 접근</text>'
    s += arrow(555, 210, 740, 210, O, w=4, mid="aho") + '<text x="648" y="192" text-anchor="middle" class="bso">웹 앱 주소</text>'
    for i, y in enumerate((60, 190, 320)):
        s += browser(760, y, 220, 110, bars(790, y + 95, [30, 50, 40, 60], O if i == 1 else G, bw=16, gap=10))
    s += f'<text x="1010" y="190" class="bt" fill="{N}">화면으로만</text>'
    s += '<text x="1010" y="218" class="bs">시트 직접 수정 없음</text><text x="1010" y="242" class="bs">정해진 입력만 저장</text><text x="1010" y="266" class="bs">원본은 안전</text>'
    return f'<svg viewBox="0 0 1240 460" class="websvg">{s}</svg>'


def static_vs_dynamic():
    """정적(CSV를 넣어 만든 HTML) vs 동적(시트 연동 웹): 원본이 바뀌면? 10초 반복 · 인쇄에는 바뀐 뒤 장면."""
    def box(title, sub, extra="", cls=""):
        return f'<div class="sd-b {cls}"><b>{title}</b><span>{sub}</span>{extra}</div>'
    val = lambda old, new, cls: f'<div class="sd-v {cls}"><i class="o">{old}</i><i class="n">{new}</i></div>'
    top = (box("CSV 파일", "10월 손해율", val("62%", "65%", "src"))
           + '<div class="sd-a">→</div>' + box("AI에 첨부 · 요청", "한 번 만들 때만")
           + '<div class="sd-a">→</div>' + box("HTML 파일", "숫자가 파일 안에 고정", val("62%", "62%", "stuck"), "file")
           + '<div class="sd-a">→</div>' + box("브라우저", "열어 보기", '<div class="sd-tag bad">그대로 62% · 다시 요청해 새 파일</div>'))
    bot = (box("Google 시트", "원본 · 10월 손해율", val("62%", "65%", "src"))
           + '<div class="sd-a dyn">⇄<em></em></div>' + box("Apps Script", "열 때마다 시트를 읽음")
           + '<div class="sd-a dyn">⇄<em></em></div>' + box("웹 화면", "새로고침", val("62%", "65%", "live"), "file")
           + '<div class="sd-a">→</div>' + box("브라우저", "웹 앱 주소", '<div class="sd-tag good">65% 반영 · 화면 입력도 시트로</div>'))
    return (f'<div class="sd"><div class="sd-ev">원본 데이터 변경 · 10월 손해율 62% → 65%</div>'
            f'<div class="sd-l"><div class="sd-h">정적 · CSV를 넣어 만든 대시보드</div><div class="sd-row">{top}</div></div>'
            f'<div class="sd-l"><div class="sd-h on">동적 · 데이터를 연동한 웹</div><div class="sd-row">{bot}</div></div></div>')


def web_three():
    """HTML · CSS · JS = 뼈대 · 인테리어 · 스위치 · 같은 카드가 단계별로 바뀜."""
    import html as _h
    cols = [
        ("HTML", "집의 뼈대 · 방 배치", "무엇이 어디에 있는지",
         '<h4>이번 주 팀 할 일</h4>\n<div class="card">\n  <b>비용 집계 보고</b>\n  <span>이준호 · 10/28</span>\n  <button>완료</button>\n</div>',
         '<div class="w3p raw"><div style="font-size:15px;font-weight:700">이번 주 팀 할 일</div><div>비용 집계 보고</div><div>이준호 · 10/28</div><div><u>완료</u></div></div>'),
        ("CSS", "인테리어", "색 · 크기 · 간격 · 배치",
         '.card {\n  border: 1px solid #ddd;\n  border-top: 4px solid #2f6bd8;\n  border-radius: 10px;\n  padding: 14px;\n}',
         '<div class="w3p"><div class="w3c"><b>비용 집계 보고</b><span>이준호 · 10/28</span><i>완료</i></div></div>'),
        ("JavaScript", "전기 · 스위치", "누르면 움직이고 계산",
         'button.onclick = () => {\n  card.classList.add("done");\n  count = count - 1;\n  left.textContent = `남은 일 ${count}개`;\n};',
         '<div class="w3p"><div class="w3c done"><b>비용 집계 보고</b><span>이준호 · 10/28</span><i>완료됨</i></div><small>남은 일 2개</small></div>'),
    ]
    out = ""
    for i, (name, ana, role, code, prev) in enumerate(cols):
        out += (f'<div class="w3"><div class="w3h"><b>{name}</b><span>= {ana}</span></div><div class="w3r">{role}</div>'
                f'<pre class="w3code">{_h.escape(code)}</pre><div class="w3k">화면</div>{prev}</div>')
        if i < 2:
            out += '<div class="w3a">+</div>'
    return f'<div class="w3s">{out}</div>'


def web_without():
    """같은 미니 대시보드: HTML만 / +CSS(JS 없음) / 셋 다."""
    raw = ('<div class="ww raw"><div class="t">손해율 대시보드</div><div>전체 손해율</div><div>—</div><div>재물</div><div>—</div>'
           '<div>배상</div><div>—</div><div><u>전체</u> <u>재물</u> <u>배상</u></div><div class="cv">(차트 자리 · 빈칸)</div></div>')
    card = lambda k, v: f'<div class="wwk"><span>{k}</span><b>{v}</b></div>'
    styled = lambda vals, chart, on: (
        f'<div class="ww"><div class="wwt">손해율 대시보드</div><div class="wwks">{card("전체", vals[0])}{card("재물", vals[1])}{card("배상", vals[2])}</div>'
        f'<div class="wwf"><i class="{"on" if on else ""}">전체</i><i>재물</i><i>배상</i></div>'
        f'<div class="wwc">{chart}</div></div>')
    bars = "".join(f'<i style="height:{h}%"></i>' for h in (55, 62, 58, 70, 65))
    nocss = styled(("—", "—", "—"), '<em>차트 빈칸</em>', False)
    full = styled(("63%", "58%", "71%"), f'<div class="wwb">{bars}</div>', True)
    cols = [("HTML만", "CSS · JS 없음", raw, ["글자가 위에서 아래로 나열", "카드 · 색 · 간격 없음 · 버튼은 밑줄 글자", "차트 자리는 빈칸", "숫자 자리는 「—」"]),
            ("HTML + CSS", "JS 없음", nocss, ["보기는 완성품처럼", "필터 버튼을 눌러도 반응 없음", "숫자 계산 · 차트 그리기가 안 됨", "「모양은 되는데 안 움직임」"]),
            ("HTML + CSS + JS", "완성", full, ["카드에 계산된 숫자", "필터를 누르면 해당 구분만", "차트가 그려짐", "CSV가 바뀌면 다시 계산"])]
    out = ""
    for i, (t, sub, mock, lis) in enumerate(cols):
        out += (f'<div class="wwcol{" on" if i == 2 else ""}"><div class="wwh"><b>{t}</b><span>{sub}</span></div>{mock}'
                f'<ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul></div>')
    return f'<div class="wws">{out}</div>'


def layouts():
    """레이아웃 네 가지 썸네일."""
    def th(inner, name, use):
        return f'<div class="lo"><div class="lo-f">{inner}</div><b>{name}</b><span>{use}</span></div>'
    b = lambda cls="": f'<i class="{cls}"></i>'
    items = [
        (f'<div class="g1">{b("h")}{b()}{b()}{b()}</div>', "세로 1단", "보고서 · 인쇄 · 좁은 화면"),
        (f'<div class="g2">{b("side")}<div class="g1">{b("h")}{b()}{b()}</div></div>', "2단 · 사이드바", "왼쪽 필터 · 오른쪽 내용"),
        (f'<div class="g3">{b()}{b()}{b()}{b()}{b()}{b()}</div>', "카드 격자", "같은 종류 여러 개 · 업무 카드"),
        (f'<div class="g4"><div class="g3s">{b()}{b()}{b()}</div>{b("big")}{b("tb")}</div>', "대시보드형", "위 지표 카드 · 가운데 차트 · 아래 표"),
    ]
    return '<div class="los">' + "".join(th(*x) for x in items) + "</div>"


# ── 다음 토큰 예측 애니메이션 (posco-dx explain.e2 → agent-track vizanim) ──
def next_token(prefix, steps, end_label, uid="nt"):
    """단계마다 (후보, 확률) 목록 · 첫 후보를 골라 문장에 붙인다. 값은 설명용."""
    import json
    data = json.dumps({"prefix": prefix, "steps": steps}, ensure_ascii=False)
    full = "".join([prefix] + [st[0][0] for st in steps])
    last = steps[-1]
    rows = "".join(
        f'<div class="gar{" pick" if i == 0 else ""}"><span class="gaw">{w}</span><span class="gab"><i style="width:{p*100:.0f}%"></i></span><span class="gap">{p:.2f}</span></div>'
        for i, (w, p) in enumerate(last + [("", 0)] * (max(len(st) for st in steps) - len(last))))
    css = ("<style>.ga{background:#F6F6F8;border:1px solid #E4E4E9;border-radius:14px;padding:22px 24px;display:flex;flex-direction:column;gap:14px}"
           ".ga .gas{font-size:26px;font-weight:800;color:#26262B;min-height:40px;line-height:1.4;word-break:keep-all}"
           ".ga .gacur{display:inline-block;width:3px;height:26px;background:#E8002D;margin-left:4px;vertical-align:-4px;animation:gablink 1s steps(1) infinite}"
           "@keyframes gablink{50%{opacity:0}}"
           ".ga .galab{font-size:13px;font-weight:800;color:#6B6B73}.ga .galab span{font-weight:400}"
           ".ga .garows{display:flex;flex-direction:column;gap:8px}"
           ".ga .gar{display:grid;grid-template-columns:120px 1fr 48px;align-items:center;gap:10px;font-size:18px;color:#26262B}"
           ".ga .gaw{text-align:right;font-weight:800;font-family:var(--mono,monospace)}"
           ".ga .gab{height:22px;background:#fff;border-radius:5px;overflow:hidden}"
           ".ga .gab i{display:block;height:100%;background:#DCDCE1;border-radius:5px;transition:width .5s ease,background .3s}"
           ".ga .gar.pick .gab i{background:#E8002D}.ga .gar.pick .gaw{color:#E8002D}"
           ".ga .gap{font-family:var(--mono,monospace);font-size:14px;color:#55555C}"
           ".ga .gaend{display:inline-block;vertical-align:5px;margin-left:12px;font-size:13px;font-weight:800;color:#fff;background:#26262B;border-radius:999px;padding:5px 12px;opacity:0;transition:opacity .3s}"
           ".ga .gaend.on{opacity:1}@media print{.ga .gaend{opacity:1}.ga .gacur{display:none}}</style>")
    js = '''<script>
(function () {
  const box = document.getElementById('%s');
  if (!box) return;
  const D = JSON.parse(box.dataset.gen);
  const txt = box.querySelector('.gatxt'), rows = box.querySelectorAll('.gar'), end = box.querySelector('.gaend');
  let step = 0, words = [D.prefix], phase = 0, timer = null;
  function show(i) {
    const st = D.steps[i];
    rows.forEach((r, k) => {
      const c = st[k];
      r.classList.remove('pick');
      r.style.visibility = c ? 'visible' : 'hidden';
      if (!c) return;
      r.querySelector('.gaw').textContent = c[0];
      r.querySelector('.gap').textContent = c[1].toFixed(2);
      r.querySelector('i').style.width = (c[1] * 100) + '%%';
    });
  }
  function tick() {
    if (box.offsetParent === null) return;
    if (step >= D.steps.length) {
      end.classList.add('on');
      if (++phase > 4) { step = 0; phase = 0; words = [D.prefix]; txt.textContent = D.prefix; end.classList.remove('on'); show(0); }
      return;
    }
    if (phase === 0) { show(step); phase = 1; return; }
    if (phase === 1) { rows[0].classList.add('pick'); phase = 2; return; }
    words.push(D.steps[step][0][0]); txt.textContent = words.join('');
    step += 1; phase = 0;
  }
  window.addEventListener('beforeprint', () => {
    clearInterval(timer); const n = D.steps.length - 1;
    txt.textContent = [D.prefix].concat(D.steps.map(st => st[0][0])).join('');
    show(n); rows[0].classList.add('pick'); end.classList.add('on');
  });
  txt.textContent = D.prefix; show(0);
  rows.forEach(r => r.querySelector('i').style.width = '0%%');
  timer = setInterval(tick, 900);
})();
</script>''' % uid
    return (css + f'''<div class="ga" id="{uid}" data-gen='{data}'>
  <div class="gas"><span class="gatxt">{full}</span><span class="gacur"></span><span class="gaend">{end_label}</span></div>
  <div class="galab">다음 토큰 후보 <span>(설명용 확률)</span></div>
  <div class="garows">{rows}</div>
</div>''' + js)


def tones():
    """같은 할 일 카드 · 네 가지 디자인 톤."""
    items = [("tn-base", "기본", "파란 강조 · 보통 간격"), ("tn-rep", "차분한 보고서", "흰 배경 · 남색 하나 · 넓은 여백 · 각진 모서리"),
             ("tn-dark", "다크 대시보드", "어두운 배경 · 청록 숫자 · 큰 숫자"), ("tn-soft", "밝은 카드형", "연한 배경 · 보라 · 둥근 모서리 · 그림자")]
    card = ('<div class="tnx"><div class="tnh">이번 주 팀 할 일</div><div class="tnc"><b>비용 집계 보고</b><span>이준호 · 10/28</span><i>완료</i></div>'
            '<div class="tnc"><b>행사 장소 답사</b><span>정하늘 · 10/30</span><i>완료</i></div></div>')
    return '<div class="tns">' + "".join(f'<div class="tn {c}">{card}<b class="tnn">{n}</b><span class="tnd">{d}</span></div>' for c, n, d in items) + "</div>"

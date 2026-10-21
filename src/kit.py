"""슬라이드 부품. 각 함수는 <section class="slide"> 하나 또는 그 안에 들어갈 HTML 조각을 돌려준다."""
import html as _h

COURSE = "코리안리재보험 AI 업무도구 제작 교육"


def esc(s):
    return _h.escape(s, quote=False)


def _head(title, kick="", sub=""):
    k = f'<div class="kick">{kick}</div>' if kick else ""
    s = f'<div class="s-sub">{sub}</div>' if sub else ""
    return f'{k}<h2 class="s-title">{title}</h2><div class="rule"></div>{s}'


def page(title, body, kick="", sub="", top=False):
    t = _h.escape(title.replace("<br>", " "))
    return (f'<section class="slide" data-title="{t}">'
            f'<div class="topbar"><span>{COURSE}</span><span class="coord"><b>01</b> / <span class="tot"></span></span></div>'
            f'{_head(title, kick, sub)}<div class="body{" top" if top else ""}">{body}</div></section>')


def cover(lines, lead, meta, part):
    h1 = "<br>".join(lines)
    m = "".join(f'<div class="it"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in meta)
    return (f'<section class="slide cover active" data-title="표지"><div class="wrap">'
            f'<div class="ckick"><span class="bar"></span>{COURSE} · {part}</div>'
            f'<h1>{h1}</h1><p class="lead">{lead}</p><div class="meta">{m}</div></div></section>')


def section(no, title, sub, time=""):  # time은 쓰지 않음 (시각 표기 제거)
    tm = ""
    return (f'<section class="slide section" data-title="{no}. {_h.escape(title)}">'
            f'<div class="ghost">{no}</div><div class="sno">{no}</div><h2>{title}</h2><p>{sub}</p>{tm}</section>')


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="ctable {cls}"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'


def cards(items, cols=3):
    out = []
    for i, it in enumerate(items):
        t, d = it[0], it[1]
        n = it[2] if len(it) > 2 else f"{i + 1:02d}"
        out.append(f'<div class="card"><span class="n">{n}</span><h3>{t}</h3><p>{d}</p></div>')
    return f'<div class="cards c{cols}">{"".join(out)}</div>'


def steps(items):
    out = "".join(f'<div class="li"><span class="num">{i + 1}</span><div class="tx"><h4>{t}</h4><p>{d}</p></div></div>'
                  for i, (t, d) in enumerate(items))
    return f'<div class="biglist">{out}</div>'


def flow(items, hl=None):
    arrow = '<div class="arrow">→</div>'
    parts = []
    for i, (t, d) in enumerate(items):
        c = " hl" if hl is not None and i == hl else ""
        parts.append(f'<div class="step{c}"><div class="si">{i + 1:02d}</div><div class="sn">{t}</div><div class="sd">{d}</div></div>')
    return f'<div class="pipe">{arrow.join(parts)}</div>'


def prompt(text, label="요청문", file=None, sm=False):
    f = f' data-file="{file}"' if file else ""
    return (f'<div class="code prompt{" sm" if sm else ""}"{f}><div class="bar"><span class="plabel">{label}</span></div>'
            f'<pre><code>{esc(text)}</code></pre></div>')


def note(k, text, kind=""):
    return f'<div class="note {kind}"><span class="nk">{k}</span><span class="nt">{text}</span></div>'


def two(a, b, cls=""):
    return f'<div class="twocol {cls}"><div>{a}</div><div>{b}</div></div>'


def three(a, b, c):
    return f'<div class="threecol"><div>{a}</div><div>{b}</div><div>{c}</div></div>'


def pane(title, body, kind=""):
    return f'<div class="pane {kind}"><h4>{title}</h4>{body}</div>'


def ul(items):
    return "<ul class='ul'>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def shot(desc, path=""):
    p = f'<span class="nm2">{path}</span>' if path else ""
    return f'<div class="need-img"><span class="nk">화면 캡처 자리</span><span class="nd">{desc}</span>{p}</div>'


def chat(user, ai):
    return (f'<div class="chat"><div class="u"><span class="who">나</span><div class="bub">{user}</div></div>'
            f'<div class="a"><span class="who ai">AI</span><div class="bub">{ai}</div></div></div>')


def lab(no, title, goal, todo, out, time=""):
    li = "".join(f"<li>{x}</li>" for x in todo)
    return (f'<section class="slide labcover" data-title="[실습 {no}] {_h.escape(title)}">'
            f'<div class="topbar"><span>{COURSE}</span><span class="coord"><b>01</b> / <span class="tot"></span></span></div>'
            f'<div class="labwrap"><div class="labl"><div class="lflag">실습 {no}{" · " + time if time else ""}</div><h2>{title}</h2><p class="goal">{goal}</p>'
            f'<div class="lout"><span>산출물</span>{out}</div></div>'
            f'<div class="labr"><div class="lh">순서</div><ol>{li}</ol></div></div></section>')


def big(items):
    out = "".join(f'<div class="stat"><div class="num">{n}</div><div class="lab">{l}</div></div>' for n, l in items)
    return f'<div class="stat-row">{out}</div>'


def tools3(rows):
    """ChatGPT 기준 · Claude · Gemini 위치표."""
    return table(["", '<span class="tg g">ChatGPT · 기준</span>', '<span class="tg c">Claude</span>', '<span class="tg m">Gemini</span>'], rows, "tools")


def img(path, cap="", light=False):
    c = f'<div class="cap">{cap}</div>' if cap else ""
    return f'<figure class="realshot{" light" if light else ""}"><img src="{path}" alt="{_h.escape(cap)}">{c}</figure>'

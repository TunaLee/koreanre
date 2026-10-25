"""최신 흐름 · 출처는 data/트렌드_출처.md (2026-10-21 확인)."""
import fig
from kit import big, note, page, table, two

TREND = [  # (시기, 제목, 설명, 강조)
    ("2022.11", "채팅", "ChatGPT 공개 · 묻고 답하기", False),
    ("2024.11", "연결 표준 MCP", "AI와 업무 시스템을 잇는 공통 규격 공개", False),
    ("2025.07", "에이전트", "AI가 여러 단계를 직접 실행 (ChatGPT agent)", False),
    ("2025.10", "스킬", "업무 지침을 저장해 꺼내 쓰는 Agent Skills 발표 → 12월 오픈 표준", False),
    ("2026.07", "ChatGPT 플러그인", "스킬 + 앱을 묶어 한 번에 설치", True),
    ("2026.09", "Gemini 스킬", "같은 SKILL.md 표준 · Gem은 스킬로 이전", True),
]


def trend_src():
    return "출처: Anthropic 발표 (2024.11 · 2025.10 · 2025.12) · OpenAI 도움말 (2025.07 · 2026.07) · Google Workspace 공지 (2026.09)"


def same_standard():
    return page("세 회사의 공통 스킬 표준", table(["", "발표", "내용"], [
        ["<b>Anthropic · Claude</b>", "2025.10 발표 · 2025.12 오픈 표준", "Agent Skills · SKILL.md 공개 (agentskills.io)"],
        ["<b>OpenAI · ChatGPT</b>", "2026.07 플러그인 디렉터리", "스킬 · 앱을 플러그인으로 묶어 설치"],
        ["<b>Google · Gemini</b>", "2026.09 발표 · 10월 배포 시작", "「SKILL.md 표준」 기반 스킬 · Gem은 스킬로 자동 이전"],
    ]) + note("의미", "한 번 만든 스킬 구조가 <b>세 툴 어디서나 같은 4칸</b> · 툴을 바꿔도 다시 쓸 수 있음", "red")
        + note("출처", "anthropic.com · claude.com/blog/skills · help.openai.com · workspaceupdates.googleblog.com (2026-10-21 확인)"),
        kick="최신 흐름")


def mcp():
    return page("연결 표준 MCP", '<div class="parts">'
                + fig._tile("plug", "MCP", "AI와 시트 · 메일 · 일정을<br>잇는 공통 규격", "core")
                + '<div class="plus">→</div>'
                + fig._tile("nodes", "공동 관리", "2025.12 리눅스 재단 산하로<br>Anthropic · OpenAI · Block 공동 설립")
                + '<div class="plus">→</div>'
                + fig._tile("globe", "어디서나", "ChatGPT · Gemini · Copilot 채택<br>공개 서버 1만 개 이상")
                + "</div>"
                + note("의미", "플러그인 · 커넥터 연결 방식이 툴마다 비슷해지는 이유")
                + note("출처", "Anthropic 「MCP 기증 · Agentic AI Foundation 설립」 (2025-12-09)"), kick="최신 흐름")


def work_stats():
    return page("AI 사용자가 느낀 변화", big([
        ("66%", "고부가 업무에 쓰는 시간 증가"),
        ("58%", "1년 전에는 불가능했던 결과물 작성"),
        ("44.5%", "국민 생성형 AI 경험률 · 1년 새 +11.2%p"),
    ]) + note("출처", "Microsoft Work Trend Index 2026 (2026-05-05 · 10개국 AI 사용자 2만 명) · "
                     "과기정통부 「2025 인터넷이용실태조사」 (2026-03-31)"), kick="최신 흐름")


HORIZON = [  # (모델, 공개, 시간) · METR Time Horizon 1.1 원자료 · 50% 성공 기준
    ("GPT-5", "2025.08", 203 / 60),
    ("GPT-5.2", "2025.12", 352 / 60),
    ("Claude Opus 4.6", "2026.02", 719 / 60),
    ("Claude Mythos Preview", "2026.04", 1045 / 60),
]


def horizon():
    """무어의 법칙처럼 · AI가 혼자 끝내는 작업 길이."""
    mx = 18
    bars = ""
    for i, (m, d, h) in enumerate(HORIZON):
        w = h / mx * 100
        last = i == len(HORIZON) - 1
        bars += (f'<div class="hz-r"><div class="hz-m"><b>{m}</b><span>{d}</span></div>'
                 f'<div class="hz-b"><i style="width:{w:.0f}%" class="{"on" if last else ""}"></i><em>약 {h:.0f}시간{"+" if last else ""}</em></div></div>')
    return page("무어의 법칙처럼 늘어나는 AI 작업 길이", two(
        f'<div class="hz"><div class="hz-h">AI가 혼자 끝내는 작업 길이 · 사람 전문가 기준 · 절반 성공</div>{bars}</div>',
        '<div class="hz-cmp"><div><small>무어의 법칙</small><b>약 2년</b><span>반도체 집적도 2배</span></div>'
        '<div class="on"><small>AI 작업 길이</small><b>약 3개월</b><span>2024년 이후 2배 (METR)</span></div></div>', "w")
        + note("그래서", "몇 분짜리 답변 → <b>몇 시간짜리 업무</b> · 검색 · 정리 · 파일 만들기를 이어서 하는 에이전트가 가능해짐", "red")
        + note("출처", "METR Time Horizon 1.1 (2026-01-29) · metr.org/time-horizons · 소프트웨어 작업 기준 · 16시간 이상은 측정 불안정"),
        kick="최신 흐름")


def three_levels():
    """같은 업무를 채팅 · 에이전트 · 스킬로."""
    cols = [
        ("채팅", "2022 ~", "「최근 3년 자연재해 피해액 알려 줘」",
         ["기억에 의존한 답 · 출처 없음"], ["자료 찾기 · 표 · 차트 · 보고서 전부"], "답 한 덩어리"),
        ("에이전트", "2025 ~", "「공식 자료를 찾아 대시보드 HTML로 만들어 줘」",
         ["웹 검색 여러 번 · 표 정리", "HTML 작성 · 미리보기"], ["출처 링크 확인 · 수치 대조"], "출처 달린 대시보드"),
        ("스킬", "2025.10 ~", "(CSV 첨부) 「대시보드로 정리해 줘」",
         ["저장된 내 기준으로 바로 제작", "카드 · 출처 · 인쇄 · 수정용 요청문"], ["검수만"], "매번 같은 모양의 결과"),
    ]
    out = ""
    for i, (t, when, req, ai, me, res) in enumerate(cols):
        out += (f'<div class="tl3{" on" if i else ""}"><div class="tl3-h"><b>{t}</b><span>{when}</span></div>'
                f'<div class="tl3-q">{req}</div>'
                f'<div class="tl3-k">AI가 하는 일</div><ul>{"".join(f"<li>{x}</li>" for x in ai)}</ul>'
                f'<div class="tl3-k">사람이 하는 일</div><ul>{"".join(f"<li>{x}</li>" for x in me)}</ul>'
                f'<div class="tl3-r">{res}</div></div>')
        if i < 2:
            out += '<div class="tl3-a">→</div>'
    return page("같은 업무, 세 단계", f'<div class="tl3s">{out}</div>'
                + note("오늘 실습", "실습 3 · 4 = 에이전트로 만들기 · 실습 6 = 스킬로 저장", "red"), kick="최신 흐름")

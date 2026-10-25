"""최신 흐름 · 출처는 data/트렌드_출처.md (2026-10-21 확인)."""
import fig
from kit import big, note, page, pane, table, two, ul

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


def two_modes():
    """대화형 → 위임형 (같은 업무)."""
    def col(cls, title, when, ask, steps, me, res):
        li = "".join(f"<li>{x}</li>" for x in steps)
        return (f'<div class="md {cls}"><div class="md-h"><b>{title}</b><span>{when}</span></div><div class="md-q">{ask}</div>'
                f'<div class="md-k">AI</div><ul>{li}</ul><div class="md-k">사람</div><p>{me}</p><div class="md-r">{res}</div></div>')
    a = col("", "대화형", "묻고 답하기", "「최근 3년 자연재해 피해액 알려 줘」",
            ["아는 범위에서 글로 답함", "자료를 찾거나 파일을 만들지 못함"], "자료 찾기 · 표 · 차트 · 보고서를 직접", "답 한 덩어리")
    b = col("on", "위임형 · 에이전트", "목표를 맡기기", "「공식 자료를 찾아 출처 달린 대시보드로 만들어 줘」",
            ["웹 검색을 여러 번 · 숫자 확인", "표로 정리 → HTML 작성 · 미리보기", "부족하면 다시 찾기"], "목표를 정하고 결과를 확인", "출처 달린 결과물")
    return page("대화형에서 위임형으로", f'<div class="mds">{a}<div class="md-a">→</div>{b}</div>'
                + note("바뀐 것", "AI가 <b>답</b>을 주는 데서 → <b>일을 맡아 끝까지</b> 하는 데로 · 사람 역할은 목표 · 확인", "red"), kick="에이전트")


def tool_use():
    """위임이 가능해진 이유: 스스로 도구를 쓴다."""
    tools = [("search", "웹 검색"), ("folder", "파일 읽기"), ("chart", "코드 실행 · 계산"), ("mail", "메일 · 일정"), ("plug", "사내 시스템 · MCP")]
    chips = "".join(f'<div class="tu-t">{fig.ic(i)}<span>{t}</span></div>' for i, t in tools)
    loop = ('<div class="tu-l">'
            '<div class="tu-s"><b>① 판단</b><span>지금 무엇이 필요한가</span></div><i>→</i>'
            '<div class="tu-s on"><b>② 도구 호출</b><span>검색 · 파일 · 계산 · 연결된 앱</span></div><i>→</i>'
            '<div class="tu-s"><b>③ 결과 확인</b><span>충분한가 · 맞는가</span></div><i>→</i>'
            '<div class="tu-s"><b>④ 다음 행동</b><span>다시 호출 또는 끝내기</span></div></div>')
    return page("위임이 가능해진 이유: 스스로 도구 사용", two(
        pane("도구 없는 AI", ul(["다음 글자를 확률로 이어 쓰기만", "계산 · 최신 정보 · 파일 · 메일 불가", "결과를 사람이 옮겨서 실행"]), "bad"),
        pane("도구를 쓰는 AI", ul(["필요할 때 도구를 <b>스스로</b> 골라 호출", "도구 결과를 읽고 다음 행동 결정", "여러 단계를 이어서 끝까지"]), "good"))
        + loop + f'<div class="tu-ts">{chips}</div>', kick="에이전트")


def agent_background():
    """오전 · 오후 공통 도입: 에이전트 배경."""
    return [page("채팅에서 에이전트로", fig.timeline(TREND), kick="최신 흐름", sub=trend_src()),
            two_modes(), tool_use(), horizon()]


def tool_kinds():
    """도구의 세 종류."""
    return page("에이전트가 쓰는 도구 세 종류", table(["종류", "예", "연결 방법"], [
        ["<b>기본 도구</b>", "웹 검색 · 파일 분석(코드 실행) · 이미지 생성", "켜져 있음 · 입력창 <b>+</b>에서 선택"],
        ["<b>앱 연결</b>", "Google Drive · Calendar · Gmail · Notion · Slack", "로그인 한 번 · 허용한 범위만 조회"],
        ["<b>MCP 서버</b>", "공공 통계 · 공시 · 법령 · 사내 시스템", "주소 등록 · 공개 서버 또는 <b>직접 만든 서버</b>"],
    ]) + note("오늘 오전", "<b>앱 연결</b>로 시트 · 캘린더를 읽고, 업무 지침은 <b>스킬</b>로 저장", "red"), kick="도구")


def external_tools():
    """밖에서 가져다 쓰는 MCP 서버 예 (재보험 업무 관점)."""
    return page("가져다 쓰는 외부 도구 · MCP 서버", table(["분야", "서버", "재보험 업무에서"], [
        ["<b>국가통계</b>", "korea-stats-mcp (KOSIS)", "재해 · 인구 · 산업 통계로 위험 추이"],
        ["<b>기업 공시</b>", "DART-mcp-server", "원수사 · 경쟁사 공시 · 재무 정보"],
        ["<b>법령</b>", "korean-law-mcp", "보험업법 · 시행령 · 행정규칙 조회"],
        ["<b>공공데이터</b>", "data-go-mcp-servers", "공공데이터포털의 여러 API를 도구로"],
        ["<b>기술 문서</b>", "Microsoft Learn MCP", "엑셀 · 파워포인트 · 스크립트 사용법"],
    ]) + note("주의", "공개 서버는 만든 곳 · 권한 범위를 먼저 확인 · 회사 데이터는 사내 승인 서버로만", "red")
        + note("출처", "Awesome MCP Korea 목록 · Microsoft Learn MCP 공식 문서"), kick="도구")


def made_tools():
    """다른 현장 과정에서 직접 만든 도구 → 재보험 업무라면."""
    return page("직접 만든 도구 예", table(["유형", "다른 현장 과정에서 만든 도구", "재보험 업무라면"], [
        ["<b>조회</b>", "설비 생산량 · 불량 조회 (철강) · Lot 이력 · 정비 기록 조회 (반도체)", "계약 · 출재 조건 조회"],
        ["<b>계산</b>", "근무조별 불량률 · 정확한 계산기 (철강)", "손해율 · 보유 · 출재 비율 계산"],
        ["<b>문서 검색</b>", "사내 규정 검색 · 조항 원문 추적 (철강) · 기술 문서 검색 서버 (반도체)", "약관 · 특약 조항 검색"],
        ["<b>기록</b>", "메모 조회 · 저장 · 수정 · 삭제 (반도체)", "업무 일지 · 회의 결정 기록"],
        ["<b>판정 · 넘기기</b>", "이상 이벤트 판정 → 조사 (반도체) · 규정에 없으면 담당자에게 (철강)", "심사 필요 건 분류 · 승인 요청"],
        ["<b>안전장치</b>", "운영 DB 쓰기 차단 (철강)", "원본 데이터 수정 차단"],
    ]) + note("공통점", "도구 = <b>이름 · 설명 · 입력</b>을 정한 기능 · AI는 설명을 보고 고르고, 실행은 프로그램이", "red"), kick="도구")

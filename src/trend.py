"""최신 흐름 · 출처는 data/트렌드_출처.md (2026-10-21 확인)."""
import fig
from kit import big, note, page, table

TREND = [  # (시기, 제목, 설명, 강조)
    ("2022.11", "채팅", "ChatGPT 공개 · 묻고 답하기", False),
    ("2024.11", "연결 규격 MCP", "AI와 업무 시스템을 잇는 공통 규격 공개", False),
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

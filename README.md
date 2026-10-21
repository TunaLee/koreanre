# AI 업무도구 제작 교육 · 강의 슬라이드

- `docs/` — 배포 폴더 (GitHub Pages 소스). `index.html` · `am.html`(오전) · `pm.html`(오후) · `dl/`(실습 자료)
- `src/` — 슬라이드 원본. `am.py` 오전 · `pm.py` 오후 · `kit.py` 부품 · `theme.css` · `template.html`
- `data/` — 실습 자료. `오전/`은 `src/make_data.py`로 생성한 더미, `오후_공통데이터.csv`는 공식 통계

## 빌드

```bash
python3 src/make_data.py --week 2026-10-26   # 교육 주 월요일 · 캘린더 · 마감일 기준
python3 src/build.py                          # docs/ 갱신
```

## 배포

GitHub 저장소 Settings → Pages → Branch `main` · 폴더 `/docs`

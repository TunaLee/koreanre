// 미리보기용: google.script.run 을 흉내 내는 가짜 서버 (Code.gs 와 같은 동작 · 메모리 저장)
(function () {
  const svg = (c, t) => 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" width="88" height="88"><rect width="88" height="88" fill="${c}"/>` +
    `<text x="44" y="50" font-size="13" text-anchor="middle" fill="#fff" font-family="sans-serif">${t}</text></svg>`);
  const d = n => { const x = new Date(Date.now() - new Date().getTimezoneOffset() * 60000); x.setDate(x.getDate() + n); return x.toISOString().slice(0, 10); };
  const db = [
    { id: 'a1', title: '연말 행사 장소 섭외', owner: '정하늘', due: d(-5), status: '진행 중', progress: 40, memo: '후보 3곳 중 2곳 회신',
      files: [{ id: 'f1', name: '장소A_외관.jpg', type: 'image/jpeg', url: '#' }, { id: 'f2', name: '장소B_내부.jpg', type: 'image/jpeg', url: '#' }], updated: '' },
    { id: 'a2', title: '3분기 비용 집계', owner: '이준호', due: d(1), status: '완료', progress: 100, memo: '',
      files: [{ id: 'f3', name: '3분기_비용.xlsx', type: 'application/vnd.ms-excel', url: '#' }], updated: '' },
    { id: 'a3', title: '협력사 명단 갱신', owner: '최유진', due: d(4), status: '진행 중', progress: 60, memo: '변경 업체 연락처 확인 중', files: [], updated: '' },
    { id: 'a4', title: '업무 매뉴얼 개정', owner: '김서연', due: d(9), status: '할 일', progress: 0, memo: '', files: [], updated: '' },
    { id: 'a5', title: '자료 보관 기준 정비', owner: '박지민', due: d(3), status: '보류', progress: 20, memo: '담당 부서 협의 대기', files: [], updated: '' },
  ];
  const thumbs = { f1: svg('#4C8BF5', '장소 A'), f2: svg('#13A06B', '장소 B') };
  const copy = () => JSON.parse(JSON.stringify(db));
  const api = {
    getTasks: () => copy(),
    saveTask: t => {
      if (!t.id) db.push({ ...t, id: Math.random().toString(16).slice(2, 10), progress: Number(t.progress) || 0, files: [], updated: '' });
      else Object.assign(db.find(x => x.id === t.id), { ...t, progress: Number(t.progress) || 0 });
      return copy();
    },
    deleteTask: id => { db.splice(db.findIndex(x => x.id === id), 1); return copy(); },
    uploadFile: (id, name, type) => {
      const fid = 'u' + Date.now();
      if (String(type).startsWith('image/')) thumbs[fid] = svg('#E8002D', name.slice(0, 8));
      db.find(x => x.id === id).files.push({ id: fid, name, type, url: '#' });
      return copy();
    },
    getThumb: fid => thumbs[fid] || '',
  };
  function runner(ok, fail) {
    return new Proxy({}, {
      get(_, k) {
        if (k === 'withSuccessHandler') return f => runner(f, fail);
        if (k === 'withFailureHandler') return f => runner(ok, f);
        return (...a) => setTimeout(() => { try { ok && ok(api[k](...a)); } catch (e) { fail && fail(e); } }, 30);
      },
    });
  }
  window.google = { script: { run: runner(null, null) } };
})();

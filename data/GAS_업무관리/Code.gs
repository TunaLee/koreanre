/**
 * 내 업무 관리 웹 — 기록은 Google 시트, 파일은 Google 드라이브
 * 사용: 새 Google 시트 → 확장 프로그램 → Apps Script → 이 파일과 Index.html 붙여 넣기 → 배포
 */
const SHEET = '업무';
const FOLDER = '업무관리_파일';
const HEAD = ['ID', '업무명', '담당', '마감일', '상태', '진행률', '메모', '파일', '수정일'];

function doGet() {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('내 업무 관리')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

function sheet_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sh = ss.getSheetByName(SHEET);
  if (!sh) {
    sh = ss.insertSheet(SHEET);
    sh.appendRow(HEAD);
    sh.setFrozenRows(1);
  }
  return sh;
}

function folder_() {
  const props = PropertiesService.getScriptProperties();
  const id = props.getProperty('FOLDER_ID');
  if (id) {
    try { return DriveApp.getFolderById(id); } catch (e) { /* 지워졌으면 새로 만든다 */ }
  }
  const it = DriveApp.getFoldersByName(FOLDER);
  const folder = it.hasNext() ? it.next() : DriveApp.createFolder(FOLDER);
  props.setProperty('FOLDER_ID', folder.getId());
  return folder;
}

function fmt_(v, pattern) {
  return v instanceof Date ? Utilities.formatDate(v, Session.getScriptTimeZone(), pattern) : String(v || '');
}

/** 업무 목록 전체 */
function getTasks() {
  const rows = sheet_().getDataRange().getValues().slice(1);
  return rows.filter(r => r[0] !== '').map(r => ({
    id: String(r[0]),
    title: String(r[1]),
    owner: String(r[2]),
    due: fmt_(r[3], 'yyyy-MM-dd'),
    status: String(r[4] || '할 일'),
    progress: Number(r[5]) || 0,
    memo: String(r[6] || ''),
    files: r[7] ? JSON.parse(r[7]) : [],
    updated: fmt_(r[8], 'yyyy-MM-dd HH:mm'),
  }));
}

/** 새 업무 추가 · 기존 업무 수정 (id 유무로 구분) */
function saveTask(t) {
  const sh = sheet_();
  const progress = Math.max(0, Math.min(100, Number(t.progress) || 0));
  if (!t.id) {
    sh.appendRow([Utilities.getUuid().slice(0, 8), t.title, t.owner, t.due, t.status || '할 일', progress, t.memo || '', '[]', new Date()]);
  } else {
    const row = findRow_(t.id);
    sh.getRange(row, 2, 1, 6).setValues([[t.title, t.owner, t.due, t.status, progress, t.memo || '']]);
    sh.getRange(row, 9).setValue(new Date());
  }
  return getTasks();
}

function deleteTask(id) {
  sheet_().deleteRow(findRow_(id));
  return getTasks();
}

/** 파일 한 개를 드라이브 폴더에 저장하고 업무 줄에 기록 */
function uploadFile(id, name, type, base64) {
  const blob = Utilities.newBlob(Utilities.base64Decode(base64), type || 'application/octet-stream', name);
  const file = folder_().createFile(blob);
  const sh = sheet_();
  const row = findRow_(id);
  const files = JSON.parse(sh.getRange(row, 8).getValue() || '[]');
  files.push({ id: file.getId(), name: name, type: type, url: file.getUrl() });
  sh.getRange(row, 8).setValue(JSON.stringify(files));
  sh.getRange(row, 9).setValue(new Date());
  return getTasks();
}

/** 이미지 썸네일 (data URL). 썸네일이 아직 없으면 2MB 이하 원본으로 대신 */
function getThumb(fileId) {
  const file = DriveApp.getFileById(fileId);
  let blob = null;
  try { blob = file.getThumbnail(); } catch (e) { blob = null; }
  if (!blob && String(file.getMimeType()).indexOf('image/') === 0 && file.getSize() < 2 * 1024 * 1024) {
    blob = file.getBlob();
  }
  return blob ? 'data:' + blob.getContentType() + ';base64,' + Utilities.base64Encode(blob.getBytes()) : '';
}

function findRow_(id) {
  const sh = sheet_();
  const ids = sh.getRange(1, 1, sh.getLastRow(), 1).getValues().map(r => String(r[0]));
  const i = ids.indexOf(String(id));
  if (i < 1) throw new Error('업무를 찾을 수 없습니다: ' + id);
  return i + 1;
}

<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Catatan Kas Bulanan</title>
<meta name="description" content="Pelacak pengeluaran &amp; pemasukan harian yang sederhana — transport, makan &amp; minuman, dan jajan — dengan ringkasan per hari, minggu, dan bulan.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=IBM+Plex+Mono:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<div class="wrap">

  <header class="top">
    <div class="label">Catatan kas bulanan</div>
    <h1>Ke mana perginya uangmu bulan ini?</h1>
    <div class="field" style="max-width:220px;margin-top:6px;">
      <label for="f-bulan">Bulan</label>
      <select id="f-bulan"></select>
    </div>
  </header>

  <div class="balance-row">
    <div class="balance-card">
      <div class="k">Masuk</div>
      <div class="v pos" id="sum-masuk">Rp 0</div>
    </div>
    <div class="balance-card">
      <div class="k">Keluar</div>
      <div class="v neg" id="sum-keluar">Rp 0</div>
    </div>
    <div class="balance-card saldo">
      <div class="k">Saldo <button type="button" id="btn-toggle-saldo" class="eye-btn" title="Sembunyikan/tampilkan saldo">👁</button></div>
      <div class="v" id="sum-saldo">Rp 0</div>
    </div>
  </div>

  <div class="card">
    <div class="crumbs" id="crumbs"></div>
    <div id="stepper"></div>
  </div>

  <div class="card">
    <h2 class="section-title">Total pengeluaran per periode</h2>
    <div class="cat-summary" id="periode-summary"></div>
  </div>

  <div class="card" id="card-summary">
    <h2 class="section-title">Ringkasan per kategori</h2>
    <div class="cat-summary" id="cat-summary"></div>
  </div>

  <div class="card">
    <h2 class="section-title">Riwayat transaksi</h2>
    <ul class="history" id="history"></ul>
  </div>

  <footer class="note">Ringkasan &amp; riwayat mengikuti bulan yang dipilih di atas.<br>Data hanya tersimpan selama halaman ini terbuka &mdash; segarkan halaman akan mengosongkan catatan.</footer>
</div>

<script src="assets/app.js"></script>
</body>
</html>

:root {
  --paper: #F5F1E6;
  --paper-raised: #FBF8F1;
  --ink: #26314A;
  --ink-soft: #5B6478;
  --rule: #D9D0B9;
  --green: #3E7C59;
  --green-soft: #E4EFE7;
  --rust: #B5473A;
  --rust-soft: #F5E5E1;
  --gold: #B98A2E;
  --shadow: rgba(38,49,74,0.10);
  box-sizing: border-box;
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #1C2030;
    --paper-raised: #262B3D;
    --ink: #ECE7DA;
    --ink-soft: #A8AEC0;
    --rule: #3A3F54;
    --green: #6FBE8F;
    --green-soft: #223A2E;
    --rust: #E08672;
    --rust-soft: #3C2422;
    --gold: #E0B65C;
    --shadow: rgba(0,0,0,0.35);
  }
}
:root[data-theme="dark"] {
  --paper: #1C2030;
  --paper-raised: #262B3D;
  --ink: #ECE7DA;
  --ink-soft: #A8AEC0;
  --rule: #3A3F54;
  --green: #6FBE8F;
  --green-soft: #223A2E;
  --rust: #E08672;
  --rust-soft: #3C2422;
  --gold: #E0B65C;
  --shadow: rgba(0,0,0,0.35);
}
html { scroll-padding-top: env(safe-area-inset-top, 0px); }
* { box-sizing: border-box; }
html, body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}
body {
  min-height: 100%;
  padding: 28px 16px 60px;
}
.wrap { max-width: 640px; margin: 0 auto; }

header.top { margin-bottom: 22px; }
header.top .label {
  font-size: 12.5px;
  color: var(--ink-soft);
  letter-spacing: 0.02em;
  margin-bottom: 4px;
}
h1 {
  font-family: 'Source Serif 4', Georgia, serif;
  font-weight: 600;
  font-size: 27px;
  margin: 0 0 18px;
  line-height: 1.25;
}

.balance-row {
  display: flex;
  gap: 10px;
  margin-bottom: 22px;
}
.balance-card {
  flex: 1;
  background: var(--paper-raised);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 13px 14px;
}
.balance-card .k { font-size: 12px; color: var(--ink-soft); margin-bottom: 6px; }
.balance-card .v {
  font-family: 'IBM Plex Mono', monospace;
  font-weight: 600;
  font-size: 16.5px;
}
.balance-card.saldo .v { font-size: 19px; }
.eye-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 12px;
  padding: 0 0 0 4px;
  line-height: 1;
  vertical-align: middle;
  opacity: 0.7;
}
.eye-btn:hover { opacity: 1; }
.v.pos { color: var(--green); }
.v.neg { color: var(--rust); }

.card {
  background: var(--paper-raised);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 1px 2px var(--shadow);
}
.crumbs {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 12.5px;
  color: var(--ink-soft);
  margin-bottom: 14px;
  min-height: 16px;
}
.crumbs b { color: var(--ink); font-weight: 600; }

.prompt {
  font-size: 15.5px;
  font-weight: 500;
  margin: 0 0 14px;
}

.choice-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}
.choice-grid.cols-3 { grid-template-columns: 1fr 1fr 1fr; }
.choice-grid.transport { grid-template-columns: 1fr 1fr; }

button.choice {
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 500;
  color: var(--ink);
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 9px;
  padding: 14px 10px;
  cursor: pointer;
  text-align: center;
  transition: border-color 0.15s ease, transform 0.1s ease;
}
button.choice:hover { border-color: var(--gold); }
button.choice:active { transform: scale(0.98); }
button.choice.masuk { border-color: var(--green); color: var(--green); }
button.choice.keluar { border-color: var(--rust); color: var(--rust); }

.field { margin-bottom: 14px; }
.field label {
  display: block;
  font-size: 12.5px;
  color: var(--ink-soft);
  margin-bottom: 6px;
}
.field input {
  width: 100%;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 16px;
  padding: 11px 12px;
  border: 1px solid var(--rule);
  border-radius: 8px;
  background: var(--paper);
  color: var(--ink);
}
.field input:focus { outline: 2px solid var(--gold); outline-offset: 1px; }
.field input#f-nominal { font-weight: 600; }
.field select {
  width: 100%;
  font-family: 'IBM Plex Mono', monospace;
  font-size: 14.5px;
  font-weight: 500;
  padding: 9px 10px;
  border: 1px solid var(--rule);
  border-radius: 8px;
  background: var(--paper-raised);
  color: var(--ink);
}
.field select:focus { outline: 2px solid var(--gold); outline-offset: 1px; }

.row-btns { display: flex; gap: 10px; margin-top: 4px; }
.btn {
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 600;
  padding: 12px 18px;
  border-radius: 8px;
  border: none;
  cursor: pointer;
}
.btn-primary { background: var(--ink); color: var(--paper); flex: 1; }
.btn-primary:disabled { opacity: 0.4; cursor: not-allowed; }
.btn-ghost { background: transparent; color: var(--ink-soft); border: 1px solid var(--rule); }

h2.section-title {
  font-family: 'Source Serif 4', Georgia, serif;
  font-size: 16.5px;
  font-weight: 600;
  margin: 0 0 12px;
}

.cat-summary { display: flex; flex-direction: column; gap: 9px; margin-bottom: 4px; }
.cat-summary .item {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  font-size: 14px;
  border-bottom: 1px dashed var(--rule);
  padding-bottom: 8px;
}
.cat-summary .item .n { color: var(--ink-soft); }
.cat-summary .item .a { font-family: 'IBM Plex Mono', monospace; font-weight: 500; }

ul.history { list-style: none; margin: 0; padding: 0; }
ul.history li {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 11px 0;
  border-bottom: 1px solid var(--rule);
}
ul.history li:last-child { border-bottom: none; }
.tag {
  font-size: 11px;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 20px;
  white-space: nowrap;
  flex-shrink: 0;
}
.tag.masuk { background: var(--green-soft); color: var(--green); }
.tag.keluar { background: var(--rust-soft); color: var(--rust); }
.hist-main { flex: 1; min-width: 0; }
.hist-name { font-size: 14px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.hist-date { font-size: 11.5px; color: var(--ink-soft); margin-top: 2px; }
.hist-amt { font-family: 'IBM Plex Mono', monospace; font-weight: 600; font-size: 14px; flex-shrink: 0; }
.hist-del {
  background: none; border: none; color: var(--ink-soft);
  font-size: 17px; cursor: pointer; padding: 2px 4px; flex-shrink: 0;
  line-height: 1;
}
.hist-del:hover { color: var(--rust); }
.empty { color: var(--ink-soft); font-size: 13.5px; padding: 6px 0 2px; }

footer.note {
  font-size: 12px;
  color: var(--ink-soft);
  text-align: center;
  margin-top: 26px;
  line-height: 1.6;
}

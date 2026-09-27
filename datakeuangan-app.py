import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Catatan Kas Bulanan", page_icon="📒", layout="centered")

HTML = r"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Catatan Kas Bulanan</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=IBM+Plex+Mono:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
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
</style>
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

<script>
(function () {
  "use strict";

  var TRANSPORT_MODES = ["KRL", "LRT", "Angkot", "Transjakarta", "Gojek"];
  var MONTHS = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"];
  var MONTHS_SHORT = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"];
  var DAYS = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"];

  function todayISO() {
    var d = new Date();
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + day;
  }

  function toISO(d) {
    var m = String(d.getMonth() + 1).padStart(2, "0");
    var day = String(d.getDate()).padStart(2, "0");
    return d.getFullYear() + "-" + m + "-" + day;
  }

  function currentWeekRangeISO() {
    var now = new Date();
    var dow = now.getDay(); // 0=Minggu..6=Sabtu
    var diffToMonday = (dow === 0) ? -6 : (1 - dow);
    var monday = new Date(now);
    monday.setDate(now.getDate() + diffToMonday);
    var sunday = new Date(monday);
    sunday.setDate(monday.getDate() + 6);
    return { start: toISO(monday), end: toISO(sunday), mondayObj: monday, sundayObj: sunday };
  }

  function parseISO(iso) {
    var parts = iso.split("-");
    return new Date(parseInt(parts[0], 10), parseInt(parts[1], 10) - 1, parseInt(parts[2], 10));
  }

  function formatHariTanggal(dateObj) {
    return DAYS[dateObj.getDay()] + ", " + dateObj.getDate() + " " + MONTHS_SHORT[dateObj.getMonth()];
  }
  var transactions = [];
  var nextId = 1;
  var selectedMonth = new Date().getMonth(); // 0 = Januari
  var saldoHidden = false;

  function initMonthSelect() {
    var sel = document.getElementById("f-bulan");
    MONTHS.forEach(function (m, i) {
      var opt = document.createElement("option");
      opt.value = i;
      opt.textContent = m;
      if (i === selectedMonth) opt.selected = true;
      sel.appendChild(opt);
    });
    sel.onchange = function () {
      selectedMonth = parseInt(sel.value, 10);
      renderPeriodeSummary();
      renderSummary();
      renderHistory();
    };
  }

  // step: 'root' | 'masuk' | 'pengeluaran' | 'transport' | 'makan' | 'jajan'
  var step = "root";
  var draft = {}; // holds selections in progress (e.g. moda)

  function formatRupiah(n) {
    n = Math.round(n || 0);
    var neg = n < 0;
    n = Math.abs(n);
    var s = n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return (neg ? "-Rp " : "Rp ") + s;
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }

  function resetToRoot() {
    step = "root";
    draft = {};
    render();
  }

  function goto(next, patch) {
    step = next;
    if (patch) Object.assign(draft, patch);
    render();
  }

  function addTransaction(tx) {
    tx.id = nextId++;
    var d = parseISO(tx.tanggal);
    tx.bulan = d.getMonth();
    transactions.unshift(tx);
    if (selectedMonth !== tx.bulan) {
      selectedMonth = tx.bulan;
      document.getElementById("f-bulan").value = String(tx.bulan);
    }
    resetToRoot();
  }

  function txForSelectedMonth() {
    return transactions.filter(function (t) { return t.bulan === selectedMonth; });
  }

  function deleteTransaction(id) {
    transactions = transactions.filter(function (t) { return t.id !== id; });
    renderPeriodeSummary();
    renderSummary();
    renderHistory();
  }

  // ---------- STEPPER RENDER ----------

  function renderCrumbs() {
    var crumbs = document.getElementById("crumbs");
    var parts = [];
    if (step === "root") { crumbs.innerHTML = ""; return; }
    if (step === "masuk") parts = ["Uang Masuk"];
    if (step === "pengeluaran") parts = ["Pengeluaran"];
    if (step === "transport") parts = ["Pengeluaran", "Transport"];
    if (step === "makan") parts = ["Pengeluaran", "Makan &amp; Minuman"];
    if (step === "jajan") parts = ["Pengeluaran", "Jajan"];
    crumbs.innerHTML = parts.map(function (p, i) {
      return (i === parts.length - 1) ? "<b>" + p + "</b>" : p;
    }).join(" &rsaquo; ");
  }

  function makeAmountForm(opts) {
    // opts: { title, showNameField, nameLabel, namePlaceholder, onSubmit }
    var box = el("div");
    box.appendChild(el("div", "prompt", opts.title));

    if (opts.showNameField) {
      var f1 = el("div", "field");
      f1.appendChild(el("label", null, opts.nameLabel));
      var inp1 = el("input");
      inp1.type = "text";
      inp1.id = "f-nama";
      inp1.placeholder = opts.namePlaceholder;
      f1.appendChild(inp1);
      box.appendChild(f1);
    }

    var fTgl = el("div", "field");
    fTgl.appendChild(el("label", null, "Tanggal"));
    var inpTgl = el("input");
    inpTgl.type = "date";
    inpTgl.id = "f-tanggal";
    inpTgl.value = todayISO();
    fTgl.appendChild(inpTgl);
    box.appendChild(fTgl);

    var f2 = el("div", "field");
    f2.appendChild(el("label", null, "Nominal (Rp)"));
    var inp2 = el("input");
    inp2.type = "number";
    inp2.inputMode = "numeric";
    inp2.id = "f-nominal";
    inp2.placeholder = "0";
    f2.appendChild(inp2);
    box.appendChild(f2);

    var rowBtns = el("div", "row-btns");
    var back = el("button", "btn btn-ghost", "Kembali");
    back.type = "button";
    back.onclick = resetToRoot;
    var save = el("button", "btn btn-primary", "Simpan");
    save.type = "button";
    save.onclick = function () {
      var tanggal = document.getElementById("f-tanggal").value || todayISO();
      var nama = opts.showNameField ? (document.getElementById("f-nama").value || "").trim() : "";
      var nominalRaw = document.getElementById("f-nominal").value;
      var nominal = parseFloat(nominalRaw);
      if (!nominal || nominal <= 0) return;
      if (opts.showNameField && !nama) return;
      opts.onSubmit(nama, nominal, tanggal);
    };
    rowBtns.appendChild(back);
    rowBtns.appendChild(save);
    box.appendChild(rowBtns);
    return box;
  }

  function renderStepper() {
    var host = document.getElementById("stepper");
    host.innerHTML = "";

    if (step === "root") {
      var box = el("div");
      box.appendChild(el("div", "prompt", "Catat transaksi baru:"));
      var grid = el("div", "choice-grid");
      var bMasuk = el("button", "choice masuk", "Uang Masuk");
      bMasuk.type = "button";
      bMasuk.onclick = function () { goto("masuk"); };
      var bKeluar = el("button", "choice keluar", "Pengeluaran");
      bKeluar.type = "button";
      bKeluar.onclick = function () { goto("pengeluaran"); };
      grid.appendChild(bMasuk);
      grid.appendChild(bKeluar);
      box.appendChild(grid);
      host.appendChild(box);

    } else if (step === "masuk") {
      host.appendChild(makeAmountForm({
        title: "Dari mana uang masuk ini?",
        showNameField: true,
        nameLabel: "Sumber (mis. gaji, transfer, THR)",
        namePlaceholder: "Sumber uang masuk",
        onSubmit: function (nama, nominal, tanggal) {
          addTransaction({ jenis: "masuk", kategori: "Uang Masuk", nama: nama, nominal: nominal, tanggal: tanggal });
        }
      }));

    } else if (step === "pengeluaran") {
      var box2 = el("div");
      box2.appendChild(el("div", "prompt", "Pengeluaran ini untuk apa?"));
      var grid2 = el("div", "choice-grid cols-3");
      var cats = [["Transport", "transport"], ["Makan & Minuman", "makan"], ["Jajan", "jajan"]];
      cats.forEach(function (c) {
        var b = el("button", "choice", c[0]);
        b.type = "button";
        b.onclick = function () { goto(c[1]); };
        grid2.appendChild(b);
      });
      box2.appendChild(grid2);
      var back2 = el("div", "row-btns");
      var bb = el("button", "btn btn-ghost", "Kembali");
      bb.type = "button";
      bb.onclick = resetToRoot;
      back2.appendChild(bb);
      box2.appendChild(back2);
      host.appendChild(box2);

    } else if (step === "transport") {
      if (!draft.moda) {
        var box3 = el("div");
        box3.appendChild(el("div", "prompt", "Naik apa?"));
        var grid3 = el("div", "choice-grid transport");
        TRANSPORT_MODES.forEach(function (m) {
          var b = el("button", "choice", m);
          b.type = "button";
          b.onclick = function () { goto("transport", { moda: m }); };
          grid3.appendChild(b);
        });
        box3.appendChild(grid3);
        var back3 = el("div", "row-btns");
        var bb3 = el("button", "btn btn-ghost", "Kembali");
        bb3.type = "button";
        bb3.onclick = function () { goto("pengeluaran"); };
        back3.appendChild(bb3);
        box3.appendChild(back3);
        host.appendChild(box3);
      } else {
        host.appendChild(makeAmountForm({
          title: "Naik " + draft.moda + " &mdash; berapa biayanya?",
          showNameField: false,
          onSubmit: function (nama, nominal, tanggal) {
            addTransaction({ jenis: "keluar", kategori: "Transport", sub: draft.moda, nama: draft.moda, nominal: nominal, tanggal: tanggal });
          }
        }));
      }

    } else if (step === "makan") {
      host.appendChild(makeAmountForm({
        title: "Makan atau minum apa?",
        showNameField: true,
        nameLabel: "Nama makanan / minuman",
        namePlaceholder: "mis. Nasi padang, kopi susu",
        onSubmit: function (nama, nominal, tanggal) {
          addTransaction({ jenis: "keluar", kategori: "Makan & Minuman", nama: nama, nominal: nominal, tanggal: tanggal });
        }
      }));

    } else if (step === "jajan") {
      host.appendChild(makeAmountForm({
        title: "Jajan beli apa?",
        showNameField: true,
        nameLabel: "Nama barang",
        namePlaceholder: "mis. Cemilan, pulsa, aksesoris",
        onSubmit: function (nama, nominal, tanggal) {
          addTransaction({ jenis: "keluar", kategori: "Jajan", nama: nama, nominal: nominal, tanggal: tanggal });
        }
      }));
    }
  }

  // ---------- SUMMARY & HISTORY ----------

  function renderPeriodeSummary() {
    var t = todayISO();
    var week = currentWeekRangeISO();

    var totHari = 0, totMinggu = 0, totBulan = 0;
    transactions.forEach(function (tx) {
      if (tx.jenis !== "keluar") return;
      if (tx.tanggal === t) totHari += tx.nominal;
      if (tx.tanggal >= week.start && tx.tanggal <= week.end) totMinggu += tx.nominal;
      if (tx.bulan === selectedMonth) totBulan += tx.nominal;
    });

    var host = document.getElementById("periode-summary");
    host.innerHTML = "";
    var rows = [
      ["Hari ini (" + formatHariTanggal(parseISO(t)) + ")", totHari],
      ["Minggu ini (" + week.mondayObj.getDate() + " " + MONTHS_SHORT[week.mondayObj.getMonth()] +
        " \u2013 " + week.sundayObj.getDate() + " " + MONTHS_SHORT[week.sundayObj.getMonth()] + ")", totMinggu],
      ["Bulan ini (" + MONTHS[selectedMonth] + ")", totBulan]
    ];
    rows.forEach(function (r) {
      var row = el("div", "item");
      row.appendChild(el("span", "n", r[0]));
      row.appendChild(el("span", "a", formatRupiah(r[1])));
      host.appendChild(row);
    });
  }

  function renderSummary() {
    var masuk = 0, keluar = 0;
    var byCat = {};
    txForSelectedMonth().forEach(function (t) {
      if (t.jenis === "masuk") {
        masuk += t.nominal;
      } else {
        keluar += t.nominal;
        var key = t.kategori === "Transport" ? ("Transport &middot; " + t.sub) : t.kategori;
        byCat[key] = (byCat[key] || 0) + t.nominal;
      }
    });

    document.getElementById("sum-masuk").textContent = formatRupiah(masuk);
    document.getElementById("sum-keluar").textContent = formatRupiah(keluar);
    var saldoEl = document.getElementById("sum-saldo");
    var saldo = masuk - keluar;
    saldoEl.textContent = saldoHidden ? "••••••" : formatRupiah(saldo);
    saldoEl.className = "v " + (saldoHidden ? "" : (saldo >= 0 ? "pos" : "neg"));

    var host = document.getElementById("cat-summary");
    host.innerHTML = "";
    var keys = Object.keys(byCat);
    if (keys.length === 0) {
      host.appendChild(el("div", "empty", "Belum ada pengeluaran tercatat."));
    } else {
      keys.sort(function (a, b) { return byCat[b] - byCat[a]; });
      keys.forEach(function (k) {
        var row = el("div", "item");
        row.innerHTML = "<span class=\"n\">" + k + "</span>";
        var amt = el("span", "a", formatRupiah(byCat[k]));
        row.appendChild(amt);
        host.appendChild(row);
      });
    }
  }

  function renderHistory() {
    var host = document.getElementById("history");
    host.innerHTML = "";
    var list = txForSelectedMonth();
    if (list.length === 0) {
      host.appendChild(el("div", "empty", "Belum ada transaksi di bulan " + MONTHS[selectedMonth] + "."));
      return;
    }
    list.sort(function (a, b) {
      if (a.tanggal !== b.tanggal) return a.tanggal < b.tanggal ? 1 : -1;
      return b.id - a.id;
    });
    list.forEach(function (t) {
      var li = el("li");
      var tag = el("span", "tag " + (t.jenis === "masuk" ? "masuk" : "keluar"),
        t.jenis === "masuk" ? "Masuk" : t.kategori);
      var main = el("div", "hist-main");
      main.appendChild(el("div", "hist-name", t.nama || t.kategori));
      main.appendChild(el("div", "hist-date", formatHariTanggal(parseISO(t.tanggal))));
      var amt = el("span", "hist-amt " + (t.jenis === "masuk" ? "" : ""), (t.jenis === "masuk" ? "+" : "-") + formatRupiah(t.nominal).replace("Rp ", "Rp "));
      amt.style.color = t.jenis === "masuk" ? "var(--green)" : "var(--rust)";
      var del = el("button", "hist-del", "\u00D7");
      del.type = "button";
      del.title = "Hapus";
      del.onclick = function () { deleteTransaction(t.id); };
      li.appendChild(tag);
      li.appendChild(main);
      li.appendChild(amt);
      li.appendChild(del);
      host.appendChild(li);
    });
  }

  function render() {
    renderCrumbs();
    renderStepper();
    renderPeriodeSummary();
    renderSummary();
    renderHistory();
  }

  initMonthSelect();
  document.getElementById("btn-toggle-saldo").onclick = function () {
    saldoHidden = !saldoHidden;
    this.textContent = saldoHidden ? "🙈" : "👁";
    renderSummary();
  };
  render();
})();
</script>
</body>
</html>
"""

components.html(HTML, height=1600, scrolling=True)

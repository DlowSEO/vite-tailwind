// Privacy-friendly event tracking (Umami). Safe no-op if the script is blocked.
const track = (name, data) => {
  try {
    window.umami?.track(name, data);
  } catch {
    /* analytics must never break the page */
  }
};
document.addEventListener("click", (event) => {
  const link = event.target.closest?.("a[href]");
  if (!link) return;
  const href = link.getAttribute("href");
  if (href.startsWith("https://buy.polar.sh")) track("checkout-click");
  else if (href.includes("seo-agent-lite")) track("lite-github-click");
  else if (href === "/pricing/" && /get pro/i.test(link.textContent))
    track("get-pro-click", { page: location.pathname });
});

// Close the Commands dropdown on outside click or Escape.
const menus = document.querySelectorAll("details.nav-menu");
document.addEventListener("click", (event) => {
  menus.forEach((menu) => {
    if (!menu.contains(event.target)) menu.removeAttribute("open");
  });
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape")
    menus.forEach((menu) => menu.removeAttribute("open"));
});

// "Copy" button on every code block, so commands can be copied in one tap.
document.querySelectorAll("pre > code").forEach((code) => {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "copy-btn";
  button.textContent = "Copy";
  button.setAttribute("aria-label", "Copy code to clipboard");

  button.addEventListener("click", async () => {
    const text = code.innerText.trim();
    try {
      await navigator.clipboard.writeText(text);
    } catch {
      const area = document.createElement("textarea");
      area.value = text;
      area.style.position = "fixed";
      area.style.opacity = "0";
      document.body.appendChild(area);
      area.select();
      document.execCommand("copy");
      area.remove();
    }
    track("copy-command");
    button.textContent = "Copied";
    setTimeout(() => (button.textContent = "Copy"), 1600);
  });

  code.parentElement.appendChild(button);
});

// Soft glow that follows the cursor across the whole page.
const glow = document.getElementById("cursor-glow");
if (glow) {
  let pending = false;
  let x = window.innerWidth / 2;
  let y = window.innerHeight / 3;

  const paint = () => {
    glow.style.background = `radial-gradient(260px circle at ${x}px ${y}px, rgba(129,140,248,0.55), rgba(99,102,241,0.22) 45%, transparent 70%)`;
    pending = false;
  };

  window.addEventListener("pointermove", (event) => {
    x = event.clientX;
    y = event.clientY;
    if (!pending) {
      pending = true;
      requestAnimationFrame(paint);
    }
  });

  paint();
}

// Nokia-style Snake, playing itself in the hero background.
const canvas = document.getElementById("snake-canvas");
if (canvas) {
  const ctx = canvas.getContext("2d");
  const CELL = 16;
  const MAX_LENGTH = 40;
  const isDark = () =>
    window.matchMedia("(prefers-color-scheme: dark)").matches;

  let cols = 0;
  let rows = 0;
  let snake = [];
  let dir = { x: 1, y: 0 };
  let food = { x: 0, y: 0 };
  let intervalId = null;

  function placeFood() {
    food = {
      x: Math.floor(Math.random() * cols),
      y: Math.floor(Math.random() * rows),
    };
  }

  function reset() {
    snake = [{ x: Math.floor(cols / 2), y: Math.floor(rows / 2) }];
    dir = { x: 1, y: 0 };
    placeFood();
  }

  function resize() {
    const rect = canvas.parentElement.getBoundingClientRect();
    canvas.width = Math.max(1, Math.floor(rect.width));
    canvas.height = Math.max(1, Math.floor(rect.height));
    cols = Math.max(1, Math.floor(canvas.width / CELL));
    rows = Math.max(1, Math.floor(canvas.height / CELL));
    reset();
  }

  function step() {
    const head = snake[0];
    const occupied = new Set(snake.slice(0, -1).map((s) => `${s.x},${s.y}`));

    const candidates = [];
    const dx = food.x - head.x;
    const dy = food.y - head.y;
    if (dx !== 0) candidates.push({ x: Math.sign(dx), y: 0 });
    if (dy !== 0) candidates.push({ x: 0, y: Math.sign(dy) });
    candidates.push(
      dir,
      { x: 1, y: 0 },
      { x: -1, y: 0 },
      { x: 0, y: 1 },
      { x: 0, y: -1 },
    );

    const next = candidates.find((option) => {
      const nx = (head.x + option.x + cols) % cols;
      const ny = (head.y + option.y + rows) % rows;
      return !occupied.has(`${nx},${ny}`);
    });
    dir = next || dir;

    const newHead = {
      x: (head.x + dir.x + cols) % cols,
      y: (head.y + dir.y + rows) % rows,
    };

    snake.unshift(newHead);
    if (newHead.x === food.x && newHead.y === food.y) {
      placeFood();
      if (snake.length >= MAX_LENGTH) reset();
    } else {
      snake.pop();
    }
  }

  function draw() {
    const dark = isDark();
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    ctx.strokeStyle = dark
      ? "rgba(148,163,184,0.07)"
      : "rgba(100,116,139,0.08)";
    ctx.lineWidth = 1;
    for (let x = 0; x <= cols; x++) {
      ctx.beginPath();
      ctx.moveTo(x * CELL + 0.5, 0);
      ctx.lineTo(x * CELL + 0.5, rows * CELL);
      ctx.stroke();
    }
    for (let y = 0; y <= rows; y++) {
      ctx.beginPath();
      ctx.moveTo(0, y * CELL + 0.5);
      ctx.lineTo(cols * CELL, y * CELL + 0.5);
      ctx.stroke();
    }

    ctx.fillStyle = dark ? "rgba(52,211,153,0.6)" : "rgba(5,150,105,0.5)";
    ctx.fillRect(food.x * CELL + 3, food.y * CELL + 3, CELL - 6, CELL - 6);

    snake.forEach((segment, index) => {
      const alpha = 0.55 - (index / snake.length) * 0.35;
      ctx.fillStyle = dark
        ? `rgba(52,211,153,${alpha})`
        : `rgba(15,23,42,${alpha})`;
      ctx.fillRect(
        segment.x * CELL + 1,
        segment.y * CELL + 1,
        CELL - 2,
        CELL - 2,
      );
    });
  }

  function tick() {
    step();
    draw();
  }

  function start() {
    if (intervalId) return;
    intervalId = setInterval(tick, 140);
  }

  function stop() {
    clearInterval(intervalId);
    intervalId = null;
  }

  resize();
  start();
  window.addEventListener("resize", resize);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) stop();
    else start();
  });
}

// ---- Motion and polish ------------------------------------------------
const reduceMotion = window.matchMedia(
  "(prefers-reduced-motion: reduce)",
).matches;
if (reduceMotion) document.documentElement.classList.add("no-motion");

// Reveal sections and animate the report card as they scroll into view.
const revealTargets = document.querySelectorAll(".reveal, .report-card");
if ("IntersectionObserver" in window && !reduceMotion) {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        io.unobserve(entry.target);
        if (entry.target.classList.contains("report-card"))
          countUp(entry.target);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.12 },
  );
  revealTargets.forEach((el) => io.observe(el));
} else {
  revealTargets.forEach((el) => el.classList.add("in"));
}

function countUp(card) {
  const el = card.querySelector(".score-count");
  if (!el) return;
  const target = Number(el.dataset.target || 0);
  const start = performance.now();
  const duration = 1400;
  const frame = (now) => {
    const t = Math.min(1, (now - start) / duration);
    const eased = 1 - Math.pow(1 - t, 3);
    el.textContent = String(Math.round(target * eased));
    if (t < 1) requestAnimationFrame(frame);
  };
  el.textContent = "0";
  requestAnimationFrame(frame);
}

// Terminal demo: an illustrative /seo audit run, played when it comes into view.
const terminal = document.getElementById("terminal-demo");
if (terminal) {
  const SPIN = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"];
  const agents = [
    ["seo-technical", "9 findings"],
    ["seo-content", "6 findings"],
    ["seo-performance", "4 findings"],
    ["seo-visual", "3 findings"],
    ["seo-geo", "5 findings"],
    ["seo-local", "4 findings"],
  ];
  const command = "/seo audit https://demo-bakery.co.uk --mode full";
  let timers = [];
  let running = false;

  const wait = (ms) =>
    new Promise((resolve) => timers.push(setTimeout(resolve, ms)));
  const line = (html = "") => {
    const div = document.createElement("div");
    div.className = "t-line";
    div.innerHTML = html;
    terminal.appendChild(div);
    return div;
  };
  const pad = (text, n) => text + " ".repeat(Math.max(1, n - text.length));

  function finalState() {
    terminal.innerHTML = "";
    line(`<span class="t-accent">&gt;</span> ${command}`);
    line(
      '<span class="t-dim">  Rendering homepage</span> <span class="t-ok">done</span>',
    );
    line('<span class="t-dim">  Business type:</span> local service');
    line('<span class="t-dim">  Crawled</span> 48 pages');
    agents.forEach(([name, result]) =>
      line(
        `  <span class="t-ok">✓</span> ${pad(name, 17)}<span class="t-dim">${result}</span>`,
      ),
    );
    line("");
    line('  Health score <span class="t-score">72/100</span>');
    line(
      '  <span class="t-ok">✓</span> FULL-AUDIT-REPORT.md  <span class="t-ok">✓</span> ACTION-PLAN.md  <span class="t-ok">✓</span> PDF report',
    );
  }

  async function play() {
    if (running) return;
    running = true;
    terminal.innerHTML = "";
    const prompt = line(
      '<span class="t-accent">&gt;</span> <span class="t-typed"></span><span class="t-caret"></span>',
    );
    const typed = prompt.querySelector(".t-typed");
    for (const ch of command) {
      typed.textContent += ch;
      await wait(28 + Math.random() * 40);
    }
    await wait(350);
    prompt.querySelector(".t-caret").remove();
    const render = line('<span class="t-dim">  Rendering homepage</span>');
    await wait(500);
    render.innerHTML += ' <span class="t-ok">done</span>';
    await wait(250);
    line('<span class="t-dim">  Business type:</span> local service');
    const crawl = line(
      '<span class="t-dim">  Crawling</span> <span class="t-n">0</span> pages',
    );
    const n = crawl.querySelector(".t-n");
    for (let i = 1; i <= 48; i += 1) {
      n.textContent = String(i);
      await wait(22);
    }
    crawl.innerHTML = '<span class="t-dim">  Crawled</span> 48 pages';
    await wait(250);
    const rows = agents.map(([name]) =>
      line(
        `  <span class="t-accent t-spin">${SPIN[0]}</span> ${pad(name, 17)}<span class="t-dim">running</span>`,
      ),
    );
    let frame = 0;
    const spinner = setInterval(() => {
      frame = (frame + 1) % SPIN.length;
      terminal
        .querySelectorAll(".t-spin")
        .forEach((el) => (el.textContent = SPIN[frame]));
    }, 80);
    timers.push(spinner);
    const order = [2, 0, 3, 5, 1, 4];
    for (const idx of order) {
      await wait(380 + Math.random() * 420);
      const [name, result] = agents[idx];
      rows[idx].innerHTML =
        `  <span class="t-ok">✓</span> ${pad(name, 17)}<span class="t-dim">${result}</span>`;
    }
    clearInterval(spinner);
    await wait(300);
    line("");
    const score = line('  Health score <span class="t-score">0/100</span>');
    const s = score.querySelector(".t-score");
    for (let v = 0; v <= 72; v += 2) {
      s.textContent = `${v}/100`;
      await wait(16);
    }
    s.textContent = "72/100";
    await wait(300);
    line(
      '  <span class="t-ok">✓</span> FULL-AUDIT-REPORT.md  <span class="t-ok">✓</span> ACTION-PLAN.md  <span class="t-ok">✓</span> PDF report',
    );
    running = false;
  }

  function reset() {
    timers.forEach((t) => {
      clearTimeout(t);
      clearInterval(t);
    });
    timers = [];
    running = false;
  }

  if (reduceMotion || !("IntersectionObserver" in window)) {
    finalState();
  } else {
    finalState();
    const tio = new IntersectionObserver(
      (entries) => {
        if (entries.some((e) => e.isIntersecting)) {
          tio.disconnect();
          play();
        }
      },
      { threshold: 0.35 },
    );
    tio.observe(terminal);
  }

  document.querySelector(".terminal-replay")?.addEventListener("click", () => {
    reset();
    if (reduceMotion) finalState();
    else play();
  });
}

// PDF preview: scales an A4 page to fit, cycles pages while in view, and
// replays each page's charts when it becomes active.
const pdfFrame = document.querySelector(".pdf-frame");
if (pdfFrame) {
  const scaler = pdfFrame.querySelector(".pdf-scaler");
  const pages = [...pdfFrame.querySelectorAll(".pdf-page")];
  const tabs = [...document.querySelectorAll(".pdf-tab")];
  const DWELL = 5500;
  let current = 0;
  let timer = null;
  let inView = false;
  let paused = false;

  const fit = () =>
    scaler.style.setProperty("--s", String(pdfFrame.clientWidth / 600));
  fit();
  if ("ResizeObserver" in window) new ResizeObserver(fit).observe(pdfFrame);
  else window.addEventListener("resize", fit);

  const countIn = (page) => {
    page.querySelectorAll(".pdf-count").forEach((el) => {
      const target = Number(el.dataset.target || 0);
      if (reduceMotion) {
        el.textContent = String(target);
        return;
      }
      const start = performance.now();
      const step = (now) => {
        const t = Math.min(1, (now - start) / 1300);
        el.textContent = String(Math.round(target * (1 - Math.pow(1 - t, 3))));
        if (t < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  };

  const schedule = () => {
    clearTimeout(timer);
    tabs.forEach((t) => t.classList.remove("is-timing"));
    if (!inView || paused || reduceMotion) return;
    const tab = tabs[current];
    void tab.offsetWidth;
    tab.classList.add("is-timing");
    timer = setTimeout(() => show((current + 1) % pages.length), DWELL);
  };

  function show(i) {
    const prev = pages[current];
    if (i !== current) {
      prev.classList.remove("is-active", "play");
      prev.classList.add("is-leaving");
      setTimeout(() => prev.classList.remove("is-leaving"), 700);
    }
    current = i;
    const page = pages[i];
    page.classList.remove("play");
    page.classList.add("is-active");
    requestAnimationFrame(() =>
      requestAnimationFrame(() => page.classList.add("play")),
    );
    countIn(page);
    tabs.forEach((t, n) => t.classList.toggle("is-active", n === i));
    schedule();
  }

  tabs.forEach((tab) =>
    tab.addEventListener("click", () => {
      paused = false;
      show(Number(tab.dataset.go));
    }),
  );
  const stage = document.querySelector(".pdf-stage");
  stage?.addEventListener("mouseenter", () => {
    paused = true;
    schedule();
  });
  stage?.addEventListener("mouseleave", () => {
    paused = false;
    schedule();
  });
  stage?.addEventListener("click", () => show((current + 1) % pages.length));

  pages[0].classList.add("is-active");
  if ("IntersectionObserver" in window) {
    new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const was = inView;
          inView = entry.isIntersecting;
          if (inView && !was) show(current);
          if (!inView) schedule();
        });
      },
      { threshold: 0.3 },
    ).observe(pdfFrame);
  } else {
    show(0);
  }
}

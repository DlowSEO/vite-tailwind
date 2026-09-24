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

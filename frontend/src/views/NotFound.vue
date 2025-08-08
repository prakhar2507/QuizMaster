<template>
  <div class="not-found-container">
    <h1 class="glitch" data-text="404">404</h1>
    <p class="tagline">Oops! Looks like you've entered the void...</p>
    <p class="subtext">Even Google couldn't find this one. 🕵️‍♂️</p>
    <button @click="$router.push('/')" class="home-btn">
      Take Me Home
    </button>
  </div>
</template>

<script>
export default {
  name: "NotFoundPage",
};
</script>

<style scoped>
.not-found-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #000;
  color: #fff;
  text-align: center;
  overflow: hidden;
  font-family: 'Courier New', Courier, monospace;
}

.glitch {
  font-size: 8rem;
  font-weight: bold;
  position: relative;
  color: white;
  animation: glitch 1s infinite;
}

.glitch::before,
.glitch::after {
  content: attr(data-text);
  position: absolute;
  left: 0;
}

.glitch::before {
  animation: glitchTop 1s infinite;
  color: #ff00c1;
  clip-path: polygon(0 0, 100% 0, 100% 45%, 0 45%);
}

.glitch::after {
  animation: glitchBottom 1s infinite;
  color: #00fff9;
  clip-path: polygon(0 60%, 100% 60%, 100% 100%, 0 100%);
}

@keyframes glitch {
  0% { text-shadow: 2px 2px #ff00c1, -2px -2px #00fff9; }
  20% { text-shadow: -2px -2px #ff00c1, 2px 2px #00fff9; }
  40% { text-shadow: 2px -2px #ff00c1, -2px 2px #00fff9; }
  60% { text-shadow: -2px 2px #ff00c1, 2px -2px #00fff9; }
  80% { text-shadow: 2px 2px #ff00c1, -2px -2px #00fff9; }
  100% { text-shadow: none; }
}

@keyframes glitchTop {
  0% { transform: translate(0, 0); }
  20% { transform: translate(-2px, -2px); }
  40% { transform: translate(-5px, -1px); }
  60% { transform: translate(2px, -3px); }
  80% { transform: translate(-1px, 2px); }
  100% { transform: translate(0, 0); }
}

@keyframes glitchBottom {
  0% { transform: translate(0, 0); }
  20% { transform: translate(2px, 2px); }
  40% { transform: translate(5px, 1px); }
  60% { transform: translate(-2px, 3px); }
  80% { transform: translate(1px, -2px); }
  100% { transform: translate(0, 0); }
}

.tagline {
  font-size: 1.5rem;
  margin-top: 1rem;
}

.subtext {
  font-size: 1rem;
  color: #aaa;
  margin-top: 0.5rem;
  margin-bottom: 2rem;
}

.home-btn {
  background: none;
  border: 2px solid white;
  color: white;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.home-btn:hover {
  background: white;
  color: black;
}
</style>
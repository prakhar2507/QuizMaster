<template>
  <section class="landing">
    <!-- Header -->
    <header class="header">
      <h1 class="logo">Quiz<span>Master</span></h1>
      <nav>
        <router-link to="/login">Login</router-link>
        <router-link to="/register" class="btn">Get Started</router-link>
      </nav>
    </header>

    <!-- Hero Section -->
    <main class="hero">
      <div class="hero-text">
        <h2>Challenge Your Mind,<br> Master the Quiz.</h2>
        <p>Test your knowledge across multiple subjects with a sleek and interactive experience.</p>
        <router-link to="/register" class="btn btn-primary">Join Now</router-link>
      </div>
    </main>

    <!-- Testimonials -->
    <section class="testimonials">
      <h3>What Our Players Say</h3>
      <div class="testimonial-cards">
        <div class="card">
          <p>"Absolutely love the UI. Makes learning fun!"</p>
          <span>- Priya S.</span>
        </div>
        <div class="card">
          <p>"Best quiz app I’ve ever used. So sleek and modern."</p>
          <span>- Rahul M.</span>
        </div>
        <div class="card">
          <p>"Keeps me hooked for hours, learning without even realizing."</p>
          <span>- Ananya K.</span>
        </div>
      </div>
    </section>

    <!-- Pricing -->
    <section class="pricing">
      <h3>Choose Your Plan</h3>
      <div class="pricing-cards">
        <div class="plan">
          <h4>Free</h4>
          <p>Basic quizzes & practice mode.</p>
          <span class="price">₹0</span>
        </div>
        <div class="plan">
          <h4>Pro</h4>
          <p>Unlimited quizzes, leaderboards & analytics.</p>
          <span class="price">₹199/month</span>
        </div>
      </div>
    </section>

    <!-- About Us -->
    <section class="about">
      <h3>About Us</h3>
      <p>
        QuizMaster is built for curious minds who love learning in a fun and competitive way.
        Our mission is to make knowledge accessible, engaging, and exciting for everyone.
      </p>
    </section>
  </section>
</template>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0f0f, #1a1a1a 50%, #0f0f0f);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 5%;
  border-bottom: 1px solid var(--color-border);
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
}
.logo span {
  color: var(--color-text-muted);
}

nav a {
  margin-left: 1.5rem;
  font-weight: 500;
}

.btn {
  padding: 0.6rem 1.2rem;
  border: 1px solid var(--color-accent);
  border-radius: 8px;
  transition: all 0.3s ease;
}
.btn:hover {
  background: var(--color-accent);
  color: var(--color-bg);
}

.btn-primary {
  background: var(--color-accent);
  color: var(--color-bg);
}

.hero {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 4rem 5%;
}

.hero-text h2 {
  font-size: 2.8rem;
  font-weight: 700;
}
.hero-text p {
  color: var(--color-text-muted);
  margin: 1rem 0 2rem;
}

/* Testimonials */
.testimonials {
  padding: 3rem 5%;
  text-align: center;
}
.testimonial-cards {
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  margin-top: 2rem;
}
.testimonial-cards .card {
  background: var(--color-bg-light);
  padding: 1.5rem;
  border-radius: 10px;
  width: 280px;
  border: 1px solid var(--color-border);
}
.testimonial-cards span {
  display: block;
  margin-top: 1rem;
  color: var(--color-text-muted);
}

/* Pricing */
.pricing {
  padding: 3rem 5%;
  text-align: center;
}
.pricing-cards {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-top: 2rem;
}
.plan {
  background: var(--color-bg-light);
  padding: 1.5rem;
  border-radius: 10px;
  width: 220px;
  border: 1px solid var(--color-border);
}
.price {
  display: block;
  margin-top: 1rem;
  font-size: 1.4rem;
  font-weight: bold;
}

/* About */
.about {
  padding: 3rem 5%;
  text-align: center;
  border-top: 1px solid var(--color-border);
}
.about p {
  color: var(--color-text-muted);
  max-width: 600px;
  margin: 1rem auto 0;
}
</style>
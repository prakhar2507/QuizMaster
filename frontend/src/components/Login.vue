<template>
  <section class="auth-page">
    <header class="top-header">
      <router-link to="/" class="site-name">Quiz<span>Master</span></router-link>
    </header>

    <div class="auth-card">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <label>Email</label>
        <input type="email" placeholder="Enter your email" v-model="email" required />

        <label>Password</label>
        <input type="password" placeholder="Enter your password" v-model="password" required />

        <button type="submit" class="btn-primary">Sign In</button>
      </form>
      <p class="switch-link">
        Don't have an account?
        <router-link to="/register">Register</router-link>
      </p>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      loading: false,
      error: "",
      success: "",
    };
  },
  methods: {
    async login() {
      this.loading = true;
      this.error = "";
      this.success = "";
      try {
        const res = await fetch("http://localhost:5000/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: this.email, password: this.password }),
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.message || "Login failed");
        this.success = "Login successful!";
        localStorage.setItem("access_token", data.access_token);
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped src="../assets/auth.css"></style>
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

        if (!res.ok) {
          await this.$swal.fire({
            icon: "error",
            title: "Login Failed",
            text: data.message || "Please try again.",
          });
          return;
        }

        await this.$swal.fire({
          icon: "success",
          title: "Login Successful",
          text: "Redirecting to dashboard...",
          timer: 2000,
          timerProgressBar: true,
          showConfirmButton: false,
        });

        localStorage.setItem("access_token", data.access_token);
        this.$router.push("/dashboard");

      } catch (err) {
        await this.$swal.fire({
          icon: "error",
          title: "Error",
          text: err.message,
        });
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped src="../assets/auth.css"></style>
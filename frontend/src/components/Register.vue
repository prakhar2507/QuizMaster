<template>
  <div class="auth-form">
    <h2>Register</h2>
    <form @submit.prevent="register">
      <input v-model="form.full_name" placeholder="Full Name" required />
      <input v-model="form.email" type="email" placeholder="Email" required />
      <input v-model="form.dob" type="date" placeholder="Date of Birth" required />
      <input v-model="form.qualification" placeholder="Qualification" required />
      <input v-model="form.mobile_no" placeholder="Mobile Number" />
      <input v-model="form.password" type="password" placeholder="Password" required />
      <button type="submit" :disabled="loading">Register</button>
      <p v-if="error" class="error">{{ error }}</p>
      <p v-if="success" class="success">{{ success }}</p>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        full_name: "",
        email: "",
        dob: "",
        qualification: "",
        mobile_no: "",
        password: "",
      },
      loading: false,
      error: "",
      success: "",
    };
  },
  methods: {
    async register() {
      this.loading = true;
      this.error = "";
      this.success = "";
      try {
        const res = await fetch("http://localhost:5000/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form),
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.message || "Registration failed");
        this.success = "Registration successful! You can now log in.";
        this.form = { full_name: "", email: "", dob: "", qualification: "", mobile_no: "", password: "" };
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.auth-form { max-width: 400px; margin: 2rem auto; padding: 2rem; border: 1px solid #eee; border-radius: 8px; }
input { display: block; width: 100%; margin-bottom: 1rem; padding: 0.5rem; }
button { width: 100%; padding: 0.5rem; }
.error { color: red; }
.success { color: green; }
</style> 
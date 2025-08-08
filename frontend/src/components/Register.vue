<template>
  <section class="auth-page">
    <header class="top-header">
      <router-link to="/" class="site-name">Quiz<span>Master</span></router-link>
    </header>

    <div class="auth-card">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <label>Full Name</label>
        <input type="text" placeholder="Enter your full name" v-model="form.full_name" required />

        <label>Email</label>
        <input type="email" placeholder="Enter your email" v-model="form.email" required />

        <label>Password</label>
        <input type="password" placeholder="Enter your password" v-model="form.password" required />

        <label>Qualification</label>
        <input type="text" placeholder="Enter your qualification" v-model="form.qualification" required />

        <label>Date of Birth</label>
        <input type="date" v-model="form.dob" required />

        <label>Mobile No</label>
        <input type="tel" placeholder="Enter your mobile number" v-model="form.mobile_no" required />

        <button type="submit" class="btn-primary">Create Account</button>
      </form>
      <p class="switch-link">
        Already have an account?
        <router-link to="/login">Login</router-link>
      </p>
    </div>
  </section>
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
    };
  },
  methods: {
    async register() {
      this.loading = true;
      try {
        const res = await fetch("http://localhost:5000/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(this.form),
        });

        const data = await res.json();

        if (!res.ok) {
          await Swal.fire({
            icon: "error",
            title: "Registration Failed",
            text: data.message || "Please try again.",
            confirmButtonColor: "#4CAF50",
          });
          return;
        }

        await Swal.fire({
          icon: "success",
          title: "Registration Successful",
          text: "You can now log in to your account.",
          confirmButtonColor: "#4CAF50",
          timer: 2000,
          timerProgressBar: true,
        });

        this.$router.push("/login");

      } catch (err) {
        await Swal.fire({
          icon: "error",
          title: "Error",
          text: err.message,
          confirmButtonColor: "#4CAF50",
        });
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped src="../assets/auth.css"></style>
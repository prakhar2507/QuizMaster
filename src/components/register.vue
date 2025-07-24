<template>
  <div class="container">
    <div class="form-container">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    register() {
      // Handle registration logic here
      console.log('Registering with:', this.username, this.email, this.password);
    }
  }
};
</script>
<template>
  <div id="app">
    <div class="toggle-buttons">
      <button @click="showLogin = true">Login</button>
      <button @click="showLogin = false">Register</button>
    </div>
    <Login v-if="showLogin" />
    <Register v-else />
  </div>
</template>

<script>
import Login from './components/Login.vue';
import Register from './components/Register.vue';

export default {
  name: 'App',
  components: {
    Login,
    Register
  },
  data() {
    return {
      showLogin: true
    };
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.toggle-buttons {
  margin-bottom: 20px;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.form-container {
  width: 300px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #369f77;
}
</style>
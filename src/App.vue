<template>
<div style="background-color:#2c3e50; width: 100vw;height: 100vh; ">
<nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="border:1px">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Skin Ratings</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link class="nav-link" to="/">Home</router-link>
        </li>
        <li class="nav-item">
            <router-link to="/LeaderBoard" class="nav-link">Leaderboard</router-link>
        </li>
        <li class="nav-item">
          <router-link to="/About" class="nav-link">About</router-link>
        </li>
        <li class="nav-iten">
          <audio ref="audio" :src="require('@/assets/audio/music.mp3')" loop></audio>
          <input style="margin-left:5px" type="checkbox" class="btn-check" id="btn-check-outlined" autocomplete="off">
          <label style="margin-left:5px"  @click="toggleAudio" class="btn btn-outline-secondary" for="btn-check-outlined">Music?</label><br>

        </li>
      </ul>
    </div>
  </div>

</nav>

  <router-view style="background-color: #2c3e50;"/>

</div>


</template>

<script>
export default {
  methods: {
    toggleAudio() {
      const audio = this.$refs.audio;
      if (audio.paused) {
        audio.play();
      } else {
        audio.pause();
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #7e7e7e;
}
</style>

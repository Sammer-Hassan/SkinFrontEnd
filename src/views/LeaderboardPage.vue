<template>
  <div>
    <h1 style="color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">Leaderboard</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div class="leaderboard-item" v-for="(skin, index) in leaderboard" :key="skin.id">
        <div class="rank">{{ index + 1 }}</div>
        <div class="details">
          <div class="name">{{ skin.name }}</div>
          <img :src="getSkinImageUrl(skin.id)" alt="Skin Image" class="image" style="cursor: pointer;" />
        </div>
        <div class="elo">ELO: {{ skin.elo }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      leaderboard: [],
      loading: true,
    };
  },
  mounted() {
    this.fetchLeaderboard();
  },
  methods: {
    async fetchLeaderboard() {
      try {
        console.log("here")
        const response = await axios.get('http://localhost:8081/api/v1/skin/Leaderboard');
        this.leaderboard = response.data.reverse();
        console.log(this.leaderboard)
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
      } finally {
        this.loading = false;
      }
    },
    getSkinImageUrl(skinId) {
      return require(`@/assets/AllValorantKnives/${skinId}.webp`);
    },
  },
};
</script>

<style>
/* Add your styling here if needed */
.leaderboard-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid #212529;
  padding: 10px;
  margin-bottom: 10px;
}

.rank, .elo {
  font-weight: bold;
  color: rgb(240, 240, 240); 
  margin:50px;
}



.name {
  margin-bottom: 10px;
  font-weight: bold;
  color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5)
  
}

.image {
  max-width: 400px; /* Adjust the width as needed */
  max-height: 400px; /* Adjust the height as needed */
}
</style>

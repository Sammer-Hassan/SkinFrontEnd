<template>
  <div>
    <h3 style="margin-top: 50px; color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">Which do you rank higher?</h3>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div class="skin-container">
        <div v-for="(skin, index) in skins" :key="skin.id" class="skin-item">
          <h1 style="color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">{{ skin.name }}</h1>
          <figure class="figure">
            <img
              :src="getSkinImageUrl(skin.id)"
              alt="Skin Image"
              @click="handleSkinClick(index)"
              style="cursor: pointer; width: 90%; height: 90%; object-fit: cover; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);"
            />
          </figure>
        </div>
      </div>
    </div>

    <div v-if="debounceLoading" class="spinner-border text-light" role="status">
    <span class="visually-hidden">Loading...</span>
    </div>
    <!-- Loading spinner -->
    <div v-if="debounceLoading">
      <h style="color:white"> {{prompts[Math.floor(Math.random() * prompts.length)] }} </h>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: true,
      skins: [],
      debounceLoading: false,
      prompts: [
        "Good choice",
        "You are actually trolling",
        "Get your eyes checked out",
        "This kid is actually throwing....",
        "I will kick you off my website",
        "VALID",
        "Fantastic selection!",
        "Is that your final answer?",
        "Great taste!",
        "You've got an eye for style",
        "Bold decision.",
        "Excellent decision",
        "You really know your skins!",
        "Impressive!",
        "Solid pick!",
        "What a legendary choice!",
        "You're on fire with these selections",
        "Keep it up!",
        "You're making these skins proud!",
        "Really? Interesting choice...",
        "Are you sure about that one?",
        "Well, that's an... unconventional pick",
        "Not what I expected, but okay",
        "Interesting strategy, let's see how it pays off",
        "Are you just picking random skins?",
        "Hmm, not everyone's cup of tea",
        "That's a bold pick...",
        "You might want to rethink that choice",
        "Well, it's your opinion, I guess",
        "Interesting, let's see how the community reacts to that one",
      ]
    };
  },
  mounted() {
    this.fetchRandomSkins();
  },
  methods: {
    fetchRandomSkins() {
      this.loading = true;

      axios.get(`${process.env.VUE_APP_API_URL}api/v1/skin`)
        .then(response => {
          this.skins.push(response.data);

          return axios.get(`${process.env.VUE_APP_API_URL}api/v1/skin`);
        })
        .then(response2 => {
          this.skins.push(response2.data);
          console.log(this.skins);
        })
        .catch(error => {
          console.error(error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getSkinImageUrl(skinId) {
      return require(`@/assets/AllValorantKnives/${skinId}.webp`);
    },
    handleSkinClick: debounce(function(index) {

      const selectedSkinId = this.skins[index].id;
      const otherSkinId = this.skins.find((_, i) => i !== index).id;

      const longValues = [selectedSkinId, otherSkinId];

      axios.post(`${process.env.VUE_APP_API_URL}api/v1/skin/UpdateElo`, longValues, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          this.skins = [];
          this.fetchRandomSkins();
        })
        .catch(error => {
          console.error(error);
        })
        .finally(() => {
          this.debounceLoading = false;
        });
    }, 1000),
  },
};

function debounce(func, wait) {
  let timeout;
  return function (...args) {
    this.debounceLoading = true;

    const context = this;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), wait);
  };
}
</script>

<style scoped>
.skin-container {
  display: flex;
  justify-content: space-between;
}

.skin-item {
  margin: 5px;
  margin-top: 20px;
}

img:hover {
  transition: transform 0.3s ease;
  transform: scale(1.05);
}
</style>

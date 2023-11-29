<template>
  <div>
    <h3 style="margin-top: 50px; color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">Which do you rank higher?</h3>
    <h5 style="margin-top: 50px; color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">Global Votes: {{this.counter.count}}</h5>

    <div v-if="loading">Loading...</div>
    <div v-else>
      <div class="skin-container">
        <div v-for="(skin, index) in skins" :key="skin.id" class="skin-item">
          <h1 style="color: rgb(240, 240, 240); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">{{ skin.name }}</h1>
          <figure class="figure">
            <img
              :src="getSkinImageUrl(skin.id)"
              alt="{{skin.name}} Image"
              @click="handleSkinClick(index)"
              class="image"
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
      counter: 0,
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
    this.fetchCounter();
  },
  methods: {
    async fetchCounter() {
  try {
    const response = await axios.get(`${process.env.VUE_APP_API_URL}api/v1/skin/Counter`);
    this.counter = response.data;
    console.log(this.counter);
  } catch (error) {
    console.error(error);
  }
},
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
          this.fetchCounter();
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
  flex-wrap: wrap; /* Allow items to wrap to the next line */
}

.skin-item {
  margin: 5px;
  margin-top: 20px;
  flex: 0 0 calc(50% - 10px); /* Each item takes 50% width on larger screens */
}
img:hover {
  transition: transform 0.5s ease, box-shadow 0.5s ease;
  transform: scale(1.05);
}
.image{
  cursor: pointer;
   width: 800px; 
   height: 450px; 
   box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }



@media (max-width: 1300px) {
  .skin-item {
    flex: 0 0 100%; /* Each item takes 100% width on small screens, stacking them */

  }
  .image{
    height:90%;
    width:90%;
  }
}
</style>

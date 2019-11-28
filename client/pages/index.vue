<template>
  <div>
    <section class="section has-text-centered">
      <div>
        <input
          v-model="start"
          class="input is-large"
          type="text"
          placeholder="何から始めますか？"
          autofocus
          @keydown.enter="triggerGetWords"
        >
      </div>

      <div>
        <button
          class="button is-info is-large"
          :class="{ 'is-loading': thinking }"
          @click="getWords"
        >
          スタート
        </button>
      </div>

      <div>
        <transition-group
          name="custom-classes-transition"
          enter-active-class="animated fadeInLeft"
          tag="ul"
          class="output-list has-text-left"
        >
          <li v-for="word in words" :key="word">
            <span class="is-size-3">{{ word }}</span>
          </li>
        </transition-group>

        <transition enter-active-class="animated fadeIn">
          <p v-if="hasError" class="is-size-5">
            うーん、そんな単語は聞いたことがないですね。
          </p>
        </transition>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'HomePage',

  data () {
    return {
      start: '',
      words: [],
      thinking: false,
      hasError: false
    }
  },

  methods: {
    triggerGetWords (event) {
      if (event.keyCode === 13) {
        this.getWords()
      }
    },
    getWords () {
      if (this.thinking) {
        return
      }

      this.words = []
      this.hasError = false

      if (!this.start) {
        return
      }

      this.thinking = true
      this.$axios.get('word-from/' + this.start)
        .then((response) => {
          for (let i = 0; i < response.data.words.length; i++) {
            const prefix = (i === 0 ? '' : '→ ')
            const word = prefix + response.data.words[i]
            setTimeout(() => this.words.push(word), 500 * i)
          }
        })
        .catch(() => {
          this.hasError = true
        })
        .finally(() => {
          this.thinking = false
        })
    }
  }
}
</script>

<style scoped>
  .input {
    width: 500px;
    margin-bottom: 20px;
  }
  .output-list {
    display: inline-block;
    width: 500px;
  }
</style>

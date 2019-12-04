<template>
  <div>
    <nav
      class="navbar header has-shadow is-primary"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand is-size-3">
        <p class="navbar-item">
          単語を{{ caption }}してみるよ
        </p>
      </div>

      <div class="navbar-end">
        <div class="navbar-item">
          <b-switch
            v-model="shiritori"
            class="is-medium"
            type="is-light"
            @input="toggle"
          >
            しりとりモード
          </b-switch>
        </div>
      </div>
    </nav>

    <section class="main-content">
      <div class="container">
        <nuxt />
      </div>
    </section>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  data () {
    return {
      shiritori: false
    }
  },
  computed: {
    caption: vm => vm.shiritori ? 'しりとり' : '連想'
  },
  methods: {
    ...mapMutations({
      toggle: 'toggleShiritori'
    })
  }
}
</script>

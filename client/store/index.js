export const state = () => ({
  shiritori: false
})

export const mutations = {
  toggleShiritori (state) {
    state.shiritori = !state.shiritori
  }
}

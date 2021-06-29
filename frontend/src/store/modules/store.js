import axios from "axios";
import { postWithToken } from "@/api/http";
const store = {
  namespaced: true,
  state: {
    dataStore: [],
  },
  getters: {
    getStore(state) {
      return state.dataStore;
    },
  },
  mutations: {
    STORE(state, data) {
      state.dataStore = data;
    },
  },
  actions: {
    async fetchStore({ commit }) {
      await axios
        .get("http://localhost:8989/v1/store/")
        .then((response) => {
          if (response.status === 200)
            commit("STORE", response.data.results);
          else commit("STORE", []);
        })
        .catch(() => {
          commit("STORE", []);
        });
    },
    async save({ commit, state }, payload) {
      this.loading = true;
      await postWithToken(
        "http://localhost:8989/v1/store/",
        payload
      ).then((response) => {
        if (response.status === 200) 
          commit("STORE", state.dataStore.push(response.data));

        console.log(state.dataStore.push(response.data));
        return response.data;
      });
      this.loading = false;
      this.dialogFormVisible = false;
    },
  },
};

export default store;

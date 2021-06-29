import axios from "axios";
import { postWithToken, deleteWithToken, putWithToken } from "@/api/http";
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
      await postWithToken(
        "http://localhost:8989/v1/store/",
        payload
      ).then((response) => {
        if (response.status === 200) 
          commit("STORE", state.dataStore.push(response.data));
        return response.data;
      });
    },
    async editSave({ dispatch }, id, payload){
      await putWithToken(
        "http://localhost:8989/v1/store/"+id,
        payload
      ).then(() => {
        dispatch('fetchStore')
      });
    },
    async deleteStore({ dispatch }, id){
      await deleteWithToken(
        "http://localhost:8989/v1/store/"+id
      ).then(() => {
        dispatch('fetchStore')
      });
    }
  },
};

export default store;

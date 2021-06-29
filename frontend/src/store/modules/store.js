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
    idKeyWithNameValue(state) {
      return state.dataStore.reduce(
        (a, e) => ({
          [e.id]: e.name,
        }),
        {}
      );
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
    async save({ dispatch }, payload) {
      await postWithToken(
        "http://localhost:8989/v1/store/",
        {
          name: payload.name,
          description: payload.description,
          rating: payload.rating
        }
      ).then(async() => {
        // if (response.status === 200) 
        //   commit("STORE", state.dataStore.push(response.data));
        // return response.data;
        await dispatch('fetchStore')
      });
    },
    async editSave({ dispatch }, payload){
      await putWithToken(
        "http://localhost:8989/v1/store/"+payload.id+"/",
        {
          name: payload.name,
          description: payload.description,
          rating: payload.rating
        }
      ).then(async() => {
        await dispatch('fetchStore')
      });
    },
    async deleteStore({ dispatch }, id){
      await deleteWithToken(
        "http://localhost:8989/v1/store/"+id
      ).then(async() => {
        await dispatch('fetchStore')
      });
    }
  },
};

export default store;

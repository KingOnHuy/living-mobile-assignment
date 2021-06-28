import TokenStorage from "@/api/token.storage";
import UrlService from "@/api/urls.service";
import axios from "axios";
import router from "@/router";

let inintState = TokenStorage.isAuthenticated() ? {
  isLogin: true,
} : {
  isLogin: false,
};

const auth = {
  namespaced: true,
  state: inintState,
  getters: {
    isLogin(state) {
      return state.isLogin;
    },
  },
  mutations: {
    IS_LOGIN(state, data) {
      state.isLogin = data;
    },
  },
  actions: {
    async login({ commit }, payload) {
      const response = await axios
        .post(UrlService.loginToken(), {
          username: payload.username,
          password: payload.password,
        })
        .then((response) => {
          if (response.data.access) {
            commit("IS_LOGIN", true);
            TokenStorage.storeToken(response.data.access);
            TokenStorage.storeRefreshToken(response.data.refresh);

            router.push({ name: "Store" });
          }
        });
      return response.data;
    },
    async logout({ commit }) {
      TokenStorage.clear();
      commit("IS_LOGIN", false);
      router.push({ name: "Login" });
    },
  },
};

export default auth;

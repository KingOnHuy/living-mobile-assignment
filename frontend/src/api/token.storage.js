import axios from "axios";
import UrlService from "@/api/urls.service";
import store from "@/store/index";
// import HTTPService from "@/services/http";

/* eslint class-methods-use-this:0 */
class TokenStorage {
  constructor() {
    this.LOCAL_STORAGE_TOKEN = "access";
    this.LOCAL_STORAGE_REFRESH_TOKEN = "refresh";
    this.LOCAL_STORAGE_TOKEN_DECODE = "accessDe";
    this.LOCAL_STORAGE_REFRESH_DECODE = "refreshDe";
  }

  isAuthenticated() {
    return this.getToken() !== null;
  }

  async getAuthenticationHeaders() {
    const tokenDecode = this.getTokenDecode();
    if (tokenDecode) {
      const expTime = tokenDecode.exp;
      const expReTime = this.getRefreshDecode().exp;
      const tempTime = Date.now();
      if (tempTime >= expReTime * 1000) {
        // Toast.open({
        //   duration: 5000,
        //   message: "Session timeout",
        //   type: "is-danger",
        //   actionText: null,
        // });
        console.error("Session timeout");
        await store.dispatch("auth/logout");
      } else if (tempTime >= expTime * 1000) {
        console.log(`${tempTime} > ${expTime * 1000} exp!!!`);
        const newToken = await this.getNewToken();
        return {
          headers: { Authorization: `Bearer ${newToken.access}` },
        };
      }
    }
    return {
      headers: { Authorization: `Bearer ${this.getToken()}` },
    };
  }

  async getNewToken() {
    const response = await axios
      .post(UrlService.refreshToken(), { refresh: this.getRefreshToken() });
    if (response.data.access) {
      this.storeToken(response.data.access);
    }
    return response.data;
  }

  storeToken(token) {
    localStorage.setItem(this.LOCAL_STORAGE_TOKEN, token);
    localStorage.setItem(this.LOCAL_STORAGE_TOKEN_DECODE, this.parseJwt(token));
  }

  storeRefreshToken(refreshToken) {
    localStorage.setItem(this.LOCAL_STORAGE_REFRESH_TOKEN, refreshToken);
    localStorage.setItem(this.LOCAL_STORAGE_REFRESH_DECODE, this.parseJwt(refreshToken));
  }

  clear() {
    localStorage.removeItem(this.LOCAL_STORAGE_TOKEN);
    localStorage.removeItem(this.LOCAL_STORAGE_REFRESH_TOKEN);
    localStorage.removeItem(this.LOCAL_STORAGE_TOKEN_DECODE);
    localStorage.removeItem(this.LOCAL_STORAGE_REFRESH_DECODE);
  }

  getRefreshToken() {
    return localStorage.getItem(this.LOCAL_STORAGE_REFRESH_TOKEN);
  }

  getToken() {
    return localStorage.getItem(this.LOCAL_STORAGE_TOKEN);
  }

  getTokenDecode() {
    return JSON.parse(localStorage.getItem(this.LOCAL_STORAGE_TOKEN_DECODE));
  }

  getRefreshDecode() {
    return JSON.parse(localStorage.getItem(this.LOCAL_STORAGE_REFRESH_DECODE));
  }

  parseJwt(token) {
    try {
      return atob(token.split(".")[1]);
    } catch (e) {
      return e;
    }
  }
}

/* eslint class-methods-use-this:1 */
export default new TokenStorage();

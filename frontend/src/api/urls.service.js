class UrlService {
  constructor() {
    this.BASE_URL = process.env.VUE_APP_BASE_URL_API;
    this.API_URL = `${this.BASE_URL}v1/`;
  }

  // AUTHENTICATION
  /**
   * This endpoint use 'username' and 'password' for get JWT
   * but in this project doesn't use this endpoint
   * @returns {String}
   */
  loginToken() {
    return `${this.BASE_URL}token/`;
  }

  refreshToken() {
    return `${this.BASE_URL}token/refresh/`;
  }
}
export default new UrlService();

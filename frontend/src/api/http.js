import axios from "axios";
import TokenStorage from "./token.storage";

async function getWithToken(url) {
  return axios.get(url, await TokenStorage.getAuthenticationHeaders());
}

async function postWithToken(url, payload = {}) {
  return axios.post(
    url,
    payload,
    await TokenStorage.getAuthenticationHeaders()
  );
}

async function putWithToken(url, payload = {}) {
  return axios.put(url, payload, await TokenStorage.getAuthenticationHeaders());
}

async function patchWithToken(url, payload = {}) {
  return axios.patch(
    url,
    payload,
    await TokenStorage.getAuthenticationHeaders()
  );
}

async function deleteWithToken(url, payload = {}) {
  return axios.delete(
    url,
    payload,
    await TokenStorage.getAuthenticationHeaders()
  );
}

export default {
  getWithToken,
  postWithToken,
  putWithToken,
  patchWithToken,
  deleteWithToken,
};

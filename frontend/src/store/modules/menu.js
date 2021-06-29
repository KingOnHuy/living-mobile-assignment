import {
  getWithToken,
  postWithToken,
  putWithToken,
  deleteWithToken,
} from "../../api/http";
import UrlService from "../../api/urls.service";
import { Message } from 'element-ui';

const menu = {
  namespaced: true,
  state: {
    tableData: [],
    dialogVisible: false,
    isLoading: false,
    updateData: null,
  },
  getters: {
    tableData(state) {
      return state.tableData;
    },
    dialogVisible(state) {
      return state.dialogVisible;
    },
    isLoading(state) {
      return state.isLoading;
    },
    updateData(state) {
      return state.updateData;
    },
  },
  mutations: {
    TABLE_DATA(state, data) {
      state.tableData = data;
    },
    OPEN_DIALOG_VISIBLE(state) {
      state.dialogVisible = true;
    },
    CLOSE_DIALOG_VISIBLE(state) {
      state.dialogVisible = false;
    },
    IS_LOADING(state, data) {
      state.isLoading = data;
    },
    UPDATE_DATA(state, data) {
      console.log(data);
      state.updateData = data;
    },
  },
  actions: {
    async getMenuData({ commit }) {
      commit("IS_LOADING", true);
      return await getWithToken(`${UrlService.API_URL}menu/`)
        .then((response) => {
          commit("TABLE_DATA", response.data.results);
          return response.data.results;
        })
        .catch((error) => {
          Message.error({
            message: `Oops, Can not get menu data.`,
          });
          return error;
        })
        .finally(() => {
          commit("IS_LOADING", false);
        });
    },
    // eslint-disable-next-line no-unused-vars
    async createMenuData({ dispatch }, payload) {
      return await postWithToken(`${UrlService.API_URL}menu/`, payload)
        .then((response) => {
          Message.success({
            message: `Created ${response.data.name} menu.`,
            offset: 100,
          });
          dispatch("getMenuData");
          return response;
        })
        .catch((error) => {
          Message.error({
            message: "Can't delete menu.",
            offset: 100,
          });
          return error;
        });
    },
    // eslint-disable-next-line no-unused-vars
    async updateMenuData({ commit, dispatch }, payload) {
      console.log(payload);
      commit("IS_LOADING", true);
      return await putWithToken(
        `${UrlService.API_URL}menu/${payload.id}/`,
        payload.data
      )
        .then(() => {
          Message.success({
            message: "Updated menu.",
            offset: 100,
          });
          dispatch("getMenuData");
        })
        .catch((error) => {
          Message.error({
            message: "Can't update menu.",
            offset: 100,
          });
          console.log(error);
          commit("IS_LOADING", false);
        });
    },
    // eslint-disable-next-line no-unused-vars
    async deleteMenuData({ commit, dispatch }, payload) {
      commit("IS_LOADING", true);
      return await deleteWithToken(`${UrlService.API_URL}menu/${payload}/`)
        .then(() => {
          Message.success({
            message: "Deleted menu.",
            offset: 100,
          });
          dispatch("getMenuData");
        })
        .catch((error) => {
          Message.error({
            message: "Can't delete menu.",
            offset: 100,
          });
          console.log(error);
          commit("IS_LOADING", false);
        });
    },
  },
};

export default menu;

import { getWithToken, deleteWithToken } from "../../api/http";
import UrlService from "../../api/urls.service";
import { Message } from 'element-ui';

const category = {
  namespaced: true,
  state: {
    tableData: [],
    dialogVisible: false,
  },
  getters: {
    tableData(state) {
      return state.tableData;
    },
    dialogVisible(state) {
      return state.dialogVisible;
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
  },
  actions: {
    async getCategoryData({ commit }) {
      return await getWithToken(`${UrlService.API_URL}category/`).then(
        (response) => {
          commit("TABLE_DATA", response.data.results);
          return response.data.results;
        }
      );
    },
    // eslint-disable-next-line no-unused-vars
    async deleteCategoryData({ dispatch }, payload) {
      return await deleteWithToken(`${UrlService.API_URL}category/${payload}`)
        .then(() => {
          Message.success({
            message: "Deleted category.",
            offset: 100,
          });
          dispatch("getcategoryData");
        })
        .catch((error) => {
          Message.error({
            message: "Can't delete category.",
            offset: 100,
          });
          console.log(error);
        });
    },
  },
};

export default category;

import { getWithToken, deleteWithToken, postWithToken, putWithToken } from "../../api/http";
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
    idKeyWithNameValue(state) {
      return state.tableData.reduce(
        (a, e) => ({
          [e.id]: e.name,
        }),
        {}
      );
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
    async save({ dispatch }, payload) {
      await postWithToken(
        "http://localhost:8989/v1/category/",
        {
          name: payload.name,
          storeId: payload.storeId,
        }
      ).then(async() => {
        await dispatch('getCategoryData')
      });
    },
    async deleteCategory({ dispatch }, id){
      await deleteWithToken(
        "http://localhost:8989/v1/category/"+id
      ).then(async() => {
        await dispatch('getCategoryData')
      });
    },
    async editSave({ dispatch }, payload){
      await putWithToken(
        "http://localhost:8989/v1/category/"+payload.id+"/",
        {
          name: payload.name,
          storeId: payload.storeId,
        }
      ).then(async() => {
        await dispatch('getCategoryData')
      });
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

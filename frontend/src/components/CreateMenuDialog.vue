<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogVisible"
    :before-close="handleClose"
    width="70%"
  >
    <el-form label-position="top" label-width="100px" :model="formData">
      <div v-if="updateData">ID: {{ updateData.id }}</div>
      <el-form-item label="Category">
        <el-select
          filterable
          v-model="formData.categoryId"
          value-key="name"
          :loading="isLoadingCategory"
        >
          <el-option
            v-for="item in categoryList"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          >
          </el-option
        ></el-select>
      </el-form-item>
      <el-form-item label="Name">
        <el-input v-model="formData.name"></el-input>
      </el-form-item>
      <el-form-item label="Price">
        <el-input-number
          type="number"
          v-model="formData.price"
        ></el-input-number>
      </el-form-item>
    </el-form>
    <span slot="footer" class="dialog-footer">
      <el-button v-if="!updateData" type="primary" @click="createItem" round>
        Add {{ title }}
      </el-button>
      <el-button v-else type="primary" @click="updateItem" round>
        Update
      </el-button>
    </span>
  </el-dialog>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";

export default {
  name: "CreateMenuDialog",
  props: {
    title: String,
  },
  data() {
    return {
      formData: {},
      isLoadingCategory: false,
    };
  },
  async created() {
    await this.getCategoryDataAPI();
    console.log(this.updateData);
    if (this.updateData) {
      this.formData = this.updateData;
    }
  },
  methods: {
    ...mapMutations({
      closeDialogMenu: "menu/CLOSE_DIALOG_VISIBLE",
    }),
    ...mapActions({
      getCategoryData: "category/getCategoryData",
      createMenuData: "menu/createMenuData",
      updateMenuData: "menu/updateMenuData",
    }),
    async getCategoryDataAPI() {
      this.isLoadingCategory = true;
      await this.getCategoryData().finally(() => {
        this.isLoadingCategory = false;
      });
    },
    querySearch(queryString, cb) {
      let categoryList = this.categoryList;
      let results = queryString
        ? categoryList.filter(this.createFilter(queryString))
        : categoryList;
      // call callback function to return suggestions
      cb(results);
    },
    createFilter(queryString) {
      return (item) =>
        item.name.toLowerCase().indexOf(queryString.toLowerCase()) === 0;
    },
    handleClose() {
      this.$confirm("Are you sure to close?")
        .then(() => {
          this.closeDialog();
        })
        .catch(() => {});
    },
    createItem() {
      console.log("Create", this.formData);
      this.createMenuData(this.formData).then(() => {
        this.closeDialog();
      });
    },
    updateItem() {
      this.updateMenuData({
        id: this.formData.id,
        data: this.formData,
      }).then(() => {
        this.closeDialog();
      });
    },
    closeDialog() {
      switch (this.title) {
        case "Menu":
          this.closeDialogMenu();
          break;
        default:
          break;
      }
    },
  },
  computed: {
    ...mapGetters({
      dialogVisible: "menu/dialogVisible",
      categoryList: "category/tableData",
      updateData: "menu/updateData",
    }),
  },
};
</script>

<style>
</style>

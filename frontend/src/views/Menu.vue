<template>
  <el-container class="sk-container">
    <el-header>
      <el-row :gutter="20">
        <el-col :span="16">
          <h1 class="title">{{ name }}</h1>
        </el-col>
        <el-col :span="8" class="d-flex align-center" style="height: 100px">
          <el-button
            round
            class="ml"
            type="primary"
            icon="el-icon-plus"
            @click="createItem({})"
            :loading="dialogVisible"
          >
            Add New {{ name }}
          </el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <el-table
        v-loading="isLoading"
        :data="tableData"
        :default-sort="{ prop: 'date', order: 'descending' }"
        style="width: 100%"
        empty-text="ไม่มีเมนู"
      >
        <el-table-column prop="id" label="ID" width="150"></el-table-column>
        <el-table-column prop="name" label="Name"> </el-table-column>
        <el-table-column prop="categoryId" label="Category" width="150">
          <template slot-scope="item">
            {{ idKeyWithNameValueCategory[item.row.categoryId] }}
          </template>
        </el-table-column>
        <el-table-column prop="price" label="Price" width="60">
        </el-table-column>
        <el-table-column width="150">
          <template slot-scope="item">
            <el-button
              icon="el-icon-edit"
              @click="createItem(item.row)"
              circle
            ></el-button>
            <el-popconfirm
              confirm-button-text="OK"
              cancel-button-text="No, Thanks"
              icon="el-icon-info"
              icon-color="primary"
              :title="`Are you sure to copy &quot;${item.row.name}&quot;?`"
              @confirm="copyItem(item.row)"
            >
              <el-button
                type="primary"
                icon="el-icon-document-copy"
                circle
                style="margin-left: 0"
                slot="reference"
              ></el-button>
            </el-popconfirm>
            <el-popconfirm
              confirm-button-text="OK"
              cancel-button-text="No, Thanks"
              icon="el-icon-info"
              icon-color="red"
              :title="`Are you sure to delete &quot;${item.row.name}&quot;?`"
              @confirm="deleteItem(item.row.id)"
            >
              <el-button
                type="danger"
                icon="el-icon-delete-solid"
                circle
                slot="reference"
              ></el-button>
            </el-popconfirm>
          </template>
        </el-table-column>
      </el-table>
    </el-main>

    <create-menu-dialog v-if="dialogVisible" :title="name" :data="editItem" />
  </el-container>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
import CreateMenuDialog from "../components/CreateMenuDialog.vue";

export default {
  components: { CreateMenuDialog },
  name: "Menu",
  data() {
    return {
      name: "Menu",
      editItem: null,
      categoryData: null,
    };
  },
  methods: {
    ...mapActions({
      getMenuData: "menu/getMenuData",
      createMenuData: "menu/createMenuData",
      getCategoryData: "category/getCategoryData",
    }),
    ...mapMutations({
      openDialogVisibleMenu: "menu/OPEN_DIALOG_VISIBLE",
      updateDialogData: "menu/UPDATE_DATA",
    }),
    ...mapActions({
      deleteMenuData: "menu/deleteMenuData",
    }),
    async getMenuDataAPI() {
      await this.getMenuData();
    },
    copyItem(item) {
      this.createMenuData(item);
    },
    async deleteItem(id) {
      console.log(id);
      switch (this.name) {
        case "Menu":
          await this.deleteMenuData(id);
          break;
        default:
          break;
      }
    },
    createItem(item = null) {
      switch (this.name) {
        case "Menu":
          if (item) {
            this.updateDialogData(item);
          }
          this.openDialogVisibleMenu();
          break;
        default:
          break;
      }
    },
  },
  computed: {
    ...mapGetters({
      tableData: "menu/tableData",
      dialogVisible: "menu/dialogVisible",
      isLoading: "menu/isLoading",
      idKeyWithNameValueCategory: "category/idKeyWithNameValue",
    }),
  },
  async mounted() {
    this.getMenuDataAPI();
    await this.getCategoryData();
  },
};
</script>

<style>
.title {
  font-family: Rubik;
  font-size: 34px;
  font-style: normal;
  font-weight: 500;
  line-height: 44px;
  letter-spacing: -0.25px;
  text-align: left;
}

.sk-container {
  max-width: 80vh;
  margin: auto;
}

.button-no-border {
  border: none;
  color: var(--primary);
}
</style>

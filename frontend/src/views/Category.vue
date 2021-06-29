<template lang="">
  <div>
    <el-row>
      <el-col :span="10" :offset="6"> <h2>Cateogry</h2></el-col>
      <el-col :span="8">
        <el-button type="primary" round @click="createCateogry">+ Add New Category</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="15" :offset="5">
        <el-table
          :data="tableData"
          style="width: 100%"
          empty-text="ไม่มีข้อมูล">
          
            <el-table-column prop="name" label="Name" width="180">
            </el-table-column>
          
            <el-table-column prop="storeId" label="StoreId" width="180">
              <template slot-scope="scope">
                {{ idKeyWithNameValueStore[scope.row.storeId] }}
              </template> 
            </el-table-column>
            <el-table-column>
              <template slot-scope="scope">
                <el-button
                icon="el-icon-edit"
                @click="editCategory(scope.row)"
                circle></el-button>
                <el-button
                type="primary"
                icon="el-icon-document-copy"
                @click="copyCategory(scope.row)"
                circle
                style="margin-left: 0"
                slot="reference"></el-button>
                <el-button
                type="danger"
                icon="el-icon-delete-solid"
                @click="deleteCategory(scope.row.id)"
                circle
                slot="reference"></el-button>

              </template>  
          </el-table-column>
          
        </el-table>
      </el-col>
    </el-row>
    <el-dialog title="Create Category" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="Category Name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Store">
          <el-select
            filterable
            v-model="form.storeId"
            value-key="name"
          >
          <el-option
              v-for="item in storeData"
              :key="item.id"
              :label="item.name"
              :value="item.id"
            >
            </el-option
          ></el-select>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">Cancel</el-button>
        <el-button
          type="primary"
          @click="save"
          v-loading.fullscreen.lock="loading"
          >Confirm</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>
<script>
import editIcon from "../assets/edit.png";
import copyIcon from "../assets/copy.png";
import deleteIcon from "../assets/delete.png";
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      editIcon: editIcon,
      copyIcon: copyIcon,
      deleteIcon: deleteIcon,
      form: {
        name: "",
        storeId: "",
        id: ""
      },
      dialogFormVisible: false,
      loading: false,
      typeAction: 'create',
    };
  },
  methods: {
    ...mapActions({
      getCategory: "category/getCategoryData",
      getStore: "store/fetchStore",
      saveCategory: "category/save",
      saveEditCategory: "category/editSave",
      saveDeleteCategory: "category/deleteCategory",
    }),
    async save() {
      this.loading = true;
      if(this.typeAction === 'create')
        await this.saveCategory(this.form)
      else if(this.typeAction === 'edit')
        await this.saveEditCategory(this.form)
      this.loading = false;
      this.dialogFormVisible = false
    },
    async copyCategory(dataCategory){
      this.form.name = dataCategory.name
      this.form.storeId = dataCategory.storeId
      this.typeAction = 'create'
      
      this.$confirm('This will copy the category. Continue?', 'Warning', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(async() => {
          
          this.loading = true
          this.save()
          this.loading = false
          this.$message({
            type: 'success',
            message: 'copy completed'
          })
        })
    },
    async editCategory(dataCategory){
      this.dialogFormVisible = true
      this.form.name = dataCategory.name
      this.form.storeId = dataCategory.storeId
      this.typeAction = 'edit'
      this.form.id = dataCategory.id
    },
    async createCateogry(){
      this.dialogFormVisible = true
      this.typeAction = 'create'
    },
    async deleteCategory(id){
      this.$confirm('This will permanently delete the category. Continue?', 'Warning', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(async() => {
          
          this.loading = true
          await this.saveDeleteCategory(id)
          this.loading = false
          this.$message({
            type: 'success',
            message: 'Delete completed'
          })
        })
    }
  },
  async mounted() {
    this.loading = true
    await this.getCategory()
    this.loading = false
    await this.getStore();
  },
  computed: {
    ...mapGetters({
      tableData: "category/tableData",
      storeData: "store/getStore",
      idKeyWithNameValueStore: "store/idKeyWithNameValue",
    }),
  },
};
</script>
<style lang=""></style>

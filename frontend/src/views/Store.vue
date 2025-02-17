<template lang="">
  <div>
    <el-row>
      <el-col :span="10" :offset="6"> <h2>Store</h2></el-col>
      <el-col :span="8">
        <el-button type="primary" round @click="createStore">+ Add New Store</el-button>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="15" :offset="5">
        <el-table :data="tableData" style="width: 100%">
          <el-table-column prop="id" label="ID" width="180"> </el-table-column>
          <el-table-column prop="name" label="Name" width="180">
          </el-table-column>
          <el-table-column prop="description" label="Description">
          </el-table-column>
          <el-table-column prop="rating" label="Rating"> </el-table-column>
          <el-table-column>
            <template slot-scope="scope">
              <el-button
                icon="el-icon-edit"
                @click="editStore(scope.row)"
                circle></el-button>
                <el-button
                type="primary"
                icon="el-icon-document-copy"
                @click="copyStore(scope.row)"
                circle
                style="margin-left: 0"
                slot="reference"></el-button>
                <el-button
                type="danger"
                icon="el-icon-delete-solid"
                @click="deleteStore(scope.row.id)"
                circle
                slot="reference"></el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-dialog title="Create Store" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="Store Name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Description">
          <el-input v-model="form.description" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Rating">
          <el-input-number
            v-model="form.rating"
            :min="1"
            :max="10"
          ></el-input-number>
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
        description: "",
        rating: "",
        id: ""
      },
      dialogFormVisible: false,
      loading: false,
      typeAction: 'create',
    };
  },
  methods: {
    ...mapActions({
      getStore: "store/fetchStore",
      saveStore: "store/save",
      saveEditStore: "store/editSave",
      saveDeleteStore: "store/deleteStore",
    }),
    async save() {
      this.loading = true;
      if(this.typeAction === 'create')
        await this.saveStore(this.form)
      else if(this.typeAction === 'edit')
        await this.saveEditStore(this.form)
      this.loading = false;
      this.dialogFormVisible = false
    },
    async copyStore(dataStore){
      this.form.name = dataStore.name
      this.form.description = dataStore.description
      this.form.rating = dataStore.rating
      this.typeAction = 'create'
      
      this.$confirm('This will copy the store. Continue?', 'Warning', {
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
    async editStore(dataStore){
      this.dialogFormVisible = true
      this.form.name = dataStore.name
      this.form.description = dataStore.description
      this.form.rating = dataStore.rating
      this.typeAction = 'edit'
      this.form.id = dataStore.id
    },
    async createStore(){
      this.dialogFormVisible = true
      this.typeAction = 'create'
    },
    async deleteStore(id){
      this.$confirm('This will permanently delete the store. Continue?', 'Warning', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning'
        }).then(async() => {
          
          this.loading = true
          await this.saveDeleteStore(id)
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
    await this.getStore()
    this.loading = false
    
  },
  computed: {
    ...mapGetters({
      tableData: "store/getStore",
    }),
  },
};
</script>
<style lang=""></style>

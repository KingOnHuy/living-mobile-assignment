<template lang="">
  <div>
    <el-row>
      <el-col :span="10" :offset="6"> <h2>Store</h2></el-col>
      <el-col :span="8">
        <el-button type="primary" round @click="dialogFormVisible = true"
          >+ Add New Store</el-button
        >
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="15" :offset="5">
        <el-table :data="tableData" style="width: 100%" empty-text='ไม่มีข้อมูล'>
          <el-table-column prop="id" label="ID" width="180"> </el-table-column>
          <el-table-column prop="name" label="Name" width="180">
          </el-table-column>
          <el-table-column prop="description" label="Description">
          </el-table-column>
          <el-table-column prop="rating" label="Rating"> </el-table-column>
          <el-table-column>
            <el-image
              style="width: 30px; height: 30px; margin-right: 10px"
              :src="editIcon"
            ></el-image>
            <el-image
              style="width: 20px; height: 20px; margin-right: 10px"
              :src="copyIcon"
            ></el-image>
            <el-image
              style="width: 20px; height: 20px"
              :src="deleteIcon"
            ></el-image>
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
import { mapActions, mapGetters } from 'vuex';

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
      },
      dialogFormVisible: false,
      loading: false,
    };
  },
  methods: {
    ...mapActions({
      getStore: "store/fetchStore",
      saveStore: "store/save"
    }),
    async save() {
      await this.saveStore(this.form)
    }
  },
  async mounted() {
    this.loading = true
    await this.getStore()
    this.loading = false
  },
  computed: {
    ...mapGetters({
      tableData: "store/getStore"
    }),
  }
};
</script>
<style lang=""></style>

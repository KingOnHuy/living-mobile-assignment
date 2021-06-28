<template>
  <div
    class="d-flex justify-center align-center"
    style="height: calc(100vh - 60px)"
  >
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <el-image
          class="d-flex"
          :src="require('@/assets/FoodStory_Logo.png')"
          fit="contain"
        ></el-image>
      </div>
      <el-form
        :model="formData"
        :rules="rules"
        ref="ruleForm"
        v-loading="isLoading"
      >
        <div class="sub-title">Username</div>
        <el-input placeholder="Username" v-model="formData.username"></el-input>
        <div class="sub-title mt-2">Password</div>
        <el-input
          placeholder="Password"
          show-password
          v-model="formData.password"
        ></el-input>
        <el-button class="mt-4" @click="login">Login</el-button>
        <el-alert v-if="error" class="mt-3" :title="error" type="error">
        </el-alert>
      </el-form>
    </el-card>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "Login",
  data() {
    return {
      isLoading: false,
      formData: {
        username: "",
        password: "",
      },
      error: false,
      rules: {
        username: {
          validator: false,
          trigger: "blur",
        },
        password: {
          validator: false,
          trigger: "blur",
        },
      },
    };
  },
  methods: {
    ...mapActions({
      loginAPI: "auth/login",
    }),
    login() {
      this.error = null;
      this.isLoading = true;
      this.loginAPI(this.formData)
        .then(() => {
          this.isLoading = false;
        })
        .catch((error) => {
          this.isLoading = false;
          if (error.response.status === 401) {
            this.error = error.response.data.detail;
          } else if (error.response.status === 400) {
            this.error = error.response.data;
          }
        });
    },
  },
};
</script>

<style>
.el-card__header {
  background-color: var(--primary);
}
.box-card {
  min-width: 400px;
}
</style>

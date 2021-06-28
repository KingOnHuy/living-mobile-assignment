<template>
  <div>
    <el-menu
      :router="true"
      :default-active="activeIndex"
      mode="horizontal"
      @select="handleSelect"
      class="d-flex align-center"
    >
      <el-menu-item index="/">
        <el-image
          :src="require('@/assets/FoodStory_Logo.png')"
          fit="cover"
        ></el-image>
      </el-menu-item>
      <el-menu-item v-if="isLogin" index="store">Story</el-menu-item>
      <el-menu-item v-if="isLogin" index="category">Category</el-menu-item>
      <el-menu-item v-if="isLogin" index="menu">Menu</el-menu-item>
      <el-button
        v-if="!isLogin"
        class="ml mr-3"
        type="primary"
        @click="routerPush('Login')"
        plain
      >
        Login
      </el-button>
      <el-button v-else class="ml mr-3" type="primary" @click="logout" plain>
        Logout
      </el-button>
    </el-menu>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      activeIndex: "store",
    };
  },
  methods: {
    ...mapActions({
      logout: "auth/logout",
    }),
    handleSelect(n) {
      console.log(n);
    },
    routerPush(name) {
      if (this.$route.name != name) {
        this.$router.push(name);
      }
    },
  },
  computed: {
    ...mapGetters({
      isLogin: "auth/isLogin",
    }),
  },
};
</script>

<style>
.el-menu {
  height: 60px;
}

.el-menu-item {
  color: white !important;
}

.el-menu-item:hover {
  color: var(--primary) !important;
  background-color: #86d5fc;
}

.el-menu-item:focus {
  color: white !important;
  background-color: #86d5fc !important;
}

.is-active {
  border-bottom: 5px solid #92dbff !important;
}

.el-image__inner {
  height: 100%;
  margin-top: 14px;
}
</style>

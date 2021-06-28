<template>
  <div>
    <el-menu
      :router="true"
      :default-active="activeIndex"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item class="d-flex justify-center align-center" index="/">
        <el-image
          class="d-flex"
          :src="require('@/assets/FoodStory_Logo.png')"
          :fit="contain"
        ></el-image>
      </el-menu-item>
      <el-menu-item index="store">Story</el-menu-item>
      <el-menu-item index="category">Category</el-menu-item>
      <el-menu-item index="menu">Menu</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "store",
    };
  },
  methods: {
    handleSelect(n) {
      console.log(n);
    },
  },
  mounted() {},
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
  border-bottom: 2px solid #00aaff !important;
  background-color: #86d5fc;
}
</style>

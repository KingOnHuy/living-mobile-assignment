<template>
  <div>
    <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1">Story</el-menu-item>
      <el-menu-item index="2">Category</el-menu-item>
      <el-menu-item index="3">Menu</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {};
</script>

<style>
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

<template>
  <div id="app">
    <!-- <v-header></v-header> -->
    <el-menu
      active-text-color= "teal"
      id="header-containter" :default-active="activeIndex" mode="horizontal" router>
      <el-menu-item index="home" :route="{ name:'home' }">明細情報</el-menu-item>
      <el-menu-item index="dashboard" :route="{ name:'dashboard' }">ダッシュボード</el-menu-item>
      <el-menu-item index="import" :route="{ name:'import' }">インポート</el-menu-item>
    </el-menu>
    <router-view/>
    <v-footer> 
    </v-footer>

  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      activeIndex: this.$route.name
    }
  }
}
</script>

<style scoped>
#header-containter {
  padding: 0px 145px 0px 145px;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
}
a {
  text-decoration: none;
}
.el-menu.el-menu--horizontal {
  box-shadow: rgba(0, 0, 0, 0.18) 0 0 4px 0;
  padding: 0 25px;
}
</style>
<template>
 <el-header
  height="48px"
 >
  <div class="demo-basic--circle">
    <el-avatar size="small" :src="circleUrl"></el-avatar>
  </div>
 </el-header>
</template>
<script>
  export default {
    data () {
      return {
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
      }
    }
  }
</script>

<style lang="scss">
header {
  background: teal;
  width: 100%;
  margin: 0px;
}

.demo-basic--circle {
  float: right;
  padding-right: 27px;
  padding: 9px 28px 0 0;
}

</style>
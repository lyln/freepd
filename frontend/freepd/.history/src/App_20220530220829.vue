<template>
	<div id="app">
		<router-view />
	</div>
</template>

<script>
export default {
	name: 'App',
}
</script>

<style>
#app {
	/* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
	font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
			font-size: 12px;
    		background-color: #ecf0f3;
   			color: #a0a5a8
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	/* color: #2c3e50; */
	color: #34495e;
	margin-top: 10px;
	/* background-color: #fff; */
}
</style>

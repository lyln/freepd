<template>

	<el-row>
		<el-col :span="24">
			<div class="grid-content bg-purple-dark"></div>

			<div class="hello">
				<h1>{{ msg }}</h1>
			</div>
		</el-col>
	</el-row>

</template>

<script>
export default {
	name: 'HelloWorld',
	data() {
		return {
			msg: 'free parse download',
		}
	},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
	font-weight: normal;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}
</style>

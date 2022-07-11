<template>
	<el-container>
		<el-main></el-main>
	</el-container>

</template>
<script>
export default {
	name: 'HelloWorld',
	data() {
		return {
			msg: 'free parse download',
			form: {
				url: '',
				type: [],
			},
		}
	},
	methods: {
		onSubmit() {
			console.log('submit!')
		},
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

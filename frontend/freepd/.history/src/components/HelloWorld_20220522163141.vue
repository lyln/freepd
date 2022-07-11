<template>
	<el-row>
		<el-col :span="24">
			<div class="grid-content bg-purple-dark"></div>

			<el-form ref="form" :model="form" label-width="80px">
				<el-form-item label="活动名称">
					<el-input v-model="form.url"></el-input>
				</el-form-item>
				<el-form-item label="特殊资源">
					<el-radio-group v-model="form.resource">
						<el-radio label="线上品牌商赞助"></el-radio>
						<el-radio label="线下场地免费"></el-radio>
					</el-radio-group>
				</el-form-item>
				<el-form-item label="活动形式">
					<el-input type="textarea" v-model="form.desc"></el-input>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" @click="onSubmit">在线解析</el-button>
					<el-button>取消</el-button>
				</el-form-item>
			</el-form>

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

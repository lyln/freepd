<template>
	<el-container>
		<el-header></el-header>
		<el-main style="wide: 80%">
			<el-row>
				<el-col :span="24">
					<div class="grid-content bg-purple-dark"></div>

					<el-form ref="form" :model="form" label-width="120px" class="fpd-form">
						<el-form-item label="分享链接内容">
							<el-input v-model="form.url"></el-input>
						</el-form-item>
						<el-form-item label="平台" label-width="120px">
							<el-radio-group v-model="form.type">
								<el-radio :label="1">抖音</el-radio>
								<el-radio :label="2">网易云</el-radio>
								<el-radio :label="3">快手</el-radio>
							</el-radio-group>
						</el-form-item>
						<el-form-item>
							<el-button type="primary" @click="onSubmit">在线解析</el-button>
						</el-form-item>
					</el-form>

				</el-col>
			</el-row>
		</el-main>
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
				type: 1,
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
.el-input {
	width: 320px;
}

.fpd-form {
	text-align: left;
}
</style>
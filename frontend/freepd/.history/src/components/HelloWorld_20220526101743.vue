<template>
	<el-row type="flex" justify="center">
		<el-col :span="18">
			<div class="grid-content bg-purple-light">
				<el-form ref="form" :model="form" label-width="120px" class="fpd-form">
					<el-form-item label="链接地址：" style="padding: 25px;">
						<el-input v-model="form.url"></el-input>
					</el-form-item>
					<el-form-item label="平台：" label-width="120px">
						<el-radio-group v-model="form.type">
							<el-radio :label="1">抖音</el-radio>
							<el-radio :label="2">网易云</el-radio>
							<el-radio :label="3">快手</el-radio>
						</el-radio-group>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" @click="onSubmit">在线解析</el-button>
					</el-form-item>
					<el-form-item label="视频地址：">
						<i class="el-icon-video-play"></i>
						<el-link :href="data.video.play" target="_blank">{{ data.title }}</el-link>
						<!-- {{data.video.play }} -->
					</el-form-item>
				</el-form>
			</div>
		</el-col>
	</el-row>

</template>
<script>
import axios from 'axios'
export default {
	name: 'HelloWorld',
	data() {
		return {
			msg: 'free parse download',
			form: {
				url: 'https://v.douyin.com/FqxyAp8/',
				type: 1,
			},
			data: {
				video: { play: '' },
				title: '',
			},
		}
	},
	metaInfo: {
		meta: [{ name: 'referrer', content: 'no-referrer' }],
	},
	methods: {
		onSubmit() {
			console.log('submit!')
			axios
				.post('http://127.0.0.1:8000/douyin', { url: this.form.url })
				.then((res) => {
					console.log(res.data)
					this.data = res.data
				})
				.catch((err) => {
					console.log('请求失败', err)
				})
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

/* .text {
	font-size: 14px;
}

.item {
	padding: 18px 0;
}

.box-card {
	width: 480px;
} */

.el-row {
	margin-bottom: 20px;
	&:last-child {
		margin-bottom: 0;
	}
}
.el-col {
	border-radius: 4px;
}
.bg-purple-light {
	background: #f5f7fa;
}
.grid-content {
	border-radius: 4px;
	min-height: 36px;
}
.row-bg {
	padding: 10px 0;
	background-color: #f9fafc;
}
.el-form-item {
	margin-bottom: 10px;
}

.el-form-item label:after {
	content: '';
	display: inline-block;
	width: 100%;
}

.el-form-item__label {
	text-align: justify;
	height: 50px;
}

.el-form-item.is-required .el-form-item__label:before {
	content: none !important;
}
</style>
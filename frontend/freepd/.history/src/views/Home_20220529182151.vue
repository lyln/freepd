
<template>
	<div class="home">
		<el-row type="flex" class="row-bg" justify="center">
			<div class="grid-content bg-purple">
				<el-col :span="18">
					<el-form ref="form" :model="form" label-width="80px">

						<el-form-item label="链接地址:" style="margin-top: 20px">
							<el-input v-model="form.url" size="small" style="width: 80%"></el-input>
						</el-form-item>
						<el-form-item label="平台:">
							<el-radio-group v-model="form.type">
								<el-radio :label="1">抖音</el-radio>
								<el-radio :label="2">网易云</el-radio>
								<el-radio :label="3">快手</el-radio>
								<el-radio :label="4">荔枝FM</el-radio>
								<el-radio :label="5">B站</el-radio>
							</el-radio-group>
						</el-form-item>

						<el-form-item>
							<el-button type="primary" size="small" @click="onSubmit">在线解析</el-button>
						</el-form-item>

						<el-form-item label="解析地址:">
							<!-- <el-link>视频地址</el-link> -->
							<video width="480" height="360" controls="controls" v-if='videoUrl' :src="videoUrl">
								<!-- <source :src="videoUrl" type="video/ogg" :key="vidioKey"> -->
								Your browser does not support the video tag.
							</video>
							<br v-if="videoUrl">
							<audio width="260" ref="audio" v-if="audioUrl" class="audio" :src="audioUrl" controls="controls">Your browser does not support the audio tag.</audio>

						</el-form-item>

					</el-form>

				</el-col>
			</div>

		</el-row>
	</div>
</template>

<script>
import { douyin, wangyiyun, kuaishou, lizhiFM, bilibili } from '@/api/parse'

export default {
	name: 'Home',
	data() {
		return {
			form: {
				url: 'https://v.douyin.com/F7XTnF2/',
				type: 1,
			},
			videoUrl: '',
			audioUrl: '',
			vidioKey: 1,
		}
	},
	methods: {
		onSubmit() {
			switch (this.form.type) {
				case 1:
					douyin(this.form)
						.then((res) => {
							console.log(res.data)
							this.videoUrl = res.data.video.play
							this.audioUrl = res.data.music.play
						})
						.catch((err) => {
							console.log('抖音解析请求失败', err)
						})
					break
				case 2:
					wangyiyun(this.form)
						.then((res) => {
							var dataUrl = res.data.data
							if (dataUrl.videos) {
								this.videoUrl = dataUrl.videos[0]
							} else {
								this.videoUrl = ''
								this.audioUrl = dataUrl.audios[0]
							}
						})
						.catch((err) => {
							console.log('网易云解析请求失败', err)
						})
					break
				case 3:
					kuaishou(this.form)
						.then((res) => {
							var dataUrl = res.data
							if (dataUrl.video) {
								this.videoUrl = dataUrl.video
								this.audioUrl = ''
							}
						})
						.catch((err) => {
							console.log('快手解析请求失败', err)
						})
					break
				case 4:
					lizhiFM(this.form)
						.then((res) => {
							var dataUrl = res.data
							if (dataUrl.voice_url) {
								this.videoUrl = ''
								this.audioUrl = dataUrl.voice_url
							}
						})
						.catch((err) => {
							console.log('荔枝FM解析请求失败', err)
						})
					break
				case 5:
					bilibili(this.form)
						.then((res) => {
							var dataUrl = res.data.data
							console.log(dataUrl)
							console.log(dataUrl.videos[0])
							if (dataUrl.videos) {
								this.videoUrl = dataUrl.videos[0]
								this.audioUrl = ''
							}
						})
						.catch((err) => {
							console.log('b站解析请求失败', err)
						})
					break
				default:
					console.log('解析请求失败')
			}
		},
	},
	// watch: {
	// 	videoRefresh() {
	// 		++this.vidioKey
	// 	},
	// },
}
</script>

<style lang="css" scoped>
.home {
	padding: 25px;
	background-color: #ecf0f3;
	box-shadow: 10px 10px 10px #d1d9e6, -10px -10px 10px #f9f9f9;
	border-radius: 12px;
}
/* .row-bg {
	background-color: #c0c4cc;
	background-color: #f9fafc;
} */

/* .bg-purple {
	margin: 20px 0;
	background: #f2f6fc;
	box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
} */
.grid-content {
	border-radius: 4px;
	width: 80%;
}

.el-form-item {
	text-align: left;
}

.el-radio {
	margin-right: 20px;
}

video {
	object-fit: contain;
}

audio {
	object-fit: fill;
}
</style>
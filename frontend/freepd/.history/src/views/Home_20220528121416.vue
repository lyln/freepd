
<template>
	<div class="home">
		<el-row type="flex" class="row-bg" justify="center">
			<div class="grid-content bg-purple">
				<el-col :span="18">
					<el-form ref="form" :model="form" label-width="80px">

						<el-form-item label="链接地址:" style="margin-top: 20px">
							<el-input v-model="form.url" size="small" style="width: 50%"></el-input>
						</el-form-item>
						<el-form-item label="平台:">
							<el-radio-group v-model="form.type">
								<el-radio :label="1">抖音</el-radio>
								<el-radio :label="2">网易云</el-radio>
								<el-radio :label="3">快手</el-radio>
							</el-radio-group>
						</el-form-item>

						<el-form-item>
							<el-button type="primary" size="small">在线解析</el-button>
						</el-form-item>

						<el-form-item label="解析地址:">
							<!-- <el-link>视频地址</el-link> -->
							<video width="480" height="360" controls="controls" v-if='videoUrl'>
								<source :src="videoUrl" type="video/ogg">
								Your browser does not support the video tag.
							</video>
							<br>
							<audio width="260" ref="audio" v-if="audioUrl" class="audio" :src="audioUrl" controls="controls">Your browser does not support the audio tag.</audio>

						</el-form-item>

					</el-form>

				</el-col>
			</div>

		</el-row>
	</div>
</template>

<script>
import { douyin } from '@/api/parse'

export default {
	name: 'Home',
	data() {
		return {
			form: {
				url: '',
				type: 1,
			},
			videoUrl:
				'https://v6-x.douyinvod.com/9bdffe21d2d7ba1e3b3d5b9ce82792eb/6291ac29/video/tos/cn/tos-cn-ve-15c001-alinc2/5bd5701b6a7e4b42ba9fdafbb705d8a0/?a=1128&ch=0&cr=0&dr=0&cd=0%7C0%7C0%7C0&cv=1&br=1527&bt=1527&btag=80000&cs=0&ds=3&ft=X5zkayvvBQ3AUq8yq8Z.wNnOYZlc3VvhF2bLNHGXYiZm&mime_type=video_mp4&qs=0&rc=aWc1PDc5ZGk3ZjM6OmllM0BpMzdsZmg6ZnJmPDMzNGkzM0AvNmEwLzQtNjExLmBjYC5eYSNxMS5rcjRvcGRgLS1kLS9zcw%3D%3D&l=20220528115510010212144157443C7844',
			audioUrl:
				'http://m10.music.126.net/20220528103309/8ed958c4a14a3bcf18196cdc1f0aee06/ymusic/e7c9/8e15/13f8/d2b862d7a4fe4a1fa7e4def64d6827c5.mp3',
		}
	},
    methods: {
		onSubmit() {
	        console.log('submit!')
            douyin(this.form.url).then(response => {        
                this.data = response.data
            })
	},
}
</script>

<style lang="css" scoped>
.home {
}
.row-bg {
	background-color: #c0c4cc;
}

.bg-purple {
	margin: 20px 0;
	background: #f2f6fc;
	box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
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
	object-fit: fill;
}

audio {
	object-fit: fill;
}
</style>
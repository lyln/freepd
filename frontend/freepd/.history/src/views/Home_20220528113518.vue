
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
export default {
	name: 'Home',
	data() {
		return {
			form: {
				url: '',
				type: 1,
			},
			videoUrl:
				'https://v26.douyinvod.com/d7b990ab42ccfd6e9313430e3e3a8230/6290f187/video/tos/cn/tos-cn-ve-15c001-alinc2/8468cfae98c3415a88652fd96a2cb880/?a=1128&ch=96&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1025&bt=1025&btag=80000&cs=0&ds=6&ft=X5zkayvvBQ3AUq8yq8Z.wNnOYZlcKxXhF2bLNHGXYiZm&mime_type=video_mp4&qs=0&rc=PGg8ZTk7ODplNGc8NDQ5ZkBpamt4N2Q6Zmk0PDMzNGkzM0AxMmI2MF4xXjAxMi0zMy5hYSNeLm9qcjRnZl5gLS1kLS9zcw%3D%3D&l=2022052722424101021206315943167C76',
			audioUrl:
				'http://m10.music.126.net/20220528103309/8ed958c4a14a3bcf18196cdc1f0aee06/ymusic/e7c9/8e15/13f8/d2b862d7a4fe4a1fa7e4def64d6827c5.mp3',
		}
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
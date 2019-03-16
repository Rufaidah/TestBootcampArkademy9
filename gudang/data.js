var app = new Vue({
	el: '#app',
	data: {
		items: [],
		item: '',
		id: 0
	},

	created() {
		axios.get('ajaxfile.php').then((response) => {
					console.log(response.data)
					this.items = response.data
		})
		.catch(function (error){
			console.log(error);
		});
	}
})
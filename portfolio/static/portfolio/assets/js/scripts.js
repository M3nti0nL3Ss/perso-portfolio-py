const get = (ele) => document.querySelector(ele);
get(".menu").addEventListener('click', ()=>{
	var sidebar = get("#sidebar");
	var wrapper = get("#wrapper");
	var footer = get("#footer");
	if(!sidebar.classList.contains("zero-left") || sidebar.classList ==""){
		wrapper.classList.add("moindizwit-right");
		wrapper.classList.add("dizwit-left");
		sidebar.classList.add("zero-left");
		footer.classList.add("dizwit-left");
		footer.classList.add("moindizwit-right");
	}else{
		wrapper.classList.remove("moindizwit-right");
		wrapper.classList.remove("dizwit-left");
		sidebar.classList.remove("zero-left");
		footer.classList.remove("dizwit-left");
		footer.classList.remove("moindizwit-right");
	}
});

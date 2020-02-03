const runCKDITOR = () => {
var labels = document.getElementsByTagName('label');
for (var i = 0; i < labels.length; i++) {       
if(labels[i].htmlFor == "id_description"){ 
labels[i].parentNode.removeChild(labels[i]);
}
}
CKEDITOR.replace('description')};

window.onload = runCKDITOR;

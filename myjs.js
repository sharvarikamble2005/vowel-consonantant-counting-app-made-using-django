function check(event)
{
	let txt=document.getElementById("id_txt");
	let msg=document.getElementById("id_msg");
	if(txt.value==="")
	{
		alert("txt is empty")
		msg.textContent="";
		txt.focus();
		return false;
	}
	return true;
}
function xnjy_init() {
	var ui_type =  get_query_string("ui_type",1);
	if(0 != ui_type) {
		document.body.style.background = "#ffc703";
	} else {
		document.body.style.background = "#0303ff";
	}

    var bl = 1.0;
    var back = document.getElementById('div_back');
    var back_height = $(back).height();
    var back_width = $(back).width();
    bl = back_height / 1920.0;

    var img_back = document.getElementById('img_back');
    img_back.style.height = back_height + "px";
    img_back.style.width = back_height * 0.5625 + "px";
    //img_back.style.width = "100%";

    var div_cont = document.getElementById('div_cont');
    div_cont.style.height = back_height + "px";
	//div_cont.style.width = "100%";
    div_cont.style.width = back_height * 0.5625 + "px";
    div_cont.style.marginLeft = (back_width - back_height * 0.5625 ) / 2 + "px";
}
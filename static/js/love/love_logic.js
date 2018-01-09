var show_len = 0;
/**是否为横屏*/
var is_h = true;

function goto_show() {
    console.log("show");
    document.getElementById("us_record").style.display = "none";
    document.getElementById("future").style.display = "inline";
    // var self_url = window.location.href;
    // var obj_url = self_url.indexOf("#") >= 0 ? self_url : self_url + "#future";
    // window.location.href = obj_url;
}

function start_love() {
    offsetX = $("#loveHeart").width() / 2;
    offsetY = $("#loveHeart").height() / 2 - 55;
    together = new Date();
    together.setFullYear(2018, 0, 18);
    together.setHours(11);
    together.setMinutes(45);
    together.setSeconds(0);
    together.setMilliseconds(0);

    if (!document.createElement('canvas').getContext) {
        var msg = document.createElement("div");
        msg.id = "errorMsg";
        msg.innerHTML = "Your browser doesn't support HTML5!<br/>Recommend use Chrome 14+/IE 9+/Firefox 7+/Safari 4+";
        document.body.appendChild(msg);
        document.execCommand("stop");
    } else {
        setTimeout(function () {
            startHeartAnimation();
        }, 500);

        timeElapse(together);
        setInterval(function () {
            timeElapse(together);
        }, 500);

        adjustCodePosition();
        $("#code").typewriter();
    }
}

var UNIT_DAY = "<span class='item_unit'> 天 </span>";
var UNIT_HOUR = "<span class='item_unit'> 小时 </span>";
var UNIT_MIN = "<span class='item_unit'> 分钟 </span>";
var UNIT_SECOND = "<span class='item_unit'> 秒 </span>";
var UNIT_PASSED = "<span class='item_unit'>已经过去 </span>";
var UNIT_LIMIT = "<span class='item_unit'>还有 </span>";

/**
 *  计时
 * @param time_id
 * @param timestamp2
 */
function item_count_time(time_id, timestamp2) {
    var time_item = document.getElementById("far" + time_id);
    var date3 = parseInt((new Date()).getTime() - timestamp2);

    //显示时间
    var days = parseInt(date3 / (1000.0 * 60 * 60 * 24)); //Math.abs((date1.getDate() - date2.getDate()));
    //计算出小时数
    var leave1 = date3 % (24 * 3600 * 1000);   //计算天数后剩余的毫秒数
    var hours = Math.floor(leave1 / (3600 * 1000));
    if (hours < 10) {
        hours = "0" + hours;
    }
    //计算相差分钟数
    var leave2 = leave1 % (3600 * 1000);    //计算小时数后剩余的毫秒数
    var minutes = Math.floor(leave2 / (60 * 1000));
    if (minutes < 10) {
        minutes = "0" + minutes;
    }
    var leave3 = leave2 % (60 * 1000) - 1;
    var seconds = Math.round(leave3 / 1000);
    if (seconds < 10) {
        seconds = "0" + seconds;
    }
    var sfix = date3 > 0 ? UNIT_PASSED : UNIT_LIMIT;
    time_item.innerHTML = "<div id='limit_" + time_id + "' class='item_num'>" //
        + sfix + days + UNIT_DAY
        + hours + UNIT_HOUR
        + minutes + UNIT_MIN
        + seconds + UNIT_SECOND//
        + "</div>";

    setTimeout("item_count_time(" + time_id + "," + timestamp2 + ")", 1000);
}

var ANINS = ['tlayui-anim-down', 'tlayui-anim-up', 'tlayui-anim-fadin'];//, 'tlayui-anim-left', 'tlayui-anim-right'];
// var ANINS = ['tlayui-anim-left', 'tlayui-anim-right'];

/**
 * 显示项
 */
var show_item = function (item_id) {
    var item = document.getElementById("item" + item_id);
    item.style.visibility = "visible";
    item.setAttribute("class", "tlayui-anim " + ANINS[(item_id - 1) % ANINS.length]);
};
<<<<<<< HEAD

var TIME_UNIT = 2000;
=======
>>>>>>> b32fb1dd732da9417b1a6aa0d77b68ead3a69765

function count_time() {
    for (var i = 1; i <= show_len; i++) {
        var stime = document.getElementById("time" + i).innerHTML;
        var timestamp2 = Date.parse(new Date(stime));
        document.getElementById("time" + i).innerHTML = stime.substr(0, 10);
        item_count_time(i, timestamp2);
<<<<<<< HEAD
        setTimeout("show_item(" + i + ")", TIME_UNIT * (i - 1));
=======
        setTimeout("show_item(" + i + ")", 1000 * (i - 1));
>>>>>>> b32fb1dd732da9417b1a6aa0d77b68ead3a69765
    }
}

function love_init(len) {
    show_len = len;

    var back = document.getElementById('us_record');
    var back_height = $(back).height();
    var back_width = $(back).width();
<<<<<<< HEAD
    var pic_fix = "/static/img/love/";
    if (back_height > back_width) {
        pic_fix += "v/";
    } else {
        pic_fix += "h/";
    }
    var pic_id = parseInt(Math.random() * 6);
    var pic_path = pic_fix + pic_id + ".jpg";
    document.getElementById("img_back").src = pic_path;

    count_time();

    //超时跳转
    setTimeout(function () {
        goto_show();
        start_love();
        startSnow();
    }, (len + 1) * TIME_UNIT);
=======

    count_time();

    // //超时跳转
    // setTimeout(function () {
    //     goto_show();
    //     start_love();
    //     startSnow();
    // }, len * 1000);
>>>>>>> b32fb1dd732da9417b1a6aa0d77b68ead3a69765


    jssdk_share();
}


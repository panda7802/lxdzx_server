function goto_show() {
    var self_url = window.location.href;
    var obj_url = self_url.indexOf("#") >= 0 ? self_url : self_url + "#future";
    window.location.href = obj_url;
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

function item_count_time(time_item, timestamp2) {
    if ((null === time_item) || (undefined === time_item)) {
        return;
    }
    var date3 = parseInt((new Date()).getTime() - timestamp2);
    var days = parseInt(date3 / (1000.0 * 60 * 60 * 24)); //Math.abs((date1.getDate() - date2.getDate()));
    //计算出小时数
    var leave1 = date3 % (24 * 3600 * 1000);   //计算天数后剩余的毫秒数
    var hours = Math.floor(leave1 / (3600 * 1000));
    if (hours < 10) {
        hours = "0" + hours;
    }
    //计算相差分钟数#}
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
    var sfix = date3 > 0 ? "已经过去 " : "还有 ";
    time_item.innerHTML = sfix + days + "天" + hours + "小时" + minutes + "分钟" + seconds + "秒"

    setTimeout("item_count_time('time_item', 'timestamp2')", 1000);
}

var items = new Array();
var stimes = new Array();

function count_time() {
    for (var i = 1; i <= 5; i++) {
        var time_item = document.getElementById("far" + i);
        console.log("far" + i + "------" + document.getElementById("far" + i))
        if ((null === time_item) || (undefined === time_item)) {
            console.log("break");
            break;
        }
        var stime = document.getElementById("time" + i).innerHTML;
        var timestamp2 = Date.parse(new Date(stime));
        items[i] = time_item;
        stimes[i] = timestamp2;
        item_count_time(time_item, timestamp2);
        // // var bak = document.getElementById("far" + i);
        // var bak = i;
        // setInterval(function () {
        //     item_count_time(items[bak], stimes[bak]);
        // }, 1000);
    }
}

function love_init() {
    start_love();
    startSnow();
    count_time();

    //超时跳转
    // setTimeout("goto_show()", 1000);
    jssdk_share();
}


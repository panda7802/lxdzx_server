var back_width = 0;
var back_height = 0;
var pic_unit = 128;

/**
 * 获取背景信息
 */
function init_back_info() {
    var back = document.getElementById('back');
    back_width = $(back).width();
    back_height = $(back).height();
    pic_unit = 256;// parseInt(back_width * 0.1);
}

function upd_pic_style() {
    var pieces = document.getElementsByClassName("piece");
    console.log(pieces);
    // pieces.forEach(function (i) {
    for (var i = 0; i < pieces.length; i++) {
        pieces[i].style.width = pic_unit + "px";
        pieces[i].style.height = pic_unit + "px";
    }
    // })
}

function init_photo() {
    if (typeof window.screenX !== "number") {
        alert("你好，养猪场不是飞机场，是开不了战斗机的！");
        return;
    }

    init_back_info();

    // 随机颜色HSL
    var randomHsl = function () {
            return "hsla(" + Math.round(360 * Math.random()) + "," + "60%, 50%, .75)";
        }
        // CSS transform变换应用
        , transform = function (element, value, key) {
            key = key || "Transform";
            ["Moz", "O", "Ms", "Webkit", ""].forEach(function (prefix) {
                element.style[prefix + key] = value;
            });

            return element;
        }
        // 浏览器选择器API
        , $ = function (selector) {
            return document.querySelector(selector);
        }, $$ = function (selector) {
            return document.querySelectorAll(selector);
        };

    // 显示图片
    var htmlPic = '', arrayPic = [1, 2, 3, 4, 5, 6], rotate = 360 / arrayPic.length;

    arrayPic.forEach(function (i) {
        htmlPic = htmlPic + '<img id="piece' + i + '" src="/static/img/love/photo/' + i + '.jpg" class="piece" />';
    });

    // 元素
    var eleStage = $("#stage"), eleContainer = $("#container"), indexPiece = 0;
    // 元素
    var elePics = $$(".piece"), transZ = parseInt(pic_unit / 2) / Math.tan((rotate / 2 / 180) * Math.PI);

    eleContainer.innerHTML = htmlPic;
    eleContainer.addEventListener("click", function () {
        transform(this, "rotateY(" + (-1 * rotate * ++indexPiece) + "deg)");
    });

    arrayPic.forEach(function (i, j) {
        transform($("#piece" + i), "rotateY(" + j * rotate + "deg) translateZ(" + (transZ + 15) + "px)");
    });

    // 垂直位置居中 - Chrome浏览器
    var funStageValign = function (element) {
        var scrollTop = document.documentElement.scrollTop, clientHeight = document.documentElement.clientHeight;
        offsetTop = element.getBoundingClientRect().top;

        if (parseInt(window.getComputedStyle(element).top) === 0) {
            element.style.top = scrollTop + (window.innerHeight - 300) / 2 - offsetTop;
        } else {
            element.style.top = "0px";
        }
    };
    //
    // if (/chrome/i.test(navigator.userAgent)) {
    //     // 创建Chrome浏览器视区修正按钮
    //     var eleButton = document.createElement("input");
    //     var arrValue = ["舞台位置窗体区域垂直居中", "垂直位置还原"];
    //
    //     eleButton.type = "button";
    //     eleButton.value = arrValue[0];
    //     eleButton.className = "chrome_fix";
    //     eleButton.addEventListener("click", function () {
    //         this.value = arrValue[Number(this.value !== arrValue[1])];
    //         var stage = this.parentNode;
    //         funStageValign(stage);
    //     });
    //
    //     eleStage.appendChild(eleButton);
    // }


    upd_pic_style();

}

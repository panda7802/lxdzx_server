String.prototype.format = function (args) {
    var result = this;
    if (arguments.length > 0) {
        if (arguments.length == 1 && typeof (args) == "object") {
            for (var key in args) {
                if (args[key] != undefined) {
                    var reg = new RegExp("({" + key + "})", "g");
                    result = result.replace(reg, args[key]);
                }
            }
        } else {
            for (var i = 0; i < arguments.length; i++) {
                if (arguments[i] != undefined) {
                    var reg = new RegExp("({[" + i + "]})", "g");
                    result = result.replace(reg, arguments[i]);
                }
            }
        }
    }
    return result;
};


function get_query_string(name, def) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
    if (r !== null) {
        return decodeURIComponent(r[2])
    }
    return def === null ? "" : def;
}


var poems = ["鸿雁在云鱼在水，惆怅此情难寄",//
    "离恨却如春草，更行更远还生",//
    "欲寄彩笺兼尺素，山长水阔知何处",//
    "终日两相思，为君憔悴尽，百花时",//
    "还卿一钵无情泪，恨不相逢未剃时",//
    "泪纵能乾终有迹，语多难寄反无词",//
    "临别殷勤重寄词，词中有誓两心知",//
    "明月不谙离恨苦，斜光到晓穿朱户",//
    "开辟鸿蒙，谁为情种？都只为风月情浓",//
    "若教眼底无离恨，不信人间有白头",//
    "离愁渐远渐无穷，迢迢不断如春水",//
    "相思本是无凭语，莫向花牋费泪行",//
    "直缘感君恩爱一回顾，使我双泪长珊珊",//
    "相思一夜梅花发，忽到窗前疑是君",//
    "别来半岁音书绝，一寸离肠千万结",//
    "唯将终夜长开眼，报答平生未展眉",//
    "无情不似多情苦，一寸还成千万缕",//
    "多情自古伤离别，更那堪，冷落清秋节",//
    "从别後，忆相逢，几回魂梦与君同",//
    "夜月一帘幽梦，春风十里柔情",//
    "同心而离居，忧伤以终老",//
    "不知魂已断，空有梦相随除却天边月，没人知",//
    "妾似胥山长在眼，郎如石佛本无心",//
    "休言半纸无多重，万斛离愁尽耐担",//
    "生当复来归，死当长相思",//
    "思君如明烛，煎心且衔泪",//
    "明月楼高休独倚，酒入愁肠，化作相思泪",//
    "若有知音见采，不辞遍唱阳春",//
    "花红易衰似郎意，水流无限似侬愁",//
    "多情只有春庭月，犹为离人照落花",//
    "若问闲情都几许？一川烟草，满城风絮，梅子黄时雨",//
    "锺情怕到相思路盼长堤，草尽红心动愁吟，碧落黄泉，两处难寻",//
    "瘦影自怜秋水照，卿须怜我我怜卿",//
    "泪眼问花花不语，乱红飞过秋千去",//
    "滴不尽相思血泪抛红豆，开不完春柳春花满画楼",//
    "人如风後入江云，情似雨馀黏地絮",//
    "都道是金玉良缘，俺只念木石前盟空对著，山中高士晶莹雪；终不忘，世外仙姝寂寞林",//
    "天涯地角有穷时，只有相思无尽处",//
    "玲珑骰子安红豆，入骨相思知不知",//
    "相恨不如潮有信，相思始觉海非深忍把千金酬一笑？毕竟相思，不似相逢",//
    "相思似海深，旧事如天远",//
    "春心莫共花争发，一寸相思一寸灰",//
    "忆君心似西江水，日夜东流无歇时",//
    "换我心，为你心，始知相忆深",//
    "诚知此恨人人有，贫贱夫妻百事哀",//
    "执手相看泪眼，竟无语凝噎",//
    "鱼沈雁杳天涯路，始信人间别离苦",//
    "愿我如星君如月，夜夜流光相皎洁",//
    "不要因为也许会改变，就不肯说那句美丽的誓言，不要因为也许会分离，就不敢求一次倾心的相遇",//
    "天长路远魂飞苦，梦魂不到关山难，长相思，摧心肝",//
    "一场寂寞凭谁诉算前言，总轻负",//
    "寻好梦，梦难成况谁知我此时情；枕前泪共帘前雨，隔箇窗儿滴到明",//
    "结发为夫妻，恩爱两不疑",//
    "梧桐树，三更雨，不道离情正苦一叶叶，一声声，空阶滴到明",//
    "千金纵买相如赋，脉脉此情谁诉",//
    "可怜无定河边骨，犹是春闺梦裏人",//
    "落花人独立，微雨燕双飞",//
    "只愿君心似我心，定不负相思意",//
    "此去经年，应是良辰好景虚设便纵有，千种风情，更与何人说",//
    "人生自是有情痴，此恨不关风与月",//
    "关关雎鸠，在河之洲+窈宨淑女，君子好逑",//
    "尊前拟把归期说，未语春容先惨咽",//
    "他生莫作有情痴，人间无地著相思",//
    "春蚕到死丝方尽，蜡炬成灰泪始乾",//
    "一个是阆苑仙葩，一个是美玉无瑕；若说没奇缘，今生偏又遇著他；若说有奇缘，如何心事终虚话？",//
    "重叠泪痕缄锦字，人生只有情难死",//
    "在天愿作比翼鸟，在地愿为连理枝",//
    "天长地久有时尽，此恨绵绵无绝期",//
    "今夕何夕，见此良人",//
    "十年生死两茫茫，不思量，自难忘，千里孤坟，无处话凄凉",//
    "一寸相思千万绪，人间没箇安排处",//
    "平生不会相思，才会相思，便害相思",//
    "兽炉沈水烟，翠沼残花片，一行行写入相思传",//
    "身无彩凤双飞翼，心有灵犀一点通",//
    "问世间，情是何物，直教生死相许",//
    "相思一夜情多少，地角天涯未是长",//
    "此情可待成追忆，只是当时已惘然",//
    "人到情多情转薄，而今真个不多情",//
    "深知身在情长在，怅望江头江水声",//
    "直道相思了无益，未妨惆怅是清狂",//
    "似此星辰非昨夜，为谁风露立中宵",//
    "天不老，情难绝心似双丝网，中有千千结",//
    "落红不是无情物，化作春泥更护花",//
    "相见争如不见，有情何似无情",//
    "自君之出矣，明镜暗不治思君如流水，何有穷已时",//
    "相思树底说相思，思郎恨郎郎不知",//
    "嗟余只影系人间，如何同生不同死",//
    "如何让你遇见我，在我最美丽的时刻为这，我已在佛前求了五百年，求他让我们结一段尘缘",//
    "还君明珠双泪垂，恨不相逢未嫁时",//
    "凄凉别後两应同，最是不胜清怨月明中",//
    "君若扬路尘，妾若浊水泥，浮沈各异势，会合何时谐",//
    "曾经沧海难为水，除却巫山不是云",//
    "入我相思门，知我相思苦，长相思兮长相忆，短相思兮无穷极",//
    "这次我离开你，是风，是雨，是夜晚； 你笑了笑，我摆一摆手，一条寂寞的路便展向两头了",//
    "有美人兮，见之不忘，一日不见兮，思之如狂",//
    "相思相见知何日？此时此夜难为情",//
    "两情若是久长时，又岂在朝朝暮暮",//
    "死生契阔，与子成说执子之手，与子偕老",//
    "衣带渐宽终不悔，为伊消得人憔悴"];

var poemCount = poems.length;

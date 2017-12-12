/**标题*/
var say_title = "这是我们奋斗的时光";

/**寄语*/
var say_jy = "奋斗知道永远";

var say_time = "";

var say_people = "留学的真相";


function say_init() {
    //
    say_title = get_query_string("say_title");
    document.getElementById("say_title").innerHTML = say_title;
    //
    say_jy = get_query_string("say_jy");
    document.getElementById("say_jy").innerHTML = say_jy;
    //
    say_people = get_query_string("say_people");
    document.getElementById("say_people").innerHTML = say_people;
}
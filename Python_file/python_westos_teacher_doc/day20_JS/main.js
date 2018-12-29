function init() {

    //书写轮播图显示的定时操作;
    setInterval('changeImg()', 3000);


    //设置广告图片的定时操作, setime不加var, 为全局变量， 其他函数里面也可以使用;
    setime = setInterval('showAd()', 1000);
}


// 书写显示轮播图的函数
// 定义一全局变量， 控制图片循环的顺序;
var i = 1;

function changeImg() {
    // 每次触发事件， 则i+1;实现下一张照片;
    i++;
    // 修改照片的链接为下一张照片
    document.getElementById("img").src = "img/img" + i + ".jpg";
    // 6为轮播图片的总数， 如果i===6， 则重头轮播, 重置i为1;
    if (i === 6) {
        i = 0;
    }
}


//书写显示广告图片的函数;
function showAd() {
    //获取广告图片的属性
    var adEle = document.getElementById('ad_img');
    //修改广告图片元素里面的属性并让其显示;
    adEle.style.display = "block";

    //清除显示图片的定时操作;传递设置定时的值;
    clearInterval(setime);

    //设置隐藏图片的定时操作;
    hiddentime = setInterval("hiddenAd()", 3000);
}


function hiddenAd() {
    //获取广告图片的属性,修改广告图片元素里面的属性并让其隐藏;
    document.getElementById('ad_img').style.display = "none";

    //清除隐藏图片的定时操作;传递设置定时的值;
    clearInterval(hiddentime);

}


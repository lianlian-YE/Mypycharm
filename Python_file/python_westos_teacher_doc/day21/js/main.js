function init() {
    //每隔固定时间， 去修改图片(changeImg()),
    // setInterval默认时间单位为毫秒；
    setInterval('changeImg()', 1000);
    //每隔1秒， 去显示广告;
    //设置广告图片的定时操作,（*****在js里面， 没有var， 则变量为全局变量;）
    displayTime = setInterval('showAd()', 1000);
}

var i = 1;

function changeImg() {
//                var img = document.getElementById('img').src;
//                alert(img);

//                document.getElementById('img').src = 'img/img2.jpg'
    // 当点击下一页的时候， 循环改变图片的内容;

    // 每次触发事件， 则i+1;实现下一张照片;
    i++;
    // 修改照片的链接为下一张照片
    document.getElementById("img").src = "img/img" + i + ".jpg";
    // 6为轮播图片的总数， 如果i===6， 则重头轮播, 重置i为1;
    if (i === 6) {
        i = 0;
    }
}

function showAd() {
    //显示广告的函数
    // 1. 获取广告图片的属性;
    document.getElementById('ad').style.display = "block";
    //2. 清除显示图片的定时操作;
    clearInterval(displayTime);

    //3. 设置隐藏图片的定时任务;
    hidtime = setInterval('hidAd()', 1000);
}


function hidAd() {
    // 1. 获取广告图片的属性;
    document.getElementById('ad').style.display = "none";
    //2. 清除隐藏图片的定时操作;
    clearInterval(hidtime);
}